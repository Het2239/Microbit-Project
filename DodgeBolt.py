from microbit import *
import radio
last_message = ""

# === RADIO SETUP ===
radio.on()
radio.config(group=42)

# === CONFIGURATION ===
role = "shooter"  # Set manually to "dodger" on the other micro:bit
my_x = 0
my_y = 4
last_sent_x = my_x

# === ROLE CONFIRMATION ===
confirmed = False
send_attempted = False
start_time = running_time()

def send_reliable(msg):
    for _ in range(4):
        radio.send(msg)
        sleep(20)
def on_received(message):
    global last_message,role
    is_role_switch = message.startswith("c,")

    if is_role_switch or message != last_message:
        if message != last_message:
            last_message = message
        if message == "shooter":
            display.scroll("Dodge!", delay=50)
        elif message == "dodger":
            display.scroll("Shoot!", delay=50)
        elif message.startswith("c,"):
            try:
                _, val = message.split(",")
                val = int(val)
                new_role = "shooter" if val == 0 else "dodger"
                if new_role != role:
                    role = new_role
                    display.scroll("Shoot!" if role == "shooter" else "Dodge!", delay=50)
                    reset_positions()
            except:
                pass

while not confirmed and running_time() - start_time < 5000:
    if not send_attempted:
        send_reliable(role)
        send_attempted = True

    msg = radio.receive()
    if msg in ("shooter", "dodger") and msg == role:
        role ="shooter" if msg == "dodger" else "dodger"
        confirmed = True
        
        send_reliable(role)
        on_received(msg)     

        break
    elif msg in ("shooter", "dodger") and msg != role:
        confirmed = True
        
        send_reliable(role)
        on_received(msg)     

        break
    sleep(100)

if not confirmed:
    display.scroll("No reply!", delay=50)
    reset()

# === INITIAL VARIABLES ===
position = my_x
other_x = 0
last_sent_x = position
last_ab_pressed = False

# Bullet tracking
bullet_active = False
bullet_x = 0
bullet_y = 0
bullet_direction = 0  # -1 for shooter (up), +1 for dodger

# Bullet counter for shooter
bullets_fired = 0

# Scores
my_score = 0
opponent_score = 0
bullet_hit_checked = False

# === TIMER ===
game_start_time = running_time()

# === SHRINK FLAGS ===
shrink1 = False
shrink2 = False

# === FUNCTIONS ===
def reset_positions():
    global my_x, my_y, last_sent_x, position, other_x
    my_x = 1 if shrink1 else 0
    if shrink2:
        my_y = 2
    else:
        my_y = 3 if shrink1 else 4
    last_sent_x = my_x
    position = my_x
    other_x = 0
    last_sent_x = position

def shrink_game1():
    global position, last_sent_x, my_y
    position = 1  
    last_sent_x = position
    my_y = 3
    send_reliable("a," + str(position))
    display.scroll("Shrink!", delay=50)

def shrink_game2():
    global my_y
    my_y = 2
    display.scroll("Shrink More!", delay=50)

# === MAIN GAME LOOP ===
while True:
    elapsed = running_time() - game_start_time

    # --- Timer check for ending ---
    if elapsed > 60000:  # 60 seconds
        display.clear()
        sleep(200)
        
        if my_score > opponent_score:
            display.scroll("Win!", delay=50)
        elif my_score < opponent_score:
            display.scroll("Lose!", delay=50)
        else:
            display.scroll("Draw", delay=50)
        
        sleep(500)
        display.scroll("You: " + str(my_score) + " Opp: " + str(opponent_score), delay=50)
        break

    # --- Timer check for shrinking ---
    if not shrink1 and elapsed > 25000:  # 25 seconds
        shrink1 = True
        shrink_game1()

    if not shrink2 and elapsed > 45000:  # 45 seconds
        shrink2 = True
        shrink_game2()

    # --- Handle movement ---
    moved = False
    min_x = 1 if shrink1 else 0
    max_x = 3 if shrink1 else 4

    if button_a.was_pressed() and position > min_x:
        position -= 1
        moved = True
    if button_b.was_pressed() and position < max_x:
        position += 1
        moved = True

    if moved and position != last_sent_x:
        send_reliable("a," + str(position))
        last_sent_x = position

     # --- Handle receiving messages ---
    msg = radio.receive()
    if msg:
        try:
            t, val = msg.split(",")
            val = int(val)
            if t == "a":
                other_x = val
            elif t == "b":
                if role == "dodger":
                    if not bullet_active:
                        bullet_active = True
                        bullet_x = 4 - val  # Mirror bullet x
                        bullet_y = 1
                        bullet_direction = +1
                        bullet_hit_checked = False
            elif t == "c":  # Receive your role change
                on_received(msg)
                bullets_fired = 0
                
        except:
            pass
    
    # --- Handle shooting ---
    ab_now = button_a.is_pressed() and button_b.is_pressed()
    if ab_now and not last_ab_pressed:
        if role == "shooter":
            send_reliable("b," + str(position))
            if not bullet_active:
                bullet_active = True
                bullet_x = position
                bullet_y = my_y - 1  # Adjusted for dynamic my_y
                bullet_direction = -1
                bullet_hit_checked = False
                bullets_fired += 1

    last_ab_pressed = ab_now

    # --- Mirror opponent x for display ---
    mirrored_x = 4 - other_x

    # === DRAW SCREEN ===
    display.clear()

    # Draw walls if shrink1 or shrink2
    display.clear()
    if shrink1 or shrink2:
        # left/right + bottom
        for y in range(5):
            display.set_pixel(0, y, 3)
            display.set_pixel(4, y, 3)
        for x in range(5):
            display.set_pixel(x, 4, 3)
    if shrink2:
        # extra upper border at row 3
        for x in range(5):
            display.set_pixel(x, 3, 3)
    

    # Draw your player and opponent
    display.set_pixel(position, my_y, 9)
    display.set_pixel(mirrored_x, 0, 6)

    # Bullet animation
    if bullet_active:
        display.set_pixel(bullet_x, bullet_y, 7)

        if role == "dodger":
            if bullet_y == my_y and bullet_x == position and not bullet_hit_checked:
                opponent_score += 1
                bullet_hit_checked = True
                display.scroll("+", delay=50)

        if role == "shooter":
            if bullet_y == 0 and bullet_x == mirrored_x and not bullet_hit_checked:
                my_score += 1
                bullet_hit_checked = True
                display.scroll("X", delay=50)

        bullet_y += bullet_direction

        if bullet_y < 0 or bullet_y > my_y:
            if not bullet_hit_checked:
                if role == "dodger":
                    my_score += 1
                else:
                    opponent_score += 1
            bullet_active = False
            
            if bullets_fired >= 2:
                bullets_fired = 0
                sleep(300)
                if role == "shooter":
                    role = "dodger"
                    display.scroll("Dodge!", delay=50)
                else:
                    role = "shooter"
                    display.scroll("Shoot!", delay=50)
                send_reliable("c," + str(1 if role == "shooter" else 0))
                reset_positions()

    sleep(100)