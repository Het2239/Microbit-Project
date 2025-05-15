from microbit import *
import random
import music

# Game state
score = 0
lives = 5
level = 1
fruits_in_level = 0
max_fruits = [15, 10, 10]  # Number of fruits per level

# Fruit state
fruit_x = random.randint(0, 4)
fruit_y = 0
fruit_speed = random.randint(400, 800)

# Bullet state
bullet_active = False
bullet_x = 0
bullet_y = 2  # Bullet starts at middle row (row 2)

# Timers
last_bullet_move = running_time()
last_fruit_move = running_time()
last_button_press = 0
bullet_interval = 200
button_cooldown = 500

# Game Boy Style Sound Effects
GAME_START_MUSIC = [
    "E5:2", "G#5:2", "B5:2", "E6:8"
]

SHOOT_SOUND = ["A#5:1", "C6:1"]

HIT_SOUND = [
    "C6:1", "E6:1", "G6:1", "C7:2"
]

CHANGE_ROW_SOUND = ["B4:1"]

FRUIT_MISS_SOUND = [
    "F#4:2", "D#4:4"
]

LEVEL_UP_MUSIC = [
    "G5:1", "C6:1", "E6:1", "G6:1", 
    "C7:3", "G6:3"
]

LEVEL_CLEAR_MUSIC = [
    "C6:2", "E6:2", "G6:2", "C7:4",
    "G6:2", "E6:2", "C6:4"
]

GAME_OVER_MELODY = [
    "C5:4", "G4:4", "E4:4",
    "A4:4", "B4:4", "A4:4",
    "G#4:4", "B4:4", "C5:8"
]

VICTORY_MUSIC = [
    "C6:2", "C6:2", "C6:2",
    "G5:4", "A5:2", "C6:4",
    "G5:4", "E5:8"
]

def reset_fruit():
    global fruit_x, fruit_y, fruit_speed, fruits_in_level, last_fruit_move
    fruit_x = random.randint(0, 4)
    fruit_y = 0
    if level == 1:
        fruit_speed = random.randint(400, 500)
    elif level == 2:
        fruit_speed = random.randint(350, 800)
    else:
        fruit_speed = random.randint(300, 800)
    fruits_in_level += 1
    last_fruit_move = running_time()  # prevent immediate drop
    draw()
    if fruits_in_level >= max_fruits[level-1]:
        advance_level()

def advance_level():
    global level, fruits_in_level
    display.clear()
    if level < 3:
        music.play(LEVEL_UP_MUSIC)
        level += 1
        fruits_in_level = 0
        display.scroll("LEVEL " + str(level), delay=70)
        sleep(500)
    else:
        music.play(VICTORY_MUSIC)
        display.scroll("YOU WIN!", delay=70)
        display.scroll("SCORE:" + str(score), delay=70)
        end_game(victory=True)

def reset_bullet():
    global bullet_active, bullet_x
    bullet_active = False
    bullet_x = 0

def draw():
    display.clear()
    if 0 <= fruit_y <= 4:
        display.set_pixel(fruit_x, fruit_y, 9)
    if bullet_active and 0 <= bullet_x <= 4:
        display.set_pixel(bullet_x, bullet_y, 5)

def end_game(victory=False):
    display.clear()
    if not victory:
        for _ in range(3):
            display.show(Image.SAD); sleep(200)
            display.clear(); sleep(200)
        music.play(GAME_OVER_MELODY)
        display.scroll("GAME OVER", delay=70)
    display.scroll("SCORE:" + str(score), delay=70)
    display.clear()
    while True:
        sleep(10000)

# Start
music.play(GAME_START_MUSIC); sleep(500)
display.scroll("LEVEL 1", delay=70); sleep(500)
bullet_y = 2
draw()

while lives > 0:
    now = running_time()

    # bullet movement + collision
    if bullet_active and now - last_bullet_move >= bullet_interval:
        bullet_x += 1
        last_bullet_move = now
        if bullet_x == fruit_x and bullet_y == fruit_y:
            score += 1
            music.play(HIT_SOUND, wait=False)
            reset_fruit()
            reset_bullet()
        elif bullet_x > 4:
            reset_bullet()
        draw()

    # fruit movement
    if now - last_fruit_move >= fruit_speed:
        fruit_y += 1
        if level == 3 and random.randint(1,5)==1:
            fruit_x = max(0, min(4, fruit_x + random.choice([-1,1])))
        if fruit_y > 4:
            lives -= 1
            music.play(FRUIT_MISS_SOUND, wait=False)
            reset_fruit()
            if lives > 0:
                display.show(Image.HEART); sleep(200)
                display.clear(); display.scroll(str(lives), delay=50)
            else:
                end_game()
        last_fruit_move = now
        draw()

    # fire bullet
    if button_a.was_pressed() and not bullet_active and now - last_button_press > button_cooldown:
        bullet_active = True
        bullet_x = -1        # start off‑screen so first move lands at 0
        last_button_press = now
        music.play(SHOOT_SOUND, wait=False)
        draw()

    # change row
    if button_b.was_pressed() and now - last_button_press > button_cooldown/2:
        bullet_y = (bullet_y + 1) % 5
        last_button_press = now
        music.play(CHANGE_ROW_SOUND, wait=False)
        display.set_pixel(0, bullet_y, 3); sleep(100)
        draw()

    sleep(20)

# clear stray pixel then halt
display.clear()
while True:
    sleep(10000)