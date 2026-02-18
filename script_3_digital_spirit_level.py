"""
================================================================================
SCRIPT 3: DIGITAL SPIRIT LEVEL - IMU/Accelerometer
================================================================================

TEACHER'S INTRO:
----------------
This script introduces students to:
1. Reading motion/orientation data from an accelerometer
2. Understanding 3D space (X, Y, Z axes)
3. Using mathematical logic to make decisions
4. Controlling individual LED pixels
5. Creating visual feedback for motion

ANALOGY: A spirit level (the tool builders use) has a bubble that moves to
show which way something is tilted. Our Pi will do the same thing, but with
LEDs instead of a bubble!

REAL-WORLD CONNECTION: This same technology is in your smartphone - it's
how your phone knows to rotate the screen when you turn it sideways!

EXPECTED OUTCOME: When students tilt the Pi, LEDs will light up on the side
that's tilted down, just like a bubble moves in a spirit level.

================================================================================
"""

# Import required libraries
from sense_hat import SenseHat
import time

# Create the SenseHat object
sense = SenseHat()

# Define colors for our spirit level
BUBBLE_COLOR = (0, 255, 255)  # Cyan (light blue) - represents the bubble
OFF_COLOR = (0, 0, 0)          # Black (LED off)

print("=== DIGITAL SPIRIT LEVEL STARTING ===")
print("Tilt your Raspberry Pi and watch the LEDs!")
print("Press Ctrl+C to stop\n")

# Function to light up pixels on a specific edge of the matrix
def light_up_edge(edge_name):
    """
    Lights up one edge of the 8x8 LED matrix to show which way it's tilted.

    Edge names: 'top', 'bottom', 'left', 'right'
    """
    # Clear the display first
    sense.clear()

    # The LED matrix is 8x8 (rows 0-7, columns 0-7)
    # Top-left corner is (0, 0), bottom-right is (7, 7)

    if edge_name == "top":
        # Light up the top row (row 0)
        for x in range(8):
            sense.set_pixel(x, 0, BUBBLE_COLOR)

    elif edge_name == "bottom":
        # Light up the bottom row (row 7)
        for x in range(8):
            sense.set_pixel(x, 7, BUBBLE_COLOR)

    elif edge_name == "left":
        # Light up the left column (column 0)
        for y in range(8):
            sense.set_pixel(0, y, BUBBLE_COLOR)

    elif edge_name == "right":
        # Light up the right column (column 7)
        for y in range(8):
            sense.set_pixel(7, y, BUBBLE_COLOR)

    elif edge_name == "level":
        # Pi is level - light up center pixels
        sense.set_pixel(3, 3, (0, 255, 0))  # Green
        sense.set_pixel(4, 3, (0, 255, 0))
        sense.set_pixel(3, 4, (0, 255, 0))
        sense.set_pixel(4, 4, (0, 255, 0))

# Main loop - continuously check orientation
try:
    while True:
        # Get accelerometer data
        # Accelerometer measures which way gravity is pulling
        # Returns a dictionary with 'pitch', 'roll', and 'yaw' in degrees
        orientation = sense.get_orientation()

        # Extract pitch and roll
        # PITCH: tilting forward/backward (like nodding your head)
        # ROLL: tilting left/right (like shaking your head "no")
        pitch = orientation['pitch']
        roll = orientation['roll']

        # The accelerometer gives us values from 0 to 360 degrees
        # We need to convert these to understand which way is "down"

        # Adjust pitch to range from -180 to 180 for easier logic
        if pitch > 180:
            pitch = pitch - 360

        # Adjust roll to range from -180 to 180
        if roll > 180:
            roll = roll - 360

        # Set a threshold - how much tilt before we react?
        # 20 degrees is a noticeable tilt but not extreme
        tilt_threshold = 20

        # Check which direction has the strongest tilt
        if pitch < -tilt_threshold:
            # Tilted forward - bottom edge is down
            light_up_edge("bottom")
            print("⬇️  Tilted FORWARD (bottom down)")

        elif pitch > tilt_threshold:
            # Tilted backward - top edge is down
            light_up_edge("top")
            print("⬆️  Tilted BACKWARD (top down)")

        elif roll < -tilt_threshold:
            # Tilted to the right
            light_up_edge("right")
            print("➡️  Tilted RIGHT")

        elif roll > tilt_threshold:
            # Tilted to the left
            light_up_edge("left")
            print("⬅️  Tilted LEFT")

        else:
            # Not tilted much - it's level!
            light_up_edge("level")
            print("✅ LEVEL")

        # Small delay before checking again
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean exit when user presses Ctrl+C
    print("\n\n=== DIGITAL SPIRIT LEVEL STOPPED ===")
    sense.clear()
    print("Display cleared. Goodbye!")

"""
================================================================================
TROUBLESHOOTING & CHALLENGES
================================================================================

COMMON ISSUES:
--------------
1. LEDs lighting up on wrong side:
   → The orientation of the Sense HAT matters!
   → Try adjusting which edge lights up in the if/elif statements

2. Too sensitive or not sensitive enough:
   → Change the tilt_threshold value
   → Lower number = more sensitive (reacts to small tilts)
   → Higher number = less sensitive (needs bigger tilts)

3. Jittery/flickering LEDs:
   → Increase the time.sleep() value to 0.2 or 0.3
   → This gives more stable readings

4. "KeyError" with orientation data:
   → Make sure the Sense HAT is properly connected
   → Try using get_accelerometer_raw() instead

CHALLENGES FOR EARLY FINISHERS:
-------------------------------
EASY:
1. Change the BUBBLE_COLOR to a different color
2. Change the tilt_threshold to make it more or less sensitive
3. Make the "level" indicator a different color (try yellow or purple)

MEDIUM:
4. Add diagonal detection - what if it's tilted forward AND left?
   (Hint: check both pitch and roll at the same time)

5. Create a "tilt meter" that shows HOW MUCH it's tilted:
   - 1 LED for small tilt
   - 4 LEDs for medium tilt
   - 8 LEDs for large tilt

6. Display an ARROW on the LED matrix instead of just a line
   (Research the set_pixels() method)

HARD:
7. Create a "balance game":
   - User must keep the Pi level for 10 seconds
   - If they succeed, flash green
   - If they tilt it, flash red and restart the timer

8. Make a "shake detector":
   - Use get_accelerometer_raw() to detect rapid movement
   - Flash the LEDs when the Pi is shaken

9. Create a "rolling ball" simulation:
   - Show a single lit pixel that "rolls" to the lowest side
   - Make it move smoothly, not jump instantly

EXTENSION ACTIVITY:
-------------------
SCIENCE EXPERIMENT: "Understanding Gravity"
1. Have students predict: What happens if you hold the Pi upside down?
2. Test it: Does the bubble still "fall" to the lowest point?
3. Discuss: Why does this work? (Gravity always pulls down)

CHALLENGE: "Build a Tilt Controller"
Combine this with Script 1:
- Tilt left = scroll message left
- Tilt right = scroll message right
- Level = stop scrolling

DISCUSSION QUESTIONS:
--------------------
1. What other devices use accelerometers? (Game controllers, fitness trackers)
2. How does your phone know when you've dropped it?
3. Could you use this to detect if someone moved your Pi?

================================================================================
"""
