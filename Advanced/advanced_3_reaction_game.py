"""
================================================================================
ADVANCED 3: REACTION GAME - Test Your Reflexes!
================================================================================

TEACHER'S INTRO:
----------------
This script introduces students to:
1. Timing and measuring elapsed time
2. Combining randomness with user input
3. Game loops and scoring systems
4. User interfaces (prompts, feedback, results)
5. Performance tracking and high scores

NEW CONCEPTS:
- time.time() for measuring intervals
- Game state management (ready, waiting, go, success, fail)
- Performance metrics (best time, average time)
- User feedback design

ANALOGY: This is like a drag racing start light - wait for the green light,
then press the button as fast as you can! Your reaction time is measured
in milliseconds.

REAL-WORLD CONNECTION: Reaction time is important in sports, driving, gaming,
and many professions. This game measures how quickly you can respond to
visual stimuli.

EXPECTED OUTCOME: Students wait for a random color to appear, then press
the matching joystick direction as fast as possible. Their reaction time
is measured and displayed!

================================================================================
"""

# Import required libraries
from sense_hat import SenseHat
import time
import random

# Initialize Sense HAT
sense = SenseHat()
sense.clear()

# Define colors and their corresponding joystick directions
CHALLENGES = {
    'up': (255, 0, 0),      # Red = UP
    'down': (0, 0, 255),    # Blue = DOWN
    'left': (0, 255, 0),    # Green = LEFT
    'right': (255, 255, 0), # Yellow = RIGHT
}

# UI colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SUCCESS = (0, 255, 0)   # Green
FAILURE = (255, 0, 0)   # Red
WAITING = (128, 128, 128)  # Gray

# Game settings
ROUNDS = 5  # How many rounds to play
MIN_WAIT_TIME = 1.0  # Minimum seconds before showing color
MAX_WAIT_TIME = 4.0  # Maximum seconds before showing color

# Performance tracking
reaction_times = []
correct_responses = 0
wrong_direction_count = 0
too_early_count = 0

def display_instructions():
    """Show game instructions."""
    print("=" * 60)
    print("⚡ REACTION GAME - Test Your Reflexes!")
    print("=" * 60)
    print("\nHOW TO PLAY:")
    print("1. Watch the LED matrix")
    print("2. Wait for a color to appear (don't press yet!)")
    print("3. Press the matching joystick direction AS FAST AS YOU CAN:")
    print("   🔴 RED = UP")
    print("   🔵 BLUE = DOWN")
    print("   🟢 GREEN = LEFT")
    print("   🟡 YELLOW = RIGHT")
    print("\n🎯 Goal: React as quickly as possible!")
    print("⚠️  Warning: If you press too early, you fail that round!")
    print(f"\n📊 Game: {ROUNDS} rounds")
    print("\nGet ready...\n")

def show_ready_state():
    """Display 'ready' state - gray screen."""
    sense.clear(WAITING)
    print("⏳ Get ready... Wait for the color!")

def show_challenge(direction):
    """
    Display challenge color and return start time.

    Args:
        direction (str): The direction to challenge (up/down/left/right)

    Returns:
        float: The timestamp when challenge was shown
    """
    color = CHALLENGES[direction]
    sense.clear(color)

    # Print to console
    direction_emoji = {
        'up': '⬆️',
        'down': '⬇️',
        'left': '⬅️',
        'right': '➡️'
    }

    print(f"🎯 {direction_emoji[direction]} GO! Press {direction.upper()}!")

    # Return current time for reaction time calculation
    return time.time()

def wait_for_response():
    """
    Wait for user to press joystick.

    Returns:
        tuple: (direction pressed, timestamp of press)
    """
    # Clear any pending events
    sense.stick.get_events()

    # Wait for a press
    while True:
        events = sense.stick.get_events()
        for event in events:
            if event.action == "pressed":
                return event.direction, time.time()

        # Small delay to avoid burning CPU
        time.sleep(0.01)

def check_for_early_press():
    """
    Check if user pressed joystick too early (before color shown).

    Returns:
        bool: True if early press detected
    """
    events = sense.stick.get_events()
    for event in events:
        if event.action == "pressed":
            return True
    return False

