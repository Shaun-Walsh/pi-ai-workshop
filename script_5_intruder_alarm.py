"""
================================================================================
SCRIPT 5: THE INTRUDER ALARM - Capstone Project (Headless Version)
================================================================================

TEACHER'S INTRO:
----------------
This is the CAPSTONE PROJECT - it combines everything students have learned:
✅ Script 1: LED Matrix control (flashing alarm)
✅ Script 2: Sensor reading (temperature for body heat detection)
✅ Script 3: Accelerometer (motion detection)
✅ Script 4: Camera (capturing the "intruder")

This script introduces NEW concepts:
1. Combining multiple inputs to make intelligent decisions
2. State management (armed vs triggered)
3. Creating a real working security system
4. Logging events with timestamps
5. Building a complete project from components

SCENARIO: Your Raspberry Pi is now a security system that:
- Monitors for movement (accelerometer) OR sudden temperature rise (body heat)
- When triggered: flashes red alarm LEDs and takes a photo of the "thief"
- Saves evidence with a timestamp
- Logs all events to a file

HEADLESS OPERATION:
------------------
Since we're running headless (no monitor), we:
- Cannot use camera.start_preview() - removed from this version
- Use LED matrix for all status feedback (green=armed, red=alarm, yellow=cooldown)
- Save photos to files that students can view in VS Code
- Print all status to console for monitoring via SSH

REAL-WORLD CONNECTION: This is how real alarm systems work! They combine
multiple sensors (motion, door sensors, cameras) to detect intrusions.

SETUP REQUIRED:
--------------
1. Sense HAT attached and working
2. Camera module connected and enabled
3. picamera2 installed: sudo apt install python3-picamera2
4. Place the Pi somewhere it can be "stolen" (like near a doorway)
5. Students SSH'd into the Pi via VS Code Remote

================================================================================
"""

# Import all required libraries
from sense_hat import SenseHat
from picamera2 import Picamera2  # NEW camera library
from libcamera import Transform   # For camera orientation
from datetime import datetime
import time
import os
import math

# Initialize hardware
sense = SenseHat()
camera = Picamera2()

# Configure camera
config = camera.create_still_configuration(
    main={"size": (1920, 1080)},  # Full HD resolution
    transform=Transform(hflip=0, vflip=1)  # Adjust if camera is upside down (0=no flip, 1=flip)
)
camera.configure(config)

# Start the camera (required before capturing)
camera.start()

# Setup photo storage in home directory (visible in VS Code)
home_path = os.path.expanduser("~")
alarm_folder = os.path.join(home_path, "Intruder_Alarm_Photos")
if not os.path.exists(alarm_folder):
    os.makedirs(alarm_folder)
    print(f"📁 Created folder: {alarm_folder}")

# Define colors for the alarm
RED = (255, 0, 0)      # Alarm triggered
GREEN = (0, 255, 0)    # System armed (ready)
YELLOW = (255, 255, 0) # Warning/countdown
OFF = (0, 0, 0)        # LEDs off

# ALARM SENSITIVITY SETTINGS
# Adjust these to make the alarm more or less sensitive
TEMP_THRESHOLD = 1.5       # Degrees Celsius - how much temp rise triggers alarm (LOWERED for easier triggering)
MOVEMENT_THRESHOLD = 0.3   # How much acceleration triggers alarm (LOWERED - higher = less sensitive)
ALARM_COOLDOWN = 30        # Seconds before alarm can trigger again

# DEBUG MODE - shows sensor readings in real-time
DEBUG_MODE = True  # Set to False once working properly

print("=" * 60)
print("🚨 INTRUDER ALARM SYSTEM v1.0 (Headless) 🚨")
print("=" * 60)
print("\nInitializing system...\n")

# Get baseline readings when system starts
# This is our "normal" state - we'll compare future readings to this
print("📊 Calibrating sensors (do not move the Pi)...")
baseline_temperature = sense.get_temperature()
sense.set_rotation(0)  # Ensure consistent orientation
time.sleep(2)

# Get baseline acceleration (should be close to 1g when stationary)
baseline_accel = sense.get_accelerometer_raw()

print(f"✅ Baseline temperature: {baseline_temperature:.1f}°C")
print(f"✅ Baseline calibration complete\n")

# Countdown before arming
print("🔐 ARMING SYSTEM IN...")
for countdown in range(5, 0, -1):
    sense.clear(YELLOW)
    sense.show_message(str(countdown), scroll_speed=0.05, text_colour=YELLOW, back_colour=OFF)
    print(f"   {countdown}...")

