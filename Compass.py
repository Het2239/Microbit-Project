from microbit import *
import math

# Calibrate compass
# compass.calibrate()

def get_pitch():
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    
    pitch = math.atan2(x, math.sqrt(y**2 + z**2))
    return math.degrees(pitch)

def in_xz_plane(threshold=30):
    
    pitch = get_pitch()
    return abs(pitch) < threshold

while True:
    if in_xz_plane():
        heading = compass.heading()

        if (337 <= heading <= 360) or (0 <= heading < 22):
            display.show('N')
        elif 22 <= heading < 67:
            display.show('NE')
        elif 67 <= heading < 112:
            display.show('E')
        elif 112 <= heading < 157:
            display.show('SE')
        elif 157 <= heading < 202:
            display.show('S')
        elif 202 <= heading < 247:
            display.show('SW')
        elif 247 <= heading < 292:
            display.show('W')
        elif 292 <= heading < 337:
            display.show('NW')
        else:
            display.show('?')
    else:
        display.clear()

    sleep(300)