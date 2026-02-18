# Raspberry Pi Workshop - Complete Curriculum

A hands-on Python workshop for PLC students learning physical computing with Raspberry Pi, Sense HAT, and Camera Module.

---

## 📁 Repository Contents

### Workshop Scripts (Main Curriculum)
- **[script_1_hello_world.py](script_1_hello_world.py)** - LED Matrix text display
- **[script_2_environment_monitor.py](script_2_environment_monitor.py)** - Temperature, humidity, and pressure sensors
- **[script_3_digital_spirit_level.py](script_3_digital_spirit_level.py)** - Accelerometer-based tilt detector
- **[script_4_candid_camera.py](script_4_candid_camera.py)** - Camera control and time-lapse (**Headless version** - no preview)
- **[script_5_intruder_alarm.py](script_5_intruder_alarm.py)** - **Capstone project** combining all components (**Headless version**)

### Advanced Projects (Optional Extensions)
- **[Advanced/](Advanced/)** - 3 additional projects for fast finishers and extended workshops
  - **[Joystick Basics](Advanced/advanced_1_joystick_basics.py)** - Event-driven programming with joystick input
  - **[Digital Dice](Advanced/advanced_2_digital_dice.py)** - Shake to roll dice with custom LED patterns
  - **[Reaction Game](Advanced/advanced_3_reaction_game.py)** - Test your reflexes with timing and scoring

### Setup & Utility Scripts
- **[show_ip_on_boot.py](show_ip_on_boot.py)** - Displays Pi's IP address on Sense HAT at boot (essential for headless setup!)

### Documentation
- **[HEADLESS_SETUP_GUIDE.md](HEADLESS_SETUP_GUIDE.md)** - **START HERE!** Complete guide for headless operation via VS Code Remote SSH
- **[WORKSHOP_GUIDE.md](WORKSHOP_GUIDE.md)** - Complete teacher's guide (curriculum planning, troubleshooting, assessment)
- **[STUDENT_QUICK_REFERENCE.md](STUDENT_QUICK_REFERENCE.md)** - Cheat sheet for students (commands, colors, error fixes)
- **[claude.md](claude.md)** - Project context and coding standards

---

## 🎯 Learning Progression

### Main Curriculum (Required):
```
Script 1: Hello World
    ↓ (Learn: Libraries, objects, methods, RGB colors)
Script 2: Environment Monitor
    ↓ (Learn: Sensors, variables, if/else, loops)
Script 3: Digital Spirit Level
    ↓ (Learn: 3D orientation, functions, pixel control)
Script 4: Candid Camera (Headless)
    ↓ (Learn: Camera control, file handling, timestamps, LED countdowns)
Script 5: Intruder Alarm (Headless) ⭐
    ↓ (Combine ALL skills into a working security system!)
```

### Advanced Projects (Optional):
```
Advanced 1: Joystick Basics
    ↓ (Learn: Event-driven programming, joystick input)
Advanced 2: Digital Dice
    ↓ (Learn: Custom LED patterns, shake detection, randomness)
Advanced 3: Reaction Game
    ↓ (Learn: Timing, scoring, game loops)
```

**See [Advanced/README.md](Advanced/README.md) for details on extension projects.**

## 🖥️ **Headless Operation**

This workshop is designed for **headless Pis** (no monitors):
- Students connect via **VS Code Remote - SSH**
- The **Sense HAT LED matrix** provides visual feedback
- All photos are **saved as files** viewable in VS Code
- **No GUI previews** - cameras work like real security cameras!

**See [HEADLESS_SETUP_GUIDE.md](HEADLESS_SETUP_GUIDE.md) for complete setup instructions.**

---

## 🛠️ Required Hardware

- Raspberry Pi 4 or 5
- Raspberry Pi Sense HAT
- Raspberry Pi Camera Module (v2 or v3)
- Monitor, keyboard, mouse
- microSD card with Raspberry Pi OS

---

## 🚀 Quick Start

### For Teachers (Headless Setup):

1. **READ THIS FIRST:**
   - **[HEADLESS_SETUP_GUIDE.md](HEADLESS_SETUP_GUIDE.md)** - Complete setup for headless operation

2. **Set up each Raspberry Pi (needs monitor for initial setup only):**
   ```bash
   # Update system
   sudo apt update && sudo apt upgrade -y

   # Install required packages
   sudo apt install -y sense-hat python3-picamera python3-pip
   sudo pip3 install sense-hat picamera

   # Enable SSH and Legacy Camera
   sudo raspi-config
   # → Interface Options → SSH → Enable
   # → Interface Options → Legacy Camera → Enable

   # Set unique hostname
   sudo raspi-config
   # → System Options → Hostname → workshop-pi-01 (etc.)

   # Configure WiFi
   sudo raspi-config
   # → System Options → Wireless LAN
   ```