# System is now armed
sense.clear(GREEN)
print("\n✅ SYSTEM ARMED - Monitoring for intruders...")
print("   💡 Green LED = System active")
print("   🔴 Red LED = Alarm triggered")
print("   🟡 Yellow LED = Cooldown period")
print("   Press Ctrl+C to disarm\n")

# Variable to track when alarm was last triggered
last_alarm_time = 0

# Main monitoring loop
try:
    while True:
        # Read current sensor values
        current_temp = sense.get_temperature()
        current_accel = sense.get_accelerometer_raw()

        # Calculate temperature change from baseline
        temp_change = abs(current_temp - baseline_temperature)

        # Calculate movement (change in acceleration)
        # We use Pythagorean theorem to get total acceleration magnitude
        accel_x = current_accel['x']
        accel_y = current_accel['y']
        accel_z = current_accel['z']
        total_accel = math.sqrt(accel_x**2 + accel_y**2 + accel_z**2)

        # Normal gravity is about 1g - significant movement changes this
        movement_detected = abs(total_accel - 1.0)

        # Check if we're in cooldown period (prevents multiple triggers)
        time_since_last_alarm = time.time() - last_alarm_time
        in_cooldown = time_since_last_alarm < ALARM_COOLDOWN

        # INTRUSION DETECTION LOGIC
        # Trigger if: (temperature rise OR movement detected) AND not in cooldown
        temperature_trigger = temp_change > TEMP_THRESHOLD
        movement_trigger = movement_detected > MOVEMENT_THRESHOLD

        # DEBUG OUTPUT - shows what sensors are detecting
        if DEBUG_MODE:
            print(f"[DEBUG] Temp: {temp_change:.2f}°C (trigger at {TEMP_THRESHOLD}°C) | Movement: {movement_detected:.2f}g (trigger at {MOVEMENT_THRESHOLD}g)", end='\r')

        if (temperature_trigger or movement_trigger) and not in_cooldown:
            # 🚨 ALARM TRIGGERED! 🚨

            print("\n" + "!" * 60)
            print("🚨 INTRUDER DETECTED! 🚨")
            print("!" * 60)

            # Determine what triggered the alarm
            if temperature_trigger:
                print(f"⚠️  TRIGGER: Temperature spike (+{temp_change:.1f}°C)")
                trigger_type = "HEAT"
            if movement_trigger:
                print(f"⚠️  TRIGGER: Movement detected (accel: {movement_detected:.2f}g)")
                trigger_type = "MOTION"
            if temperature_trigger and movement_trigger:
                trigger_type = "HEAT+MOTION"

            # Flash red alarm LEDs
            print("🔴 Activating alarm lights...")
            for flash in range(6):  # Flash 6 times
                sense.clear(RED)
                time.sleep(0.3)
                sense.clear(OFF)
                time.sleep(0.3)

            # Keep LEDs red while taking photo
            sense.clear(RED)

            # Take photo of the intruder (NO PREVIEW in headless mode)
            print("📸 Capturing photo evidence...")

            # Give camera time to adjust exposure (important without preview)
            time.sleep(2)

            timestamp = datetime.now()
            timestamp_str = timestamp.strftime("%Y-%m-%d_%H-%M-%S")
            photo_filename = f"INTRUDER_{trigger_type}_{timestamp_str}.jpg"
            photo_path = os.path.join(alarm_folder, photo_filename)

            # Capture photo (no preview in headless mode!)
            # picamera2 uses capture_file instead of capture
            camera.capture_file(photo_path)

            print(f"✅ Evidence saved: {photo_filename}")
            print(f"📂 Location: {alarm_folder}")
            print(f"👁️  To view: Open the file in VS Code's file explorer")

            # Log the event to a text file
            log_file = os.path.join(alarm_folder, "alarm_log.txt")
            with open(log_file, 'a') as f:
                log_entry = f"{timestamp_str} | Trigger: {trigger_type} | Photo: {photo_filename}\n"
                f.write(log_entry)
            print(f"📝 Event logged to alarm_log.txt")

            # Flash success confirmation
            for flash in range(3):
                sense.clear(GREEN)
                time.sleep(0.2)
                sense.clear(OFF)
                time.sleep(0.2)

            # Update baseline temperature (in case room temp changed)
            baseline_temperature = current_temp

            # Record alarm time for cooldown
            last_alarm_time = time.time()

            print(f"\n⏳ Alarm cooldown: {ALARM_COOLDOWN} seconds")
            print("   (prevents multiple triggers from same event)")
            print("\n✅ Returning to armed state...\n")

            # Return to armed state (green LED)
            sense.clear(GREEN)

        elif in_cooldown:
            # Show we're in cooldown (yellow LED)
            sense.clear(YELLOW)
        else:
            # Normal monitoring (green LED)
            sense.clear(GREEN)

        # Small delay before next check (don't check too frequently)
        time.sleep(0.5)

