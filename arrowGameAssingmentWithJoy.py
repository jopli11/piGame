import random
import time
from sense_hat import SenseHat

sense = SenseHat()

r = [255, 0, 0]
w = [255, 255, 255]
g = [0, 255, 0]
e = [0, 0, 0]

arrow = [e,e,e,w,w,e,e,e,e,e,w,w,w,w,e,e,e,w,e,w,w,e,w,e,w,e,e,w,w,e,e,w,e,e,e,w,w,e,e,e,e,e,e,w,w,e,e,e,e,e,e,w,w,e,e,e,e,e,e,w,w,e,e,e]

arrow_red = [e,e,e,r,r,e,e,e,e,e,r,r,r,r,e,e,e,r,e,r,r,e,r,e,r,e,e,r,r,e,e,r,e,e,e,r,r,e,e,e,e,e,e,r,r,e,e,e,e,e,e,r,r,e,e,e,e,e,e,r,r,e,e,e]

arrow_green = [e,e,e,g,g,e,e,e,e,e,g,g,g,g,e,e,e,g,e,g,g,e,g,e,g,e,e,g,g,e,e,g,e,e,e,g,g,e,e,e,e,e,e,g,g,e,e,e,e,e,e,g,g,e,e,e,e,e,e,g,g,e,e,e]


def wait_for_movement():
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = round(x, 0)
    y = round(y, 0)

    while x == 0 and y == 0 and z == 0:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = round(x, 0)
        y = round(y, 0)

def main():
    pause = 3
    score = 0
    play = True

    sense.show_message("Keep the arrow pointing up", scroll_speed=0.05, text_colour=[100,100,100])

    while play:
        angle = random.choice([0, 90, 180, 270])
        sense.set_rotation(angle)	

        sense.set_pixels(arrow)

        time.sleep(pause)

        # Check for joystick or tilt input
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']

        x = round(x, 0)
        y = round(y, 0)

        if (x == -1 and angle == 180) or (x == 1 and angle == 0) or (y == -1 and angle == 90) or (y == 1 and angle == 270):
            sense.set_pixels(arrow_green)
            score += 1
        else:
            for event in sense.stick.get_events():
                if event.action == "pressed":
                    if event.direction == "up" and angle == 0:
                        sense.set_pixels(arrow_green)
                        score += 1
                    elif event.direction == "down" and angle == 180:
                        sense.set_pixels(arrow_green)
                        score += 1
                    elif event.direction == "left" and angle == 270:
                        sense.set_pixels(arrow_green)
                        score += 1
                    elif event.direction == "right" and angle == 90:
                        sense.set_pixels(arrow_green)
                        score += 1
                    else:
                        sense.set_pixels(arrow_red)
                        play = False

        pause = pause * 0.95
        time.sleep(0.5)

    msg = "GAME OVER, Your score was %s" % score
    sense.show_message(msg, scroll_speed=0.05, text_colour=[100,100,100])

if __name__ == '__main__':
    main()