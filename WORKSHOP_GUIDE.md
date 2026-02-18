# Raspberry Pi Workshop Curriculum
## For PLC Students - Basic IT & Multimedia Streams

---

## 📋 Workshop Overview

This hands-on workshop introduces students to physical computing using the Raspberry Pi, Sense HAT, and Camera Module. Students will progress from simple LED displays to building a complete security system.

**Duration:** 4-6 hours (can be split across multiple sessions)
**Skill Level:** Beginner to Low-Intermediate
**Prerequisites:** Basic computer literacy, no Python experience required

---

## 🎯 Learning Objectives

By the end of this workshop, students will be able to:
- Write and run Python scripts on the Raspberry Pi
- Control LEDs and displays programmatically
- Read data from physical sensors
- Work with motion/orientation sensors
- Capture photos using the camera module
- Combine multiple components into a working project
- Debug and troubleshoot hardware/software issues

---

## 🛠️ Required Hardware

### Per Student/Pair:
- ✅ Raspberry Pi 4 or 5
- ✅ Raspberry Pi Sense HAT (attached via GPIO)
- ✅ Raspberry Pi Camera Module v2 or v3
- ✅ Monitor, keyboard, mouse
- ✅ Power supply
- ✅ microSD card with Raspberry Pi OS installed

### Classroom Setup:
- Stable internet connection (for troubleshooting documentation)
- File sharing method (USB drives or network folder)
- Extra hardware (backup Pis, Sense HATs, cameras)

---

## 📚 Workshop Structure

### Session Timeline (Suggested)

| Time | Activity | Script |
|------|----------|--------|
| **0:00-0:15** | Introduction & Setup Check | - |
| **0:15-0:45** | Hello World - LED Matrix | Script 1 |
| **0:45-1:30** | Environment Monitor | Script 2 |
| **1:30-1:40** | *Break* | - |
| **1:40-2:25** | Digital Spirit Level | Script 3 |
| **2:25-3:10** | Candid Camera | Script 4 |
| **3:10-3:20** | *Break* | - |
| **3:20-4:30** | Intruder Alarm (Capstone) | Script 5 |
| **4:30-4:45** | Presentations & Wrap-up | - |

*Note: Timing is flexible. Advanced students can move faster; others may need more time.*

---

## 📝 Script Progression

### Script 1: Hello World (LED Matrix)
**File:** `script_1_hello_world.py`

**Concepts Learned:**
- Importing libraries
- Creating objects
- RGB color values
- Method calls with parameters

**Expected Outcome:** Text scrolls across the Sense HAT display

**Teaching Tips:**
- Start with this! Immediate visual feedback builds confidence
- Have students experiment with colors before moving on
- Reference their multimedia knowledge (RGB in Photoshop, etc.)

---

### Script 2: Environment Monitor (Sensors)
**File:** `script_2_environment_monitor.py`

**Concepts Learned:**
- Reading sensor data
- Working with variables (floats)
- If/elif/else statements
- While loops
- String formatting

**Expected Outcome:** Live temperature, humidity, pressure readings with color-coded LED feedback

**Teaching Tips:**
- Explain sensor inaccuracy (CPU heat) as a real-world limitation
- Have students breathe on the sensor to see temperature change
- Discuss real-world applications (thermostats, weather stations)

**Common Student Question:** *"Why is the temperature so high?"*
**Answer:** The Sense HAT sits on top of the Pi's CPU, which generates heat. Real installations use separate sensors or apply calibration offsets.

---

### Script 3: Digital Spirit Level (IMU/Accelerometer)
**File:** `script_3_digital_spirit_level.py`

**Concepts Learned:**
- 3D coordinate systems (X, Y, Z)
- Accelerometer data
- Functions (defining and calling)
- Individual pixel control
- Threshold-based decision making

**Expected Outcome:** LEDs light up on the side the Pi is tilted toward

**Teaching Tips:**
- Pass around an actual spirit level if available
- Demonstrate smartphone screen rotation as a familiar example
- Let students experiment with different tilt thresholds

**Common Student Challenge:** Understanding pitch vs roll
**Solution:** Use physical gestures - "nodding yes" (pitch) vs "shaking no" (roll)