def show_result(success, reaction_time=None, correct_direction=None, pressed_direction=None):
    """
    Display result of the round.

    Args:
        success (bool): Whether response was correct
        reaction_time (float): Time taken to respond (in seconds)
        correct_direction (str): The correct direction
        pressed_direction (str): The direction user pressed
    """
    if success:
        # Flash green for success
        sense.clear(SUCCESS)
        print(f"✅ CORRECT! Reaction time: {reaction_time*1000:.0f} ms")

        # Categorize reaction time
        if reaction_time < 0.2:
            print("   ⚡ AMAZING! Lightning fast!")
        elif reaction_time < 0.3:
            print("   🌟 EXCELLENT! Very quick!")
        elif reaction_time < 0.5:
            print("   👍 GOOD! Nice reflexes!")
        else:
            print("   😅 Not bad... but you can do better!")

    else:
        # Flash red for failure
        sense.clear(FAILURE)

        if pressed_direction:
            print(f"❌ WRONG! You pressed {pressed_direction.upper()}, needed {correct_direction.upper()}")
        else:
            print("❌ TOO EARLY! Wait for the color!")

    time.sleep(1)
    sense.clear()

# Main game
display_instructions()

# Wait for user to be ready
print("Press MIDDLE button to start...")
while True:
    event = sense.stick.wait_for_event()
    if event.action == "pressed" and event.direction == "middle":
        break

print("\n🎮 GAME STARTING!\n")
time.sleep(1)

# Play rounds
for round_num in range(1, ROUNDS + 1):
    print(f"\n{'='*60}")
    print(f"Round {round_num}/{ROUNDS}")
    print('='*60)

    # Show ready state
    show_ready_state()

    # Random wait time (prevents predictability)
    wait_time = random.uniform(MIN_WAIT_TIME, MAX_WAIT_TIME)

    # Check for early presses during wait period
    start_wait = time.time()
    early_press = False

    while time.time() - start_wait < wait_time:
        if check_for_early_press():
            early_press = True
            break
        time.sleep(0.05)

    if early_press:
        # User pressed too early!
        show_result(success=False)
        too_early_count += 1
        continue  # Skip to next round

    # Choose random direction
    correct_direction = random.choice(list(CHALLENGES.keys()))

    # Show challenge and get start time
    challenge_start_time = show_challenge(correct_direction)

    # Wait for response
    pressed_direction, press_time = wait_for_response()

    # Calculate reaction time
    reaction_time = press_time - challenge_start_time

    # Check if correct
    if pressed_direction == correct_direction:
        # Correct!
        show_result(success=True, reaction_time=reaction_time)
        reaction_times.append(reaction_time)
        correct_responses += 1
    else:
        # Wrong direction
        show_result(
            success=False,
            correct_direction=correct_direction,
            pressed_direction=pressed_direction
        )
        wrong_direction_count += 1

    # Brief pause between rounds
    time.sleep(0.5)

# Game over - show final statistics
print("\n" + "=" * 60)
print("🏁 GAME OVER - FINAL RESULTS")
print("=" * 60)

# Overall performance
print(f"\n📊 PERFORMANCE SUMMARY:")
print(f"   Correct: {correct_responses}/{ROUNDS}")
print(f"   Wrong direction: {wrong_direction_count}")
print(f"   Too early: {too_early_count}")

if correct_responses > 0:
    accuracy = (correct_responses / ROUNDS) * 100
    print(f"   Accuracy: {accuracy:.1f}%")

# Reaction time statistics
if len(reaction_times) > 0:
    print(f"\n⏱️  REACTION TIMES:")
    print(f"   Best: {min(reaction_times)*1000:.0f} ms")
    print(f"   Worst: {max(reaction_times)*1000:.0f} ms")
    print(f"   Average: {(sum(reaction_times)/len(reaction_times))*1000:.0f} ms")

    # Show all times
    print(f"\n   All times: ", end="")
    for t in reaction_times:
        print(f"{t*1000:.0f}ms ", end="")
    print()

    # Rating
    avg_time = sum(reaction_times) / len(reaction_times)
    print(f"\n🏆 RATING:")
    if avg_time < 0.25:
        print("   ⭐⭐⭐⭐⭐ ELITE REFLEXES!")
        rating = "ELITE"
    elif avg_time < 0.35:
        print("   ⭐⭐⭐⭐ EXCELLENT!")
        rating = "EXCELLENT"
    elif avg_time < 0.5:
        print("   ⭐⭐⭐ GOOD!")
        rating = "GOOD"
    elif avg_time < 0.7:
        print("   ⭐⭐ AVERAGE")
        rating = "AVERAGE"
    else:
        print("   ⭐ KEEP PRACTICING!")
        rating = "BEGINNER"

    # Display rating on LED matrix
    sense.show_message(rating, scroll_speed=0.05, text_colour=SUCCESS)

