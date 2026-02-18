"""
================================================================================
ADVANCED 1: JOYSTICK BASICS - Event-Driven Programming
================================================================================

TEACHER'S INTRO:
----------------
This script introduces students to:
1. Event-driven programming (responding to user input)
2. The Sense HAT joystick (5-way: up, down, left, right, middle)
3. Dictionaries for data storage
4. Event loops
5. Real-time interactive programs

NEW CONCEPTS:
- Event listeners (waiting for things to happen)
- Event objects (information about what happened)
- Event types (pressed, released, held)

ANALOGY: The joystick is like a game controller. Your code "listens" for button
presses and responds - just like a video game reacts when you press buttons!

REAL-WORLD CONNECTION: All interactive programs work this way - apps, games,
websites all use event-driven programming to respond to user actions.

EXPECTED OUTCOME: Students can control the LED matrix by pressing the joystick
in different directions. Immediate, interactive feedback!

================================================================================
"""

# Import required libraries
from sense_hat import SenseHat
import time

# Initialize Sense HAT
sense = SenseHat()

# Clear the display to start fresh
sense.clear()

# Define colors for each direction
COLORS = {
    'up': (255, 0, 0),      # Red
    'down': (0, 0, 255),    # Blue
    'left': (0, 255, 0),    # Green
    'right': (255, 255, 0), # Yellow
    'middle': (255, 0, 255) # Magenta (purple)
}

# Counter to track how many times each direction was pressed
direction_count = {
    'up': 0,
    'down': 0,
    'left': 0,
    'right': 0,
    'middle': 0
}

print("=" * 60)
print("🕹️  JOYSTICK BASICS - Event-Driven Programming")
print("=" * 60)
print("\nPress the joystick in any direction!")
print("The LED matrix will light up with the corresponding color:")
print("  ⬆️  UP = Red")
print("  ⬇️  DOWN = Blue")
print("  ⬅️  LEFT = Green")
print("  ➡️  RIGHT = Yellow")
print("  🔘 MIDDLE (click) = Magenta\n")
print("Press Ctrl+C to exit\n")

# Main event loop
try:
    while True:
        # Wait for a joystick event
        # This is a "blocking" call - the program pauses here until
        # the user presses the joystick
        event = sense.stick.wait_for_event()

        # An "event" is a Python object with information about what happened
        # event.direction = which direction was pressed (up, down, left, right, middle)
        # event.action = what type of action (pressed, released, held)

        # We only want to respond to "pressed" events (not released or held)
        if event.action == "pressed":
            direction = event.direction

            # Increment the counter for this direction
            direction_count[direction] += 1

            # Get the color for this direction
            color = COLORS[direction]

            # Light up the LED matrix with this color
            sense.clear(color)

            # Print to console
            print(f"🕹️  {direction.upper():6} pressed! (Total: {direction_count[direction]:2} times)")

            # Keep the color displayed for a moment
            time.sleep(0.3)

            # Turn off the LEDs
            sense.clear()

except KeyboardInterrupt:
    # User pressed Ctrl+C to exit
    print("\n\n" + "=" * 60)
    print("📊 JOYSTICK STATISTICS")
    print("=" * 60)

    # Calculate total presses
    total_presses = sum(direction_count.values())

    print(f"\nTotal presses: {total_presses}\n")

    # Show breakdown by direction
    for direction, count in direction_count.items():
        # Calculate percentage
        if total_presses > 0:
            percentage = (count / total_presses) * 100
        else:
            percentage = 0

        # Create a simple bar chart
        bar = "█" * count

        print(f"{direction.upper():6}: {count:3} ({percentage:5.1f}%) {bar}")

    # Find most-pressed direction
    if total_presses > 0:
        most_pressed = max(direction_count, key=direction_count.get)
        print(f"\n🏆 Most pressed: {most_pressed.upper()} ({direction_count[most_pressed]} times)")

    # Clean up
    sense.clear()
    print("\n✅ Joystick program ended. LEDs cleared.\n")