except KeyboardInterrupt:
    # User pressed Ctrl+C to stop the alarm
    print("\n\n" + "=" * 60)
    print("🔓 SYSTEM DISARMED BY USER")
    print("=" * 60)

    # Cleanup
    sense.clear()
    camera.stop()
    camera.close()

    print("✅ LEDs off")
    print("✅ Camera released")
    print(f"📂 All evidence stored in: {alarm_folder}")
    print(f"📋 Check alarm_log.txt for event history")
    print("\nThank you for using Intruder Alarm System!")
    print("Stay safe! 🛡️\n")

"""
================================================================================
TROUBLESHOOTING & CHALLENGES
================================================================================

COMMON ISSUES:
--------------
1. Alarm triggers immediately when armed:
   → The calibration period might be too short
   → Increase the sleep time after getting baseline readings (try 5 seconds)
   → Make sure you're not touching/moving the Pi during calibration

2. Alarm never triggers:
   → Thresholds might be too high
   → Try lowering TEMP_THRESHOLD to 1.5 or MOVEMENT_THRESHOLD to 0.8
   → Print current values to debug:
     Add this line in the main loop:
     print(f"Debug: Temp change: {temp_change:.2f}, Movement: {movement_detected:.2f}")

3. Alarm triggers too often:
   → Increase the thresholds or the ALARM_COOLDOWN time
   → Temperature fluctuations from CPU heat can cause false alarms
   → Try: TEMP_THRESHOLD = 5.0

4. Photos are dark/blurry:
   → The 2-second delay might not be enough for the camera to adjust
   → Increase to 3-4 seconds: time.sleep(4)
   → Or set manual exposure: camera.iso = 400

5. "RuntimeError: Camera is not running":
   → Another program is using the camera
   → Reboot the Pi: sudo reboot

6. Can't find the photos in VS Code:
   → Look in your home directory → Intruder_Alarm_Photos folder
   → Refresh the file explorer in VS Code (right-click → Refresh)
   → The full path is printed in the console

7. "ModuleNotFoundError: No module named 'picamera2'":
   → Install with: sudo apt install python3-picamera2
   → (Do NOT use pip for picamera2 - use apt!)

HEADLESS-SPECIFIC TIPS:
----------------------
1. You won't see what the camera is capturing - position it BEFORE arming!
2. Test with one trigger first, check the photo, adjust camera angle
3. Make sure there's good lighting in the room
4. The LED matrix is your only visual feedback - watch it!
5. Use the console output to monitor what's happening

PICAMERA2 NOTES:
---------------
This script uses picamera2 (NEW library for Raspberry Pi OS Bookworm+):
- Works with modern libcamera system
- Better performance than old picamera
- No need to enable "Legacy Camera"
- If you have older Pi OS, ask teacher for legacy version

CHALLENGES FOR EARLY FINISHERS:
-------------------------------
EASY:
1. Change the alarm flash pattern (more/fewer flashes, different timing)
2. Change the trigger thresholds to make it more/less sensitive
3. Change the cooldown period (try 60 seconds)
4. Add a different color for each trigger type:
   - Temperature = Orange LEDs
   - Movement = Red LEDs
   - Both = Purple LEDs

MEDIUM:
5. Add a "countdown warning" before the alarm triggers:
   - When movement detected, flash yellow for 3 seconds
   - If movement continues, then trigger full alarm
   - If movement stops, return to green (armed)

6. Display a message on the LED matrix when triggered:
   sense.show_message("ALARM!", text_colour=RED, scroll_speed=0.05)

7. Create different responses for different triggers:
   - Temperature trigger: Yellow flash + photo
   - Movement trigger: Red flash + photo
   - Both: Purple flash + 2 photos

8. Add humidity detection (sudden humidity change could mean door opened):
   humidity = sense.get_humidity()
   baseline_humidity = sense.get_humidity()  # Add at startup
   humidity_change = abs(humidity - baseline_humidity)
   if humidity_change > 10:  # 10% change
       # Trigger alarm

9. Take multiple photos when triggered:
   for i in range(3):
       camera.capture_file(f"intruder_{i}.jpg")
       time.sleep(1)

10. Add camera metadata logging:
    metadata = camera.capture_metadata()
    with open(log_file, 'a') as f:
        f.write(f"   Exposure: {metadata['ExposureTime']}, Gain: {metadata['AnalogueGain']}\n")

HARD:
11. Create a "disarm code" using the joystick:
    - User must press: Up, Up, Down, Left, Right to disarm
    - Wrong combination = trigger alarm
    - Research: sense.stick.get_events()

12. Create a CSV log file with structured data:
    - Columns: Timestamp, Trigger Type, Temperature, Movement, Photo File
    - Use Python's csv module
    - Can be opened in Excel/Google Sheets for analysis

13. Add statistics to alarm_log.txt:
    - Count total triggers
    - Count heat vs motion triggers
    - Calculate average time between triggers
    - Add a summary at the end of the file

14. Create a "smart cooldown" based on trigger type:
    - Heat trigger = 60 second cooldown (slow to change)
    - Motion trigger = 15 second cooldown (quick to re-trigger)

15. Add email notifications (advanced):
    - Use Python's smtplib library
    - Send email when alarm triggers
    - Include photo as attachment
    - Include trigger type and timestamp

16. Create a web dashboard using Flask:
    - Show current alarm status (armed/triggered/cooldown)
    - Display recent photos in a gallery
    - Show alarm history from log file
    - Allow remote arming/disarming
    - Show live sensor readings

EXTENSION ACTIVITIES:
--------------------
PROJECT 1: "Multi-Zone Security System"
- Use multiple Raspberry Pis in different locations
- Each one monitors a different area
- All save to a shared network folder
- Central dashboard shows all zones

PROJECT 2: "Smart Alarm with Pattern Detection"
- Log all sensor readings (not just triggers)
- Analyze patterns: When does the alarm trigger most?
- Create graphs of temperature and movement over time
- Use matplotlib to visualize the data

PROJECT 3: "AI-Enhanced Security"
- Take multiple photos when triggered
- Use OpenCV or TensorFlow Lite to detect if it's a person
- Only save photos if a person is detected (reduce false positives)
- Research: Raspberry Pi + TensorFlow Lite

DISCUSSION QUESTIONS:
--------------------
1. What are "false positives" and why do they matter in security systems?
   (Alarm triggers when there's no real threat)

2. How could you make this alarm smarter?
   (AI face recognition, multiple sensors, pattern learning)

3. What are the privacy implications of security cameras?
   (GDPR, consent, data storage, who has access)

4. How do real security systems prevent false alarms?
   (Multiple sensors, confirmation delays, AI analysis)

5. What other sensors could you add?
   (Door sensors, IR motion detectors, sound detectors, light sensors)

6. Why is headless operation actually better for a security camera?
   (Uses less power, can be hidden, no monitor needed, runs 24/7)

ETHICAL CONSIDERATIONS:
-----------------------
⚠️ IMPORTANT: This is a learning project. If deploying a real security system:
- Clearly mark areas under surveillance (signage)
- Comply with privacy laws (GDPR in Europe, local laws)
- Don't record people without consent
- Secure your photos (encryption, access control)
- Consider data retention policies (auto-delete old photos after 30 days)
- Inform visitors they are being recorded
- Don't monitor areas where people expect privacy (bathrooms, changing rooms)

GRADING RUBRIC SUGGESTIONS FOR TEACHERS:
----------------------------------------
✅ Basic (Pass):
   - System arms successfully
   - Detects movement OR temperature
   - Takes a photo when triggered
   - Photo is saved correctly and viewable

✅ Good (Merit):
   - All basic criteria
   - Detects BOTH movement AND temperature
   - Proper cooldown prevents multiple triggers
   - Code is well-commented
   - Can explain the detection logic

✅ Excellent (Distinction):
   - All good criteria
   - Completed at least 2 challenges
   - Added unique feature not in original script
   - Can explain how the code works line-by-line
   - Professional presentation/documentation
   - Thoughtful discussion of ethical implications

PRESENTATION IDEAS:
------------------
Have students demonstrate their alarm via screen share:
1. Show the system arming (green LED on physical Pi)
2. Trigger it (move the Pi or breathe on it for heat)
3. Show the photo captured in VS Code
4. Open and explain the alarm_log.txt file
5. Explain one modification they made
6. Discuss one challenge they overcame
7. Discuss one ethical consideration

TESTING THE ALARM:
-----------------
Suggested test scenarios for students:

1. **Motion Test:**
   - Arm the system
   - Shake the Pi gently
   - Should trigger alarm and take photo

2. **Heat Test:**
   - Arm the system
   - Breathe on the Sense HAT for 10 seconds (adds warmth)
   - Should trigger alarm

3. **Cooldown Test:**
   - Trigger the alarm
   - Try to trigger it again immediately
   - Should show yellow LED (cooldown) and NOT take another photo

4. **False Positive Test:**
   - Arm the system
   - Don't touch it for 2 minutes
   - Should remain green (no false alarms)

5. **Log File Test:**
   - Trigger the alarm 3 times
   - Open alarm_log.txt
   - Should show 3 entries with timestamps and trigger types

================================================================================
"""