else:
    print("\n😢 No successful reactions recorded!")
    print("   Try again and wait for the color before pressing!")

# Clean up
sense.clear()
print("\n✅ Game ended. Thanks for playing!\n")

"""
================================================================================
TROUBLESHOOTING & CHALLENGES
================================================================================

COMMON ISSUES:
--------------
1. "Too early" messages all the time:
   → You're pressing before the color appears
   → Wait until you SEE the color!
   → The gray screen means "not yet"

2. Always wrong direction:
   → Make sure you know which color matches which direction:
     RED = UP, BLUE = DOWN, GREEN = LEFT, YELLOW = RIGHT
   → Practice without time pressure first

3. Reaction times seem impossible (negative or huge):
   → This shouldn't happen, but if it does:
   → Check system clock: date
   → Restart the program

4. Joystick not responding:
   → Make sure Sense HAT is properly connected
   → Try different joystick direction

UNDERSTANDING REACTION TIME:
---------------------------
Human reaction time facts:
- Average: 200-300 milliseconds (0.2-0.3 seconds)
- Fastest human: ~150 ms (elite athletes)
- Factors that affect it:
  * Age (younger = usually faster)
  * Practice (improves with training)
  * Fatigue (tired = slower)
  * Distraction (focus matters!)

CHALLENGES FOR EARLY FINISHERS:
-------------------------------
EASY:
1. Change the number of rounds (try 10 rounds)
2. Change the colors used
3. Make wait time shorter or longer

4. Add more directions (include 'middle' button)

MEDIUM:
5. Create a "practice mode":
   - Unlimited rounds
   - Show current average after each round
   - Keep going until user presses Ctrl+C

6. Add difficulty levels:
   - Easy: Long wait times, only 2 colors
   - Medium: Current settings
   - Hard: Short wait times, all 5 directions

7. Create a "high score" system:
   - Save best average time to a file
   - Load and display on start
   - Show "NEW RECORD!" message

8. Add visual countdown:
   - Show "3... 2... 1..." before each round
   - Use different colors for countdown

9. Create a "multiplayer mode":
   - Two players take turns
   - Compare their best times
   - Declare winner

HARD:
10. Build a "training mode":
    - Track improvement over time
    - Plot reaction times on a graph
    - Show trend (getting faster/slower)

11. Add "combos":
    - Multiple colors in sequence
    - Must press all correctly in order
    - Time from first to last press

12. Create "distraction mode":
    - Show wrong colors briefly
    - Add random LED flashes
    - Make it harder to focus

13. Build "tournament mode":
    - Multiple players
    - Bracket system
    - Grand champion declared

14. Add machine learning:
    - Predict when user will press early
    - Adjust wait times based on user patterns
    - Provide personalized feedback

EXTENSION ACTIVITY:
-------------------
PROJECT: "Sports Training Assistant"
Create a comprehensive training tool:
- Different drills (speed, accuracy, endurance)
- Progress tracking over days/weeks
- Personalized difficulty adjustment
- Export data to spreadsheet for analysis

SCIENCE EXPERIMENT:
------------------
Test these hypotheses:
1. Do you get faster with practice?
   - Play 5 games, compare first vs last
2. Does caffeine improve reaction time?
   - Test before and after coffee (if allowed!)
3. Does time of day matter?
   - Test morning vs afternoon vs evening

DISCUSSION QUESTIONS:
--------------------
1. Why do sports players need fast reaction times?
   - Tennis, boxing, racing, gaming all require quick responses

2. Can you improve reaction time with practice?
   - Yes! Brain forms faster neural pathways

3. What jobs require fast reaction times?
   - Pilots, drivers, surgeons, athletes, gamers

4. What's the difference between reaction time and reflexes?
   - Reaction: conscious response to stimulus
   - Reflex: automatic response (like pulling hand from hot stove)

5. How does this game test reaction time fairly?
   - Random wait times (prevents prediction)
   - Consistent challenge format
   - Objective measurement (milliseconds)

REAL-WORLD APPLICATIONS:
-----------------------
- Driver training (brake reaction time)
- Sports performance testing
- Cognitive assessment (medical/psychological)
- Gaming skill measurement
- Pilot selection tests

PROGRAMMING CONCEPTS LEARNED:
----------------------------
✅ Timing and performance measurement
✅ Random number generation for unpredictability
✅ State machines (ready, waiting, go, result)
✅ User interface design (clear feedback)
✅ Data collection and statistical analysis
✅ Game loop architecture

================================================================================
"""