3. **Install IP display script (ESSENTIAL for headless):**
   ```bash
   # Copy show_ip_on_boot.py to /home/pi/
   # Then set it to run on boot:
   crontab -e
   # Add: @reboot python3 /home/pi/show_ip_on_boot.py &
   ```

4. **Copy workshop scripts:**
   ```bash
   mkdir -p /home/pi/Workshop_Scripts
   # Copy all script_*.py files to this folder
   ```

5. **On workshop day:**
   - Power on all Pis
   - Read IP addresses from Sense HAT displays
   - Give students IP list to connect via VS Code Remote SSH

### For Students (Via VS Code Remote SSH):

1. **Install VS Code Extension:**
   - Open VS Code
   - Install "Remote - SSH" extension by Microsoft

2. **Connect to your Pi:**
   - Press F1 → "Remote-SSH: Connect to Host"
   - Enter: `ssh pi@<IP_ADDRESS>` (get IP from teacher)
   - Password: `raspberry` (or as provided)

3. **Open Workshop Folder:**
   - Click "Open Folder"
   - Navigate to `/home/pi/Workshop_Scripts`
   - Click OK

4. **Run your first script:**
   - Open Terminal in VS Code (Ctrl+`)
   - Run: `python3 script_1_hello_world.py`
   - **Watch the physical Raspberry Pi Sense HAT!**

---

## 📊 Workshop Timeline

| Duration | Script | Difficulty |
|----------|--------|-----------|
| 30 min | Script 1: Hello World | ⭐ Beginner |
| 45 min | Script 2: Environment Monitor | ⭐⭐ Easy |
| 45 min | Script 3: Digital Spirit Level | ⭐⭐ Moderate |
| 45 min | Script 4: Candid Camera | ⭐⭐⭐ Moderate |
| 60-90 min | Script 5: Intruder Alarm | ⭐⭐⭐⭐ Advanced |

**Total:** 4-6 hours (including breaks and challenges)

---

## ✨ What Students Will Build

### Script 1: Scrolling LED Text
```python
# Students will make custom messages scroll with chosen colors
sense.show_message("Hello World!", text_colour=(0, 255, 0))
```

### Script 2: Live Environment Dashboard
```python
# Real-time sensor readings with color-coded alerts
🌡️  Temperature: 24.5°C
💧 Humidity: 45.2%
🔽 Pressure: 1013.2 mb
✅ STATUS: Comfortable!
```

### Script 3: Motion-Reactive Display
```python
# LEDs light up on the side the Pi is tilted toward
⬅️  Tilted LEFT
➡️  Tilted RIGHT
✅ LEVEL
```

### Script 4: Automated Photography
```python
# Capture photos with timestamps
📸 Photo saved: photo_2026-02-18_14-30-45.jpg
⏱️  Time-lapse: 6 photos captured
```

### Script 5: Smart Security System ⭐
```python
# Complete intruder detection with multi-sensor fusion
🚨 INTRUDER DETECTED!
⚠️  TRIGGER: Movement detected
📸 Capturing photo evidence...
✅ Evidence saved: INTRUDER_MOTION_2026-02-18_15-42-33.jpg
```

---

## 🎓 Learning Outcomes

By completing this workshop, students will be able to:

**Technical Skills:**
- Write and execute Python scripts
- Import and use external libraries
- Control hardware (LEDs, sensors, camera) programmatically
- Read and interpret sensor data
- Make decisions with conditional logic
- Create loops for repeated actions
- Handle file I/O (saving photos, logging data)
- Debug common Python and hardware errors

**Computational Thinking:**
- Break complex problems into smaller steps
- Recognize patterns in code
- Generalize solutions to new problems
- Debug systematically

**Real-World Applications:**
- Understand how IoT devices work
- See practical uses of programming
- Connect coding to multimedia concepts (RGB, pixels, frames)
- Apply knowledge to security systems, weather stations, cameras

---

## 🏆 Challenges & Extensions

Each script includes three difficulty levels of challenges:

### Easy (For Everyone)
- Change colors, text, and timing
- Modify thresholds and parameters
- Experiment with different values

### Medium (For Fast Finishers)
- Add new conditional logic
- Combine features from multiple scripts
- Display data in creative ways

### Hard (For Advanced Students)
- Build mini-games with sensors
- Create web dashboards
- Implement AI/ML features
- Design custom projects

---

## 🐛 Common Issues & Solutions

### Sense HAT Not Working
```bash
# Check connection and install library
sudo pip3 install sense-hat
i2cdetect -y 1  # Should show devices at 0x5c, 0x5f, 0x6a
```

### Camera Not Detected
```bash
# Enable legacy camera
sudo raspi-config
# → Interface Options → Legacy Camera → Enable

# Check camera status
vcgencmd get_camera
# Should show: supported=1 detected=1
```

### Temperature Readings Too High
```python
# CPU heat affects Sense HAT - apply offset
temp = sense.get_temperature() - 12  # Adjust value as needed
```

**More troubleshooting:** See WORKSHOP_GUIDE.md section "Common Technical Issues"

---

## 📚 Additional Resources

### Documentation:
- [Sense HAT API Reference](https://pythonhosted.org/sense-hat/)
- [PiCamera Documentation](https://picamera.readthedocs.io/)
- [Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/)

### Practice Online:
- [Sense HAT Emulator](https://trinket.io/sense-hat) - Test code without hardware!

### Project Ideas:
- [Raspberry Pi Projects Database](https://projects.raspberrypi.org/)

### Community:
- [Raspberry Pi Forums](https://forums.raspberrypi.com/)
- [r/raspberry_pi](https://reddit.com/r/raspberry_pi)

---

## 👥 Target Audience

**Designed for:** Irish PLC (Post Leaving Certificate) students
**Streams:** Basic IT and Multimedia
**Level:** Beginner to Low-Intermediate
**Prerequisites:** Basic computer literacy, no Python experience required

**Teaching Philosophy:**
- Visual, hands-on learning
- Immediate feedback builds confidence
- Real-world applications
- Peer collaboration encouraged
- Errors are learning opportunities

---

## 📋 Pre-Workshop Checklist

### For Teachers:

**One Week Before:**
- [ ] Test all Raspberry Pis boot successfully
- [ ] Verify Sense HATs are working (`i2cdetect -y 1`)
- [ ] Test cameras are detected (`vcgencmd get_camera`)
- [ ] Install libraries: `sudo pip3 install sense-hat picamera`
- [ ] Copy scripts to all Pis
- [ ] Print student quick reference sheets

**Day Before:**
- [ ] Test Script 1 on each Pi (quick functionality check)
- [ ] Prepare backup hardware
- [ ] Charge wireless peripherals

**Day Of:**
- [ ] Arrive early to boot all systems
- [ ] Set up demo Pi for demonstrations
- [ ] Have USB drives with scripts as backup

### For Students:

- [ ] Raspberry Pi powered on and connected to monitor
- [ ] Sense HAT firmly attached (all 40 GPIO pins)
- [ ] Camera module connected to camera port
- [ ] Scripts folder on Desktop
- [ ] Quick reference sheet accessible
- [ ] Notebook/paper for ideas and debugging

---

## 🎯 Assessment Rubric

### Pass (Basic)
- ✅ All scripts run successfully
- ✅ Can explain what the code does (in simple terms)
- ✅ Capstone project functions correctly

### Merit (Good)
- ✅ All Pass criteria
- ✅ Completed at least 2 Easy challenges
- ✅ Can troubleshoot basic errors independently
- ✅ Helps peers with debugging

### Distinction (Excellent)
- ✅ All Merit criteria
- ✅ Completed Medium or Hard challenges
- ✅ Added unique feature to capstone project
- ✅ Can explain how sensors and code interact
- ✅ Demonstrates creativity and experimentation

---

## 🌟 Success Stories

**What students say:**
> "I didn't know Python before today, but now I've built a working alarm system!"

> "The best part was seeing the LEDs react when I tilted the Pi - it felt like magic!"

> "I want to build more projects with my Raspberry Pi at home now."

**What teachers notice:**
- High engagement (students don't want to leave during breaks!)
- Peer teaching emerges naturally
- Students connect programming to real-world devices
- Confidence boost from building something tangible

---

## 📞 Support

**Questions about the curriculum?**
- Check WORKSHOP_GUIDE.md for detailed teaching notes
- Consult STUDENT_QUICK_REFERENCE.md for quick answers
- Search Raspberry Pi forums for hardware issues
- Review comments in each script for inline explanations

**Hardware issues?**
- [Official Raspberry Pi Help](https://www.raspberrypi.org/help/)
- [Sense HAT Troubleshooting](https://www.raspberrypi.org/forums/viewforum.php?f=104)

---

## 📄 License

These educational materials are provided for non-commercial educational use.

**Credits:**
- Curriculum designed for Irish PLC students (Basic IT & Multimedia)
- Created with input from educators and students
- Built on Raspberry Pi Foundation resources

---

## 🚀 Next Steps

**After the workshop:**

1. **Continue Learning:**
   - Try the extension challenges in each script
   - Browse [Raspberry Pi Projects](https://projects.raspberrypi.org/)
   - Join online communities

2. **Build Your Own Projects:**
   - Weather station with data logging
   - Motion-controlled games
   - Time-lapse nature photography
   - Smart home automation

3. **Share Your Work:**
   - Show family and friends
   - Present at school
   - Post on Reddit or Twitter
   - Enter competitions

---

## 🎉 Ready to Start?

**Teachers:** Open [WORKSHOP_GUIDE.md](WORKSHOP_GUIDE.md)
**Students:** Open [STUDENT_QUICK_REFERENCE.md](STUDENT_QUICK_REFERENCE.md)
**Everyone:** Start with [script_1_hello_world.py](script_1_hello_world.py)

---

**Let's build something amazing! 🔧💻🎨**

---

*Last Updated: February 2026*
