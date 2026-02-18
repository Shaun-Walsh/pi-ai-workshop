"""
================================================================================
ADVANCED 2: DIGITAL DICE - Shake to Roll!
================================================================================

TEACHER'S INTRO:
----------------
This script introduces students to:
1. Combining accelerometer and LED display
2. Creating custom LED patterns (dice faces)
3. Random number generation
4. Shake/movement detection
5. State machines (waiting vs rolling vs displaying)

NEW CONCEPTS:
- 2D lists (representing LED matrix patterns)
- Magnitude calculation (Pythagorean theorem in 3D)
- State management (tracking what the program is doing)
- Animation (rolling effect)

ANALOGY: This is like a real dice, but digital! Shake your Pi like you'd
shake dice in your hand, and it "rolls" a random number and shows it on the
LED matrix as a dice face.

REAL-WORLD CONNECTION: Digital dice are used in board game apps, casino games,
and random number generators. Movement detection is used in step counters,
shake-to-shuffle music apps, and fall detection systems.

EXPECTED OUTCOME: Students shake the Pi, see a rolling animation, then see
a dice face (1-6 dots) displayed on the LED matrix.

================================================================================
"""

# Import required libraries
from sense_hat import SenseHat
import time
import random
import math

# Initialize Sense HAT
sense = SenseHat()
sense.clear()

# Define colors
WHITE = (255, 255, 255)  # Dice dots
BLACK = (0, 0, 0)        # Dice background
RED = (255, 0, 0)        # Rolling animation
YELLOW = (255, 255, 0)   # Rolling animation
GREEN = (0, 255, 0)      # Success flash

# OFF is just BLACK
OFF = BLACK

# DICE FACE PATTERNS
# Each pattern is an 8x8 grid where:
# 0 = black (empty)
# 1 = white (dot)

# We use 'W' for white and '.' for black to make it easier to visualize

