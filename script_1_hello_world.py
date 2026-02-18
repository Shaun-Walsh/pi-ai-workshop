"""
================================================================================
SCRIPT 1: HELLO WORLD - LED Matrix
================================================================================

TEACHER'S INTRO:
----------------
This script introduces students to:
1. Importing libraries (sense_hat)
2. Creating objects (instantiating the SenseHAT)
3. Using methods (show_message)
4. Understanding RGB color values (like in graphics/multimedia)
5. Controlling timing/speed parameters

ANALOGY: Think of the LED matrix like a tiny TV screen. Just like you can control
what appears on a monitor, you can control what appears on these 8x8 pixels.

EXPECTED OUTCOME: Students will see their custom message scroll across the
Sense HAT LED matrix in their chosen color.

================================================================================
"""

# Import the library that controls the Sense HAT
from sense_hat import SenseHat

# Create a SenseHat object - this is like turning on the device
sense = SenseHat()

# Define your message
# This is the text that will scroll across the LED matrix
message_text = "Hello Pi Workshop!"

# Define the text color using RGB values (Red, Green, Blue)
# RGB works like mixing light - each value goes from 0 to 255
# (255, 255, 255) = White
# (255, 0, 0) = Red
# (0, 255, 0) = Green
# (0, 0, 255) = Blue
text_color = (0, 255, 0)  # Bright Green

# Define the background color (the color behind the text)
background_color = (0, 0, 0)  # Black (LEDs off)

# Define the scroll speed
# Lower number = faster scroll
# Higher number = slower scroll
scroll_speed = 0.05  # seconds between each frame

# Display the scrolling message
# This method makes the text move across the screen
sense.show_message(
    message_text,           # The text to display
    scroll_speed,           # How fast it scrolls
    text_color,             # Color of the letters
    background_color        # Color of the background
)

# Clear the display when finished
sense.clear()

print("Message displayed successfully!")

"""
================================================================================
TROUBLESHOOTING & CHALLENGES
================================================================================

COMMON ISSUES:
--------------
1. "ModuleNotFoundError: No module named 'sense_hat'"
   → Solution: Run in terminal: sudo pip3 install sense-hat

2. Nothing appears on the LED matrix:
   → Check that the Sense HAT is properly attached to the GPIO pins
   → Try running with sudo: sudo python3 script_1_hello_world.py

3. Wrong colors appearing:
   → Remember RGB order: (Red, Green, Blue)
   → Each value must be between 0 and 255

CHALLENGES FOR EARLY FINISHERS:
-------------------------------
EASY:
1. Change the message to your own name
2. Change the text color to purple (hint: mix red and blue)
3. Make it scroll very slowly (try 0.1 or 0.2)

MEDIUM:
4. Make the background color dark blue instead of black
5. Display TWO different messages one after another with different colors
6. Create a rainbow effect by using multiple sense.show_message() calls
   with different colors

HARD:
7. Use a loop to make the message repeat 3 times
8. Create a color-changing animation where each letter is a different color
   (hint: you'll need to use set_pixels() for this - research it!)

EXTENSION ACTIVITY:
-------------------
Ask students: "What other RGB values could you try? Can you make orange? Pink?"
Have them create a "color palette" sheet with at least 5 different RGB
combinations and their resulting colors.

================================================================================
"""