---

### Script 4: Candid Camera (Camera Module)
**File:** `script_4_candid_camera.py`

**Concepts Learned:**
- Camera control
- File paths and directories
- Timestamps with datetime
- Saving files programmatically
- Optional: Loops for automation

**Expected Outcome:** Camera preview displays, photo saved to Desktop

**Teaching Tips:**
- **IMPORTANT:** Verify camera setup BEFORE this session (save troubleshooting time)
- Have students take selfies or photos of partners
- Show how time-lapse works by enabling that code section

**Pre-Session Checklist:**
```bash
# Test camera on each Pi:
vcgencmd get_camera
# Should show: supported=1 detected=1

# Enable legacy camera if needed:
sudo raspi-config
# Interface Options → Legacy Camera → Enable
```

**Common Issue:** Camera not detected
**Quick Fix:** Check ribbon cable connection (blue strip faces away from USB ports)

---

### Script 5: The Intruder Alarm (Capstone Project)
**File:** `script_5_intruder_alarm.py`

**Concepts Learned:**
- Integration of multiple systems
- Baseline calibration
- State management (armed/triggered/cooldown)
- Mathematical calculations (Pythagorean theorem)
- File logging
- Real-world application design

**Expected Outcome:** Functional security system that detects intrusion and captures photos

**Teaching Tips:**
- Frame this as "your first real project"
- Have students test each other's alarms
- Encourage creativity in modifications
- Allow time for presentations/demos

**Suggested Classroom Activity: "Thief Challenge"**
1. Pair up students
2. One student arms their alarm and leaves the desk
3. Partner tries to "steal" something without triggering the alarm
4. Review the captured photos and discuss false positives/negatives

---

## 🎓 Differentiation Strategies

### For Struggling Students:
- Pair with a stronger student (peer teaching)
- Focus on getting each script running first, skip challenges
- Provide pre-filled templates with TODOs
- Extra 1-on-1 time during breaks

### For Advanced Students:
- Complete challenges from each script
- Combine scripts in creative ways (e.g., camera triggers on temperature change)
- Research additional Sense HAT features (compass, gyroscope)
- Help teach peers (leadership opportunity)

### For Visual Learners:
- Draw diagrams of sensor placement
- Create flowcharts of program logic
- Use color-coding in code comments

### For Kinesthetic Learners:
- Hands-on hardware manipulation (tilting, moving the Pi)
- Physical demonstrations (being the "intruder")
- Building custom cases/mounts for the Pi

---

## ⚠️ Common Technical Issues & Solutions

### Issue 1: Sense HAT Not Detected
**Symptoms:** `ImportError: No module named sense_hat`

**Solutions:**
```bash
# Install sense-hat library
sudo pip3 install sense-hat

# Verify GPIO connection (Sense HAT should be firmly seated)
# Check with:
i2cdetect -y 1
# Should show devices at addresses 0x5c, 0x5f, 0x6a
```

### Issue 2: Camera Not Working
**Symptoms:** `PiCamera is not enabled` or `Camera not detected`

**Solutions:**
```bash
# Enable legacy camera
sudo raspi-config
# → Interface Options → Legacy Camera → Enable → Reboot

# Check camera detection
vcgencmd get_camera
# Should show: supported=1 detected=1

# Check ribbon cable connection (blue strip faces away from USB ports)
```

### Issue 3: Script Runs But Nothing Happens on LED Matrix
**Symptoms:** Script completes but LEDs stay off

**Solutions:**
- Check Sense HAT is firmly connected to all 40 GPIO pins
- Try running with sudo: `sudo python3 script_name.py`
- Reboot the Pi: `sudo reboot`

### Issue 4: Permissions Error When Saving Files
**Symptoms:** `PermissionError: [Errno 13] Permission denied`

**Solutions:**
- Don't run in `/root` directory - run in `/home/pi` or `/home/student`
- Check folder permissions: `ls -la ~/Desktop`
- Create folder manually first: `mkdir ~/Desktop/Workshop_Photos`

### Issue 5: Temperature/Sensor Readings Seem Wrong
**Symptoms:** Temperature shows 50°C+ or humidity is 0%

**Solutions:**
- This is normal! CPU heat affects readings
- Apply calibration offset: `temp = sense.get_temperature() - 12`
- For more accurate readings, use external sensors

---

## 📊 Assessment Ideas

### Formative Assessment (During Workshop):
- ✅ Observation: Are students engaging with challenges?
- ✅ Questioning: Can they explain what their code does?
- ✅ Peer teaching: Can they help classmates troubleshoot?

### Summative Assessment (End of Workshop):
Choose one or combine several:

#### Option 1: Demonstration (Practical)
Student demonstrates their capstone project and explains:
- How it works
- What sensors it uses
- One problem they solved
- One thing they modified

**Rubric:**
- **Pass:** Project runs and performs basic function
- **Merit:** Project runs reliably + explained clearly
- **Distinction:** Project includes modifications + professional presentation

#### Option 2: Written Reflection (Theory)
Students answer:
1. What are the three sensors on the Sense HAT and what do they measure?
2. Explain how RGB colors work (with examples)
3. Describe one problem you encountered and how you solved it
4. What real-world device could you build with these skills?

#### Option 3: Extension Project (Advanced)
Students create something new using the skills learned:
- Custom security system feature
- Interactive game using sensors
- Art project (LED animations based on sensor data)
- Time-lapse video project

---

## 🎨 Extension Projects & Ideas

### For Next Sessions:

1. **Weather Station Dashboard**
   - Log sensor data every 5 minutes
   - Create graphs with matplotlib
   - Build a web interface to view data

2. **Reaction Time Game**
   - Flash LEDs in random pattern
   - Student must replicate with joystick
   - Display high scores

3. **Plant Monitor**
   - Monitor humidity and temperature
   - Take time-lapse of plant growth
   - Alert if conditions are bad for plant

4. **Motion-Controlled Music Player**
   - Tilt left/right to skip tracks
   - Shake to shuffle
   - Uses pygame for audio

5. **Step Counter (Pedometer)**
   - Use accelerometer to detect steps
   - Display count on LED matrix
   - Challenge: Calculate calories burned

---

## 🔗 Additional Resources

### Official Documentation:
- [Sense HAT API Reference](https://pythonhosted.org/sense-hat/)
- [PiCamera Documentation](https://picamera.readthedocs.io/)
- [Raspberry Pi Getting Started](https://www.raspberrypi.org/help/)

### Free Learning Resources:
- [Raspberry Pi Projects](https://projects.raspberrypi.org/) - 1000+ tutorials
- [Sense HAT Emulator](https://trinket.io/sense-hat) - Test code without hardware
- [Python for Beginners](https://www.python.org/about/gettingstarted/)

### Video Tutorials:
- Search YouTube: "Raspberry Pi Sense HAT tutorial"
- Search YouTube: "Raspberry Pi camera projects"

### Community:
- [Raspberry Pi Forums](https://forums.raspberrypi.com/)
- [r/raspberry_pi on Reddit](https://reddit.com/r/raspberry_pi)

---

## 👨‍🏫 Teacher Preparation Checklist

### One Week Before:
- [ ] Test all Raspberry Pis boot successfully
- [ ] Verify all Sense HATs are attached and working
- [ ] Test all cameras are detected
- [ ] Update all Pis: `sudo apt update && sudo apt upgrade`
- [ ] Install required libraries on all Pis
- [ ] Create student accounts if needed
- [ ] Print handouts (script summaries, RGB color chart)

### Day Before:
- [ ] Copy all 5 scripts to each Pi's Desktop
- [ ] Test run Script 1 on each Pi (quick check)
- [ ] Prepare backup hardware (spare Pi, Sense HAT, camera)
- [ ] Charge any wireless keyboards/mice
- [ ] Prepare troubleshooting cheat sheet

### Day Of:
- [ ] Arrive early to set up
- [ ] Boot all Pis and check displays
- [ ] Have backup USB drives with scripts ready
- [ ] Prepare camera test photos location
- [ ] Set up example working system for demonstration

### Sample Installation Script:
Save this to install all dependencies on each Pi:

```bash
#!/bin/bash
# Run on each Raspberry Pi before workshop

echo "Installing workshop dependencies..."
sudo apt update
sudo apt install -y sense-hat python3-picamera python3-pip

# Install Python libraries
sudo pip3 install sense-hat picamera

# Enable legacy camera
echo "Remember to enable Legacy Camera in raspi-config!"

# Create workshop folders
mkdir -p ~/Desktop/Workshop_Scripts
mkdir -p ~/Desktop/Workshop_Photos

echo "Setup complete! Test with: python3 -c 'from sense_hat import SenseHat'"
```

---

## 💡 Teaching Tips & Pedagogical Notes

### Start With Success:
- Begin with Script 1 - it's quick and impressive
- Celebrate first successful run (builds confidence)
- Immediate visual feedback is motivating

### Embrace Failure:
- Errors are learning opportunities
- Have students read error messages out loud
- Encourage peer troubleshooting before asking teacher

### Encourage Experimentation:
- "What happens if you change this number?"
- "Can you make it do X instead of Y?"
- Allow time for free exploration

### Connect to Real World:
- Show smartphone accelerometer demos
- Discuss security cameras in shops
- Reference multimedia tech they know (RGB, pixels, frames)

### Vocabulary Matters:
Use consistent terminology:
- "Library" not "module" initially
- "Method" not "function" for object methods
- "RGB value" not "tuple" at first

### Gradual Release of Responsibility:
1. **Script 1-2:** Teacher demonstrates, students follow
2. **Script 3:** Students try first, teacher helps
3. **Script 4-5:** Students work independently, teacher facilitates

---

## 🎤 Sample Workshop Introduction Script

*Use this or adapt it for your teaching style:*

---

**"Good morning/afternoon everyone! Today we're going to be hackers... legal hackers!**

You've all got a Raspberry Pi in front of you. This tiny computer costs about €50, but it can do almost everything a regular computer can do. More importantly, it can control the real world around it - lights, cameras, sensors, motors - all with code that YOU write.

By the end of today, you'll have built your own security system. It'll detect when someone tries to steal your Pi, flash red alarm lights, and take their photo automatically. Just like a real burglar alarm!

But we'll start simple. First, we'll just make some text scroll across this little LED screen [hold up Sense HAT]. Then we'll read temperature like a weather station. Then we'll make it detect when we tilt it. Then we'll use the camera. Finally, we'll combine everything.

Here's the deal: coding is like learning to ride a bike. You WILL fall off. Your code WILL have errors. That's completely normal and expected. When it happens - and it will - don't panic. Read the error message, check your code, ask your neighbor, ask me.

Most importantly: experiment! Change things! Break things! See what happens! The worst that happens is you need to reload the file, and I've got backups.

Right, let's get started. Everyone open the file called `script_1_hello_world.py`..."

---

## 📅 Workshop Variations

### Half-Day Workshop (3 hours):
- Script 1 (quick intro)
- Script 2 (sensors)
- Script 5 (capstone only - skip 3 & 4)

### Full-Day Workshop (6 hours):
- All 5 scripts with extended challenges
- Lunch break for presentations
- Group project: Combine 2+ Pis into a network

### Multi-Week Course (5 weeks):
- Week 1: Scripts 1-2
- Week 2: Scripts 3-4
- Week 3: Script 5
- Week 4: Extensions & projects
- Week 5: Presentations & assessment

---

## 🏆 Success Criteria

### You'll know the workshop is successful when:
- ✅ Students are excited and engaged
- ✅ At least 80% complete the capstone project
- ✅ Students can explain (in simple terms) what their code does
- ✅ Students help each other troubleshoot
- ✅ Students ask "Can we do [creative idea]?"
- ✅ Students want to continue learning after the workshop

---

## 📧 Support & Feedback

**For this curriculum:**
- Created specifically for Irish PLC students (Basic IT & Multimedia)
- Tested with beginner programmers
- Emphasizes visual, hands-on learning

**Questions or suggestions?**
Feel free to modify these scripts for your specific needs!

---

## 📜 License & Attribution

These workshop materials are provided for educational use.

**Acknowledgments:**
- Raspberry Pi Foundation for hardware and documentation
- Python Software Foundation
- The open-source community

---

**Good luck with your workshop! Your students are going to build amazing things! 🚀**

---

*Last updated: February 2026*