"""
================================================================================
TROUBLESHOOTING & CHALLENGES
================================================================================

COMMON ISSUES:
--------------
1. Joystick not responding:
   → Make sure Sense HAT is properly connected (all 40 GPIO pins)
   → Try running with sudo: sudo python3 advanced_1_joystick_basics.py
   → Reboot the Pi: sudo reboot

2. Wrong colors appearing:
   → Check the COLORS dictionary - make sure RGB values are correct
   → Remember: (Red, Green, Blue) each 0-255

3. Program seems frozen:
   → It's not frozen! It's waiting for you to press the joystick
   → This is normal behavior for event-driven programs

4. LEDs stay on after pressing:
   → Increase the sleep time (change 0.3 to 0.5 or 1.0)
   → Or remove the sense.clear() to keep colors visible

UNDERSTANDING EVENT-DRIVEN PROGRAMMING:
--------------------------------------
Traditional programs: Execute line by line, top to bottom
Event-driven programs: Wait for events (button presses), then respond

This is how ALL interactive software works:
- Video games (wait for controller input)
- Apps (wait for button clicks)
- Websites (wait for mouse clicks/keyboard input)

CHALLENGES FOR EARLY FINISHERS:
-------------------------------
EASY:
1. Change the colors for each direction
2. Change the sleep time to make LEDs stay on longer
3. Add a sixth direction (try detecting "held" actions instead of "pressed")

4. Make it a "color mixer":
   - Start with black screen
   - UP = add red (+10 to red value)
   - DOWN = add blue
   - LEFT = add green
   - MIDDLE = reset to black

MEDIUM:
5. Create a "drawing" program:
   - Track cursor position (x, y)
   - Joystick moves the cursor
   - MIDDLE = toggle pixel on/off
   - Draw patterns on the LED matrix!

6. Make a "counter" program:
   - UP = increment counter (+1)
   - DOWN = decrement counter (-1)
   - MIDDLE = reset to 0
   - Display the number on LED matrix (use sense.show_message())

7. Create a "color chooser":
   - UP/DOWN cycles through colors (red, green, blue, yellow, etc.)
   - MIDDLE confirms selection
   - Display chosen color name

8. Add sound effects:
   - Different beep for each direction
   - Research: pygame.mixer for playing sounds

HARD:
9. Create a "password system":
   - User must enter a sequence (e.g., UP, UP, DOWN, LEFT, RIGHT, MIDDLE)
   - If correct: flash green (success)
   - If wrong: flash red (denied)
   - Hint: Store sequence in a list, compare with user input

10. Build a "menu system":
    - UP/DOWN navigates menu items
    - MIDDLE selects item
    - Display menu options on LED matrix
    - Execute different functions based on selection

11. Create a "reaction timer":
    - Display random color
    - User must press corresponding direction as fast as possible
    - Measure and display reaction time
    - Keep track of best time

12. Make a "Simon Says" game:
    - Program shows a sequence of colors
    - User must repeat the sequence using joystick
    - Sequence gets longer each round
    - Game over if user makes a mistake

EXTENSION ACTIVITY:
-------------------
PROJECT: "Joystick-Controlled Drawing App"
Create a full drawing application:
- Cursor moves with joystick (up/down/left/right)
- MIDDLE = place/remove pixel
- Keep track of cursor position
- Display cursor as blinking pixel
- Save "drawings" as patterns

DISCUSSION QUESTIONS:
--------------------
1. What's the difference between event.action "pressed", "released", and "held"?
   - Pressed: Button just pushed down
   - Released: Button just let go
   - Held: Button is being held down continuously

2. Why do we use wait_for_event() instead of checking constantly?
   - More efficient (saves CPU power)
   - Prevents missing rapid button presses
   - This is called "event-driven" vs "polling"

3. What other devices use joysticks or similar input?
   - Game controllers (Xbox, PlayStation)
   - Drones (remote control)
   - Wheelchairs (joystick control)
   - Industrial machinery

4. How could you make this program more responsive?
   - Remove the sleep() delay
   - Use non-blocking event checking
   - Use threading (advanced)

REAL-WORLD APPLICATIONS:
-----------------------
- Game controllers for accessibility
- Remote control systems
- Interactive art installations
- Control panels for machinery
- Menu navigation systems

PROGRAMMING CONCEPTS LEARNED:
----------------------------
✅ Event loops (while True + wait_for_event)
✅ Event objects (event.direction, event.action)
✅ Dictionaries (COLORS, direction_count)
✅ Conditional logic (if event.action == "pressed")
✅ Data aggregation (counting and statistics)
✅ User interaction (real-time response to input)

================================================================================
"""