dice_patterns = {
    1: [  # One dot in center
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
    2: [  # Two dots (diagonal)
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
    3: [  # Three dots (diagonal)
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
    4: [  # Four dots (corners)
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
    5: [  # Five dots (corners + center)
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
    6: [  # Six dots (two columns)
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
}

def display_dice_face(number):
    """
    Display a dice face on the LED matrix.

    Args:
        number (int): The dice value (1-6)
    """
    pattern = dice_patterns[number]

    # Convert pattern to pixel list
    for y in range(8):
        for x in range(8):
            if pattern[y][x] == 1:
                sense.set_pixel(x, y, WHITE)
            else:
                sense.set_pixel(x, y, BLACK)

def detect_shake():
    """
    Detect if the Pi has been shaken by measuring acceleration.

    Returns:
        bool: True if shake detected, False otherwise
    """
    # Get raw accelerometer data (in g's)
    accel = sense.get_accelerometer_raw()

    # Calculate total acceleration magnitude using Pythagorean theorem
    # In 3D: magnitude = sqrt(x² + y² + z²)
    x = accel['x']
    y = accel['y']
    z = accel['z']

    magnitude = math.sqrt(x**2 + y**2 + z**2)

    # Normal gravity is about 1g
    # If magnitude is significantly different from 1, the Pi is being moved
    # Threshold of 1.5 means fairly vigorous shaking required
    shake_threshold = 1.5

    return magnitude > shake_threshold

def rolling_animation():
    """
    Display a rolling animation (random numbers flashing quickly).
    """
    for i in range(10):  # Flash 10 random numbers
        random_number = random.randint(1, 6)
        display_dice_face(random_number)

        # Alternate colors for excitement
        # NOTE: low_light feature disabled - causes errors on some Sense HATs
        # if i % 2 == 0:
        #     sense.low_light = False
        # else:
        #     sense.low_light = True

        time.sleep(0.1)

    # Reset to normal brightness
    # sense.low_light = False

# Statistics tracking
roll_history = []
roll_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

print("=" * 60)
print("🎲 DIGITAL DICE - Shake to Roll!")
print("=" * 60)
print("\n🤚 Shake your Raspberry Pi to roll the dice!")
print("📊 Watch the LED matrix for the result")
print("🛑 Press Ctrl+C to see statistics and exit\n")

# Display initial state (show a random face)
current_roll = random.randint(1, 6)
display_dice_face(current_roll)
print(f"Initial dice face: {current_roll}")
print("\nWaiting for shake...\n")

# Main loop
try:
    while True:
        # Check for shake
        if detect_shake():
            print("🤚 Shake detected! Rolling...")

            # Show rolling animation
            rolling_animation()

            # Roll the dice (generate random number 1-6)
            result = random.randint(1, 6)

            # Display the result
            display_dice_face(result)

            # Flash green to indicate success
            time.sleep(0.3)
            sense.clear(GREEN)
            time.sleep(0.2)

            # Show result again
            display_dice_face(result)

            # Track statistics
            roll_history.append(result)
            roll_count[result] += 1

            print(f"🎲 You rolled: {result}")
            print(f"   (Total rolls: {len(roll_history)})\n")

            # Prevent multiple triggers from same shake
            time.sleep(1)

        # Small delay to avoid checking too frequently
        time.sleep(0.1)

except KeyboardInterrupt:
    # User pressed Ctrl+C
    print("\n\n" + "=" * 60)
    print("📊 DICE ROLLING STATISTICS")
    print("=" * 60)

    if len(roll_history) > 0:
        print(f"\nTotal rolls: {len(roll_history)}")
        print(f"Roll history: {roll_history}\n")

        # Show frequency of each number
        print("Frequency:")
        for number in range(1, 7):
            count = roll_count[number]
            percentage = (count / len(roll_history)) * 100
            bar = "█" * count
            print(f"  {number}: {count:2} times ({percentage:5.1f}%) {bar}")

        # Find most and least rolled
        most_rolled = max(roll_count, key=roll_count.get)
        least_rolled = min(roll_count, key=roll_count.get)

        print(f"\n🏆 Most rolled: {most_rolled} ({roll_count[most_rolled]} times)")
        print(f"🔻 Least rolled: {least_rolled} ({roll_count[least_rolled]} times)")

        # Calculate average
        average = sum(roll_history) / len(roll_history)
        print(f"📊 Average roll: {average:.2f}")

        # Expected average for fair dice is 3.5
        print(f"   (Expected average: 3.50)\n")
    else:
        print("\nNo rolls recorded - you didn't shake the Pi!\n")

    # Clean up
    sense.clear()
    print("✅ Dice program ended. LEDs cleared.\n")

"""
================================================================================
TROUBLESHOOTING & CHALLENGES
================================================================================

COMMON ISSUES:
--------------
1. Shake detection too sensitive (rolls without shaking):
   → Increase shake_threshold (try 2.0 or 2.5)
   → The Pi might be on an unstable surface

2. Shake detection not sensitive enough:
   → Decrease shake_threshold (try 1.2 or 1.0)
   → Shake more vigorously!

3. Dice patterns look wrong:
   → Check the dice_patterns dictionary
   → Make sure 8x8 grid is correct (8 rows, 8 values per row)

4. Program keeps rolling without stopping:
   → Increase the sleep time after rolling (change 1 to 2 seconds)
   → This is the "cooldown" period

5. No response when shaking:
   → Check Sense HAT connection
   → Try printing magnitude values to debug:
     print(f"Magnitude: {magnitude:.2f}")

UNDERSTANDING THE CONCEPTS:
--------------------------
1. **Accelerometer Magnitude:**
   - Measures total movement in 3D space
   - Uses Pythagorean theorem: sqrt(x² + y² + z²)
   - Normal (still) = ~1.0g (gravity)
   - Shaking = >1.5g (movement + gravity)

2. **2D Lists (Patterns):**
   - dice_patterns[1] is a list of lists
   - Outer list = rows (y-axis)
   - Inner lists = columns (x-axis)
   - Creates a grid pattern

3. **Random Numbers:**
   - random.randint(1, 6) generates 1, 2, 3, 4, 5, or 6
   - Each has equal probability (1/6 = 16.67%)
   - Over many rolls, distribution should be even

CHALLENGES FOR EARLY FINISHERS:
-------------------------------
EASY:
1. Change the dice dot color (change WHITE to a different color)
2. Change the shake sensitivity (adjust shake_threshold)
3. Add a different background color (change BLACK to dark blue)

4. Change the rolling animation:
   - Make it faster (reduce sleep time)
   - Make it longer (increase range to 20)
   - Use different colors

MEDIUM:
5. Create a "double dice" roller:
   - Split screen in half
   - Display two dice
   - Show sum of both dice

6. Add sound effects:
   - Rolling sound during animation
   - Success "ding" when result is shown
   - Research: pygame.mixer

7. Create a "lucky number" mode:
   - User sets a target number
   - Flash green if rolled number matches
   - Flash red if it doesn't
   - Count how many rolls to get lucky number

8. Add a "streak counter":
   - Track consecutive rolls of same number
   - Display current streak
   - Show longest streak at end

9. Create different dice types:
   - D4 (4-sided: 1-4)
   - D8 (8-sided: 1-8)
   - D10 (10-sided: 1-10)
   - D20 (20-sided: 1-20) - used in Dungeons & Dragons!
   - Switch between types using joystick

HARD:
10. Create "loaded dice" mode:
    - Make certain numbers more likely
    - For example: 6 appears 50% of time
    - Compare statistics to "fair" dice

11. Build a "Yahtzee scorer":
    - Roll 5 dice at once
    - Detect patterns (three of a kind, full house, etc.)
    - Calculate score

12. Create "dice battles":
    - Two players
    - Each shakes to roll
    - Highest number wins the round
    - First to 10 wins gets victory animation

13. Add "shake intensity" detection:
    - Gentle shake = D4 (small dice)
    - Medium shake = D6 (normal dice)
    - Hard shake = D20 (big dice!)

EXTENSION ACTIVITY:
-------------------
PROJECT: "Board Game Companion"
Create a full board game helper:
- Roll dice when needed
- Keep track of player turns
- Display player scores on LED matrix
- Use joystick to switch between players
- Save game state to file

MATH DISCUSSION:
---------------
Q: If you roll a dice 60 times, how many times SHOULD you get each number?
A: 60 ÷ 6 = 10 times each (in theory)

Q: Why don't you always get exactly 10 of each?
A: Randomness! Each roll is independent.

Q: What's the probability of rolling two 6s in a row?
A: (1/6) × (1/6) = 1/36 = 2.78%

DISCUSSION QUESTIONS:
--------------------
1. Is a computer random number generator truly random?
   - No! It's "pseudo-random" (follows a mathematical formula)
   - For games, it's random enough
   - For cryptography, special techniques are needed

2. How could you test if dice are "fair" (not loaded)?
   - Roll many times (hundreds or thousands)
   - Check if all numbers appear equally often
   - Statistical analysis

3. What other apps use shake detection?
   - Music apps (shake to shuffle)
   - Games (shake to reset)
   - Step counters (detect walking)
   - Fall detection (elderly care devices)

REAL-WORLD APPLICATIONS:
-----------------------
- Board game apps (digital dice)
- Casino games (RNG = Random Number Generator)
- Educational tools (learning probability)
- Gesture-controlled interfaces
- Motion-based games

================================================================================
"""
