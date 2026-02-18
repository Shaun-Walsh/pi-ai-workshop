# Student Quick Reference Guide
## Raspberry Pi Workshop - Cheat Sheet

---

## 🚀 Running Your Scripts

```bash
# Navigate to your scripts folder
cd ~/Desktop/Workshop_Scripts

# Run a Python script
python3 script_1_hello_world.py

# Stop a running script
Press Ctrl+C on your keyboard
```

---

## 🎨 RGB Color Reference

Use these values in your code: `(Red, Green, Blue)`

Each value goes from **0** (off) to **255** (brightest)

| Color | RGB Value |
|-------|-----------|
| **Red** | `(255, 0, 0)` |
| **Green** | `(0, 255, 0)` |
| **Blue** | `(0, 0, 255)` |
| **Yellow** | `(255, 255, 0)` |
| **Cyan** | `(0, 255, 255)` |
| **Magenta** | `(255, 0, 255)` |
| **White** | `(255, 255, 255)` |
| **Black (Off)** | `(0, 0, 0)` |
| **Orange** | `(255, 165, 0)` |
| **Purple** | `(128, 0, 128)` |
| **Pink** | `(255, 192, 203)` |

**Make your own:** Mix red, green, and blue like paint!

---

## 📚 Common Sense HAT Commands

```python
from sense_hat import SenseHat
sense = SenseHat()

# Display text
sense.show_message("Hello!", text_colour=(255,0,0))

# Clear the display
sense.clear()

# Set all LEDs to one color
sense.clear((0, 255, 0))  # All green

# Set one pixel (x, y, color)
sense.set_pixel(0, 0, (255, 0, 0))  # Top-left pixel red

# Read temperature (Celsius)
temp = sense.get_temperature()

# Read humidity (percentage)
humidity = sense.get_humidity()

# Read pressure (millibars)
pressure = sense.get_pressure()

# Read orientation
orientation = sense.get_orientation()
pitch = orientation['pitch']
roll = orientation['roll']

# Read raw accelerometer
accel = sense.get_accelerometer_raw()
x = accel['x']
y = accel['y']
z = accel['z']
```

---

## 📸 Camera Commands

```python
from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Set resolution
camera.resolution = (1920, 1080)

# Rotate image if upside down
camera.rotation = 180  # or 0, 90, 270

# Show preview
camera.start_preview()
sleep(2)  # Wait 2 seconds
camera.stop_preview()

# Take a photo
camera.capture('/home/pi/Desktop/photo.jpg')

# Close camera when done
camera.close()
```

---

## 🐛 Common Errors & Fixes

### Error: `ModuleNotFoundError: No module named 'sense_hat'`
**Fix:**
```bash
sudo pip3 install sense-hat
```

### Error: `PiCamera is not enabled`
**Fix:**
```bash
sudo raspi-config
# Go to: Interface Options → Legacy Camera → Enable
# Then reboot: sudo reboot
```

### Error: `IndentationError: unexpected indent`
**Fix:** Python cares about spaces! Make sure your indentation is consistent.
- Use 4 spaces for each indent level
- Don't mix tabs and spaces

### Error: Script runs but nothing happens
**Fix:**
- Check Sense HAT is properly attached (all 40 pins connected)
- Try running with sudo: `sudo python3 script_name.py`
- Reboot the Pi: `sudo reboot`

### Sense HAT shows wrong colors
**Fix:**
- Check RGB order: Red, Green, Blue (not BGR!)
- Each value must be 0-255 (not 256+)

### Temperature is too high (50°C+)
**Fix:** This is normal! The Sense HAT sits on the Pi's CPU which is hot.
For more accurate readings, subtract 10-15 degrees:
```python
temp = sense.get_temperature() - 12
```

---

## ⌨️ Keyboard Shortcuts

| Shortcut | What it does |
|----------|--------------|
| **Ctrl+C** | Stop a running program |
| **Ctrl+S** | Save file |
| **Ctrl+Z** | Undo |
| **Ctrl+Shift+T** | Open new terminal |
| **Tab** | Auto-complete in terminal |

---

## 💡 Coding Tips

### 1. Start Small
Don't write the whole program at once. Write 2-3 lines, test it, then add more.

### 2. Read Error Messages
They're trying to help! They tell you:
- What went wrong
- What line it happened on

### 3. Print Everything
When debugging, use `print()` to see what's happening:
```python
print(f"Temperature is: {temp}")
print(f"X value: {x}, Y value: {y}")
```

### 4. Comment Your Code
Leave notes for yourself:
```python
# This sets the LED matrix to red
sense.clear((255, 0, 0))
```

### 5. Ask for Help!
- Check with your neighbor first
- Google the error message
- Ask your teacher

---

## 🎯 Challenge Ladder

### Easy Challenges:
- Change colors
- Change text messages
- Change sensor thresholds
- Adjust timing/speeds

### Medium Challenges:
- Add if/else logic
- Display sensor values on LEDs
- Take multiple photos in sequence
- Combine two scripts together

### Hard Challenges:
- Create custom animations
- Build mini-games with joystick
- Add new features to the alarm
- Create a web dashboard

---

## 🔍 Troubleshooting Checklist

When something doesn't work:

- [ ] Did I save the file? (Ctrl+S)
- [ ] Did I spell everything correctly? (check variable names)
- [ ] Are my parentheses `()` and brackets `[]` matched?
- [ ] Is my indentation correct? (4 spaces)
- [ ] Is the Sense HAT properly attached?
- [ ] Did I import the libraries at the top?
- [ ] Did I create the objects (`sense = SenseHat()`)?

---

## 📝 Script Summary

| Script | What It Does | Main Concept |
|--------|-------------|--------------|
| **Script 1** | Scrolling text on LEDs | Basic output |
| **Script 2** | Read temperature/humidity | Sensor input |
| **Script 3** | Tilt detector | Motion sensing |
| **Script 4** | Take photos | Camera control |
| **Script 5** | Security alarm | Combining everything |

---

## 🏆 Workshop Goals

By the end of today, you should be able to:
- ✅ Run a Python script
- ✅ Control LEDs with code
- ✅ Read sensor data
- ✅ Take photos with code
- ✅ Explain what your code does
- ✅ Debug simple errors
- ✅ Build a working security system!

---

## 📚 Want to Learn More?

### Free Resources:
- **Raspberry Pi Projects:** https://projects.raspberrypi.org/
- **Sense HAT Emulator:** https://trinket.io/sense-hat (test code online!)
- **Python for Beginners:** https://www.python.org/about/gettingstarted/

### YouTube Channels:
- Raspberry Pi Foundation
- The Coding Train
- Programming with Mosh (Python tutorials)

### What's Next?
- Build a weather station
- Create a reaction game
- Make music with code
- Control robots with sensors

---

## 🎓 Remember:

> **"Every expert was once a beginner. Every pro was once an amateur. Keep coding!"**

---

**Good luck! Have fun! Break things (safely)! 🚀**
