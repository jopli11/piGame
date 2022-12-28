from sense_hat import SenseHat
import time
import random

# Import the SenseHat module and create a SenseHat object
sense = SenseHat()

# Empty LED variable declerations
empty = [0, 0, 0]

# Coloured LEDs variable declerations
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]

# Declare variables for arrow shapes using the empty and colored LED variables
arrow = [
empty, empty, empty, white, white, empty, empty, empty,
empty, empty, white, white, white, white, empty, empty,
empty, white, empty, white, white, empty, white, empty,
white, empty, empty, white, white, empty, empty, white,
empty, empty, empty, white, white, empty, empty, empty,
empty, empty, empty, white, white, empty, empty, empty,
empty, empty, empty, white, white, empty, empty, empty,
empty, empty, empty, white, white, empty, empty, empty
]

arrow_red = [
empty, empty, empty, red, red, empty, empty, empty,
empty, empty, red, red, red, red, empty, empty,
empty, red, empty, red, red, empty, red, empty,
red, empty, empty, red, red, empty, empty, red,
empty, empty, empty, red, red, empty, empty, empty,
empty, empty, empty, red, red, empty, empty, empty,
empty, empty, empty, red, red, empty, empty, empty,
empty, empty, empty, red, red, empty, empty, empty
]

arrow_green = [
empty, empty, empty, green, green, empty, empty, empty,
empty, empty, green, green, green, green, empty, empty,
empty, green, empty, green, green, empty, green, empty,
green, empty, empty, green, green, empty, empty, green,
empty, empty, empty, green, green, empty, empty, empty,
empty, empty, empty, green, green, empty, empty, empty,
empty, empty, empty, green, green, empty, empty, empty,
empty, empty, empty, green, green, empty, empty, empty
]

# Declare variables for game play, including pause time, score, angle, and play status
pause = 3
score = 0
angle = 0
play = True

# Display a message to the player to keep the arrow pointing up
sense.show_message("Keep the arrow pointing up", scroll_speed=0.05, text_colour=[100,100,100])

# Start the game loop
while play:
    # Choose a new random angle
    angle = random.choice([0, 90, 180, 270])

    # Set the rotation of the Sense HAT and display the arrow
    sense.set_rotation(angle)	
    sense.set_pixels(arrow)

    # Pause for the specified time
    time.sleep(pause)

    # Take an accelerometer reading and calculate the x and y values
    acceleration = sense.get_accelerometer_raw()
    x = round(acceleration['x'], 0)
    y = round(acceleration['y'], 0)

    # Check if the x and y values and the current angle match a correct combination
    if (x, y, angle) in [(1, 0, 0), (-1, 0, 180), (0, -1, 90), (0, 1, 270)]:
        sense.set_pixels(arrow_green)
        score += 1
    else:
        sense.set_pixels(arrow_red)
        play = False
        break
        
    # Decrease the pause time and wait for half a second
    pause = pause * 0.95
    time.sleep(0.5)

# Display the game over message with the final score
msg = "GAME OVER, Your score was %s" % score
sense.show_message(msg, scroll_speed=0.05, text_colour=[100,100,100])