"""
================================================================================
SCRIPT 4: THE BLIND PHOTOGRAPHER - Camera Module (Headless Version)
================================================================================

TEACHER'S INTRO:
----------------
This script introduces students to:
1. Controlling the camera module with code
2. Working with file paths and saving files
3. Using the Sense HAT for visual feedback (countdown)
4. Understanding timestamps
5. Creating loops for automation (time-lapse)

IMPORTANT - HEADLESS OPERATION:
-------------------------------
Since we are running HEADLESS (no monitor), we CANNOT use camera preview
like you would on a Pi with a display. Instead:
- We use the Sense HAT LED matrix to show a countdown (3, 2, 1...)
- We take the photo "blindly" (without preview)
- Students open the saved JPG file in VS Code to see the result

ANALOGY: It's like a timer on a phone camera - you set it, step back, and
trust it will capture the photo!

REAL-WORLD CONNECTION: Security cameras, trail cameras, and time-lapse cameras
all work this way - they take photos without anyone watching a preview.

SETUP REQUIRED:
--------------
1. Camera is connected to the camera port (NOT USB)
2. picamera2 is installed: sudo apt install python3-picamera2
3. Camera is detected (should work automatically with picamera2)

IMPORTANT: This script uses picamera2 (the NEW camera library for Raspberry Pi OS Bookworm+)
If you're on older Pi OS, you might need the old picamera library version.

EXPECTED OUTCOME: Countdown appears on LED matrix, photo is saved to home
directory, and students can open the JPG in VS Code to view it.

================================================================================
"""

# Import required libraries
from picamera2 import Picamera2  # NEW camera library
from libcamera import Transform   # For camera orientation
from sense_hat import SenseHat
from time import sleep
from datetime import datetime
import os

# Initialize hardware
camera = Picamera2()
sense = SenseHat()

# Get the home directory path
# In VS Code Remote SSH, students can easily see files in their home directory
home_path = os.path.expanduser("~")

# Create a "Workshop_Photos" folder in the home directory if it doesn't exist
photos_folder = os.path.join(home_path, "Workshop_Photos")
if not os.path.exists(photos_folder):
    os.makedirs(photos_folder)
    print(f"📁 Created folder: {photos_folder}")

print("=" * 60)
print("📸 THE BLIND PHOTOGRAPHER (Headless Camera)")
print("=" * 60)
print("\nCamera initializing...\n")

# Camera configuration
# picamera2 uses a configuration object instead of individual properties
config = camera.create_still_configuration(
    main={"size": (1920, 1080)},  # Full HD resolution
    transform=Transform(hflip=0, vflip=1)  # Adjust if camera is upside down (0=no flip, 1=flip)
)
camera.configure(config)

# Start the camera (required before capturing)
camera.start()

# Give the camera a moment to adjust to lighting conditions
# This is important when there's no preview - the auto-exposure needs time
print("⚙️  Camera adjusting to lighting...")
sleep(3)

# Define colors for countdown
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
OFF = (0, 0, 0)

# PART 1: TAKE A PHOTO WITH LED COUNTDOWN
# =========================================

print("📸 PHOTO MODE")
print("Watch the Sense HAT for the countdown!\n")

# Countdown on LED matrix
for count in [3, 2, 1]:
    print(f"   {count}...")

    # Show number on LED matrix
    if count == 3:
        sense.clear(RED)
    elif count == 2:
        sense.clear(YELLOW)
    elif count == 1:
        sense.clear(GREEN)

    sense.show_message(str(count), scroll_speed=0.05, text_colour=(255, 255, 255), back_colour=OFF)
    sleep(0.5)

# Flash green to indicate photo being taken
sense.clear(GREEN)
print("   📸 SNAP!")

# Create a filename with current date and time
# Example: "photo_2026-02-18_14-30-45.jpg"
current_time = datetime.now()
timestamp = current_time.strftime("%Y-%m-%d_%H-%M-%S")
photo_filename = f"photo_{timestamp}.jpg"

# Create the full path to save the photo
photo_path = os.path.join(photos_folder, photo_filename)

# Take the photo (no preview needed!)
# picamera2 uses capture_file instead of capture
camera.capture_file(photo_path)

# Clear the LED matrix
sense.clear()

print(f"\n✅ Photo saved: {photo_filename}")
print(f"📂 Location: {photos_folder}")
print(f"👁️  To view: Open the file in VS Code's file explorer\n")

# PART 2: TIME-LAPSE MODE (commented out by default)
# ===================================================
# Uncomment the code below to enable time-lapse mode!

"""
print("=" * 60)
print("⏱️  TIME-LAPSE MODE")
print("=" * 60)
print("Taking 1 photo every 10 seconds for 1 minute...")
print("(That's 6 photos total)\n")

# Time-lapse settings
interval_seconds = 10  # Time between photos
total_photos = 6       # How many photos to take

# Create a subfolder for time-lapse photos
timelapse_folder = os.path.join(photos_folder, f"timelapse_{timestamp}")
os.makedirs(timelapse_folder)
print(f"📁 Time-lapse folder: {timelapse_folder}\n")

for photo_number in range(1, total_photos + 1):
    # Show countdown on LED matrix (3, 2, 1)
    for count in [3, 2, 1]:
        sense.clear(YELLOW)
        sense.show_message(str(count), scroll_speed=0.05, text_colour=(255, 255, 255), back_colour=OFF)
        sleep(0.3)

    # Flash green when taking photo
    sense.clear(GREEN)

    # Create filename for this photo
    timelapse_filename = f"timelapse_{photo_number:03d}.jpg"
    timelapse_path = os.path.join(timelapse_folder, timelapse_filename)

    # Take the photo
    camera.capture_file(timelapse_path)
    print(f"📸 Photo {photo_number}/{total_photos} captured: {timelapse_filename}")

    # Clear LEDs
    sense.clear()

    # Wait before taking the next photo (except after the last one)
    if photo_number < total_photos:
        print(f"⏳ Waiting {interval_seconds} seconds until next photo...")
        sleep(interval_seconds)

print(f"\n✅ Time-lapse complete! {total_photos} photos saved to:")
print(f"📂 {timelapse_folder}")
print("👁️  To view: Open the folder in VS Code's file explorer\n")
"""

# Clean up - release the camera
camera.stop()
camera.close()
sense.clear()

print("=" * 60)
print("✅ CAMERA SHUT DOWN")
print("=" * 60)
print(f"All photos are in: {photos_folder}")
print("Open them in VS Code to view!\n")

"""
================================================================================
TROUBLESHOOTING & CHALLENGES
================================================================================

COMMON ISSUES:
--------------
1. "Camera not detected" or import errors:
   → Check camera is connected to camera port (NOT USB)
   → Install picamera2: sudo apt install python3-picamera2
   → Check camera detected: libcamera-hello --list-cameras
   → Should show your camera model

2. "ModuleNotFoundError: No module named 'picamera2'":
   → Install with: sudo apt install python3-picamera2
   → (Do NOT use pip for picamera2 - use apt!)

3. Photos are upside down:
   → Change transform settings in config:
     transform=Transform(hflip=1, vflip=0)
   → Try different combinations (0=no flip, 1=flip):
     - Transform(hflip=1, vflip=1) (rotate 180°)
     - Transform(hflip=1, vflip=0) (horizontal flip)
     - Transform(hflip=0, vflip=1) (vertical flip)
     - Transform() (no transformation)

4. Photos are saved but can't find them:
   → Check the Workshop_Photos folder in your home directory
   → In VS Code: Look in the file explorer on the left side
   → The script prints the full path where photos are saved

5. Photos are too dark or too bright:
   → Increase the sleep time after "Camera adjusting to lighting" (try 5 seconds)
   → The camera needs time to auto-adjust exposure without a preview
   → Or manually set exposure: camera.set_controls({"ExposureTime": 20000})

6. "RuntimeError: Camera is not running":
   → Another script might be using the camera
   → Reboot the Pi: sudo reboot

7. Can't see the countdown on Sense HAT:
   → The LEDs are flashing quickly - watch carefully!
   → Try increasing sleep times in the countdown loop
   → Check Sense HAT is properly connected

HEADLESS-SPECIFIC TIPS:
----------------------
1. Position the camera BEFORE running the script (you won't see a preview!)
2. Make sure there's good lighting in the room
3. Use the 3-second adjustment period to point the camera where you want
4. Test with one photo first, check the result, adjust camera angle if needed

PICAMERA2 vs OLD PICAMERA:
--------------------------
This script uses picamera2 (NEW library for modern Pi OS):
- Works on Raspberry Pi OS Bookworm and later
- Uses modern libcamera system
- Better performance and features
- No need to enable "Legacy Camera"

If you have OLDER Pi OS (Bullseye or earlier):
- You need the OLD picamera library
- Ask your teacher for the legacy version of this script

CHALLENGES FOR EARLY FINISHERS:
-------------------------------
EASY:
1. Change the countdown colors (make it all blue, or rainbow colors)
2. Change the resolution in the config (try 640x480 for smaller files)
3. Change the transform settings to flip the image
4. Add a longer delay (5 seconds) for better lighting adjustment

MEDIUM:
5. Uncomment the time-lapse code and run it!
6. Modify the time-lapse to take photos every 5 seconds instead of 10

7. Add camera controls (manual settings):
   # Before camera.start(), add:
   camera.set_controls({
       "Brightness": 0.2,      # -1.0 to 1.0
       "Contrast": 1.5,        # 0.0 to 2.0
       "Saturation": 1.0       # 0.0 to 2.0
   })

8. Take 3 photos in a row with different brightness:
   for brightness in [-0.3, 0.0, 0.3]:
       camera.set_controls({"Brightness": brightness})
       sleep(1)  # Let it adjust
       camera.capture_file(f"photo_brightness_{brightness}.jpg")

9. Add metadata to photos:
   # Get camera metadata after capture
   metadata = camera.capture_metadata()
   print(f"Exposure time: {metadata['ExposureTime']}")
   print(f"Gain: {metadata['AnalogueGain']}")

HARD:
10. Create a "photo booth" that takes 4 photos in quick succession:
    - Show countdown before each
    - Save them all with descriptive names
    - Create a contact sheet (grid of images)

11. Add a motion-triggered camera:
    - Import accelerometer code from Script 3
    - When Pi is moved/shaken, automatically take a photo
    - Save with timestamp

12. Create a "best exposure detector":
    - Take 5 photos with different ExposureTime values
    - Students can compare and see which works best
    - Research: Camera controls in picamera2

EXTENSION ACTIVITY:
-------------------
PROJECT: "Stop-Motion Animation"
1. Use time-lapse mode to take 30+ photos (every 3 seconds)
2. Between each photo, move an object slightly (toy car, action figure, etc.)
3. After capturing all photos, use software to combine them:
   - On Pi: sudo apt install ffmpeg
   - Run: ffmpeg -r 10 -i timelapse_%03d.jpg -vcodec libx264 animation.mp4
4. Result: Your object appears to move on its own!

DISCUSSION QUESTIONS:
--------------------
1. Why do security cameras not need previews? (They run automatically)
2. What's the advantage of NOT having a preview? (Saves power, simpler code)
3. How do trail cameras (wildlife cameras) work? (Same principle - trigger + capture)
4. What's the difference between a photo and a video?
   (Video = many photos per second, typically 24-30 fps)

REAL-WORLD PROJECT IDEAS:
-------------------------
- Time-lapse of clouds/sunset from a window
- Motion-activated security camera
- Plant growth time-lapse (1 photo per hour for a week)
- Stop-motion animation project
- Automatic pet camera (triggered by sensors)

TIPS FOR GREAT PHOTOS (Headless):
---------------------------------
1. Position your Pi BEFORE running the script
2. Ensure good lighting (natural light from window is best)
3. Keep the Pi stable (don't move it during the countdown)
4. Run once, check the result, adjust angle, run again
5. The camera "sees" a wider angle than you expect - test it!

PICAMERA2 RESOURCES:
-------------------
- Official docs: https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
- Examples: /usr/share/python3-picamera2/examples/
- Camera controls: camera.camera_controls (shows all available settings)

================================================================================
"""
