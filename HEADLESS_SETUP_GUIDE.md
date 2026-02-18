# Headless Raspberry Pi Workshop Setup Guide

**For teachers running the workshop with SSH access via VS Code Remote**

---

## 🎯 Overview

This workshop is designed for **headless operation** where:
- Raspberry Pis have **no monitors** in the workshop room
- Students connect via **VS Code Remote - SSH** from their laptops
- The **Sense HAT LED matrix** provides visual feedback
- Pis are connected to **corporate WiFi**
- All visual output (photos) is **saved to files** viewable in VS Code

---

## 📋 Pre-Workshop Setup Checklist

### Week Before Workshop:

#### 1. Hardware Preparation
- [ ] Test all Raspberry Pis boot successfully
- [ ] Attach Sense HATs to all Pis (all 40 GPIO pins connected)
- [ ] Connect Camera Modules to all Pis (ribbon cable in camera port)
- [ ] Label each Pi (e.g., "Workshop-Pi-01", "Workshop-Pi-02", etc.)

#### 2. Software Configuration (Per Pi)

**You'll need a monitor, keyboard, and mouse for initial setup only**

```bash
# Update the system
sudo apt update
sudo apt upgrade -y

# Install required libraries
sudo apt install -y sense-hat python3-picamera python3-pip

# Install Python packages
sudo pip3 install sense-hat picamera

# Enable SSH
sudo raspi-config
# → Interface Options → SSH → Enable

# Enable Legacy Camera
sudo raspi-config
# → Interface Options → Legacy Camera → Enable

# Set unique hostname (important for identification)
sudo raspi-config
# → System Options → Hostname → workshop-pi-01
# (Use workshop-pi-01, workshop-pi-02, etc.)

# Reboot
sudo reboot
```

#### 3. WiFi Configuration

**CRITICAL: This must be done beforehand**

Connect each Pi to your corporate WiFi:

```bash
sudo raspi-config
# → System Options → Wireless LAN
# Enter SSID and password
```

**Corporate Network Considerations:**
- Some corporate networks require web portal login (captive portal) - won't work with headless Pi
- You may need to provide IT with the MAC addresses of all Pis for whitelisting
- Check with IT beforehand to ensure devices can connect

To get MAC address for IT:
```bash
ifconfig wlan0 | grep ether
```

#### 4. Set Up IP Address Display (ESSENTIAL for headless!)

**This is the key to making headless work - the Pi will tell you its IP address!**

On each Pi:

```bash
# Copy the IP display script to home directory
# (You can use SCP, USB drive, or create it with nano)
nano /home/pi/show_ip_on_boot.py
# (Paste the contents from show_ip_on_boot.py file)

# Make it run on boot
crontab -e
# Select nano editor if asked
# Add this line to the bottom:
@reboot python3 /home/pi/show_ip_on_boot.py &

# Save and exit (Ctrl+X, Y, Enter)

# Reboot to test
sudo reboot
```

**After reboot:** The Sense HAT should scroll `IP: 192.168.x.x` in green!

If you see "No WiFi" in red, the Pi isn't connected to the network.

#### 5. Copy Workshop Scripts

On each Pi, create the workshop directory and copy all scripts:

```bash
# Create workshop directory in home
mkdir -p /home/pi/Workshop_Scripts

# Copy all scripts (via SCP, USB, or git clone)
# Scripts go in: /home/pi/Workshop_Scripts/

# The scripts should be:
# - script_1_hello_world.py
# - script_2_environment_monitor.py
# - script_3_digital_spirit_level.py
# - script_4_candid_camera.py
# - script_5_intruder_alarm.py
```

**Quick copy method using SCP from your computer:**
```bash
# From your laptop (replace IP_ADDRESS with actual Pi IP)
scp script_*.py pi@IP_ADDRESS:/home/pi/Workshop_Scripts/
```

#### 6. Test Each Pi

Before the workshop, test each Pi:

```bash
# SSH into the Pi
ssh pi@192.168.x.x

# Navigate to scripts folder
cd ~/Workshop_Scripts

# Test script 1 (LED matrix)
python3 script_1_hello_world.py

# Verify:
# - Sense HAT displays scrolling text
# - No errors in console

# Test script 4 (camera)
python3 script_4_candid_camera.py

# Verify:
# - Countdown appears on Sense HAT
# - Photo is saved to ~/Workshop_Photos/
# - Photo can be viewed: ls ~/Workshop_Photos/
```

---

## 📅 Workshop Day Setup

### 1. Physical Setup (30 mins before students arrive)

1. **Arrange the Pis:**
   - Place Pis on desks/tables
   - Ensure Sense HAT is visible to students
   - Camera should face outward (students can adjust angle later)
   - Connect power supplies

2. **Boot and record IPs:**
   - Power on all Pis
   - Wait 60 seconds for them to boot and connect to WiFi
   - Read IP address from each Sense HAT LED matrix
   - Create a list:

   ```
   Pi Name         | IP Address      | Desk/Location
   ----------------|-----------------|---------------
   workshop-pi-01  | 192.168.1.45    | Desk 1
   workshop-pi-02  | 192.168.1.46    | Desk 2
   workshop-pi-03  | 192.168.1.47    | Desk 3
   ...
   ```

3. **Prepare handout:**
   - Print or project the IP address list
   - Students will need this to connect

### 2. Student Connection Process

**Give students these instructions:**

#### Step 1: Install VS Code Remote - SSH Extension

1. Open VS Code on your laptop
2. Go to Extensions (Ctrl+Shift+X or Cmd+Shift+X)
3. Search for "Remote - SSH"
4. Install the official Microsoft extension

#### Step 2: Connect to Your Pi

1. In VS Code, press `F1` or `Ctrl+Shift+P`
2. Type: `Remote-SSH: Connect to Host`
3. Choose: `Add New SSH Host`
4. Enter: `ssh pi@IP_ADDRESS` (use the IP from the list)
   - Example: `ssh pi@192.168.1.45`
5. Select SSH config file (usually the first option)
6. Click "Connect" in the notification
7. When prompted:
   - Select "Linux" as the platform
   - Enter password: `raspberry` (or your custom password)
8. You're in! VS Code is now running ON the Raspberry Pi

#### Step 3: Open Workshop Folder

1. In VS Code, click "Open Folder"
2. Navigate to `/home/pi/Workshop_Scripts`
3. Click "OK"
4. Enter password again if prompted

You should now see all the workshop scripts in the file explorer!

#### Step 4: Run Your First Script

1. Open `script_1_hello_world.py`
2. Open a Terminal: `Terminal > New Terminal` (or Ctrl+`)
3. Run the script:
   ```bash
   python3 script_1_hello_world.py
   ```
4. Watch the Sense HAT on your physical Pi - you should see text scrolling!

---

## 🎓 Teaching the Headless Workflow

### Key Points to Explain to Students:

1. **Your code runs ON the Pi, not on your laptop**
   - VS Code is just a window into the Pi
   - When you run a script, it executes on the Raspberry Pi hardware
   - That's why you can control the LEDs and camera remotely!

2. **The Sense HAT is your visual output**
   - No monitor = no GUI
   - The LED matrix shows status, countdowns, etc.
   - Watch the physical Pi while running scripts!

3. **Photos are saved as files, not displayed on screen**
   - After taking a photo, look in the file explorer
   - Click the JPG file to view it
   - VS Code has a built-in image viewer

4. **Console output is your friend**
   - Read the messages in the terminal
   - They tell you what's happening
   - Error messages are helpful - don't panic!

---

## 🐛 Troubleshooting Common Issues

### Issue: Student can't connect via SSH

**Possible causes:**
1. Wrong IP address
   - **Fix:** Check the Pi's Sense HAT - it should show the IP
   - **Fix:** Re-read the IP display or reboot the Pi

2. Pi not on network
   - **Fix:** Check WiFi is enabled on the Pi
   - **Fix:** Reboot the Pi and wait for IP to appear

3. SSH not enabled
   - **Fix:** Connect monitor temporarily, enable SSH in raspi-config

4. Firewall blocking connection
   - **Fix:** Check corporate firewall settings
   - **Fix:** Ensure student laptop and Pi are on same network

### Issue: "Permission denied" when connecting

**Cause:** Wrong password

**Fix:**
- Default password is `raspberry`
- If you changed it, provide the correct password
- Students can type it wrong - have them try again carefully

### Issue: VS Code says "Could not establish connection"

**Possible causes:**
1. Pi lost power
   - **Fix:** Check power connection

2. Network dropped
   - **Fix:** Reboot the Pi, get new IP address

3. Another student already connected
   - **Fix:** Multiple connections are allowed, but might cause conflicts
   - **Fix:** Have previous student disconnect first

### Issue: Sense HAT shows "No WiFi"

**Cause:** Pi not connected to network

**Fix:**
1. Connect monitor temporarily
2. Run: `sudo raspi-config` → Wireless LAN
3. Re-enter WiFi credentials
4. Reboot

### Issue: Camera script fails

**Error:** `PiCamera is not enabled`

**Fix:**
```bash
sudo raspi-config
# → Interface Options → Legacy Camera → Enable
sudo reboot
```

### Issue: Script runs but Sense HAT doesn't respond

**Possible causes:**
1. Sense HAT not properly connected
   - **Fix:** Power off, reseat the HAT, power on

2. Another script still running
   - **Fix:** Press Ctrl+C in terminal to stop previous script

3. Wrong permissions
   - **Fix:** Try running with sudo: `sudo python3 script.py`

### Issue: Photos are black/dark

**Cause:** Camera needs time to adjust exposure without preview

**Fix:**
- In the script, increase the sleep time before capture
- Ensure room has good lighting
- Students should test and adjust camera angle

---

## 📊 Managing the Workshop

### Recommended Flow:

1. **Introduction (15 mins)**
   - Explain headless operation
   - Demo SSH connection
   - Show how to view Sense HAT while working remotely

2. **Connection Time (15 mins)**
   - Students connect to their assigned Pi
   - Help troubleshoot connection issues
   - Ensure everyone can run Script 1 successfully

3. **Workshop Progression**
   - Follow normal curriculum (Script 1 → 5)
   - Emphasize watching the physical Pi while code runs
   - Remind students to open photo files to view results

4. **Benefits of Headless:**
   - Emphasize: "Real security cameras work this way!"
   - "You're learning professional remote development"
   - "This is how servers are managed in industry"

### Tips for Managing Remote Sessions:

1. **Walk around and observe the physical Pis**
   - You can see LED status without looking at screens
   - Green = armed, Red = alarm, etc.
   - Helps you spot issues quickly

2. **Have students share screens for troubleshooting**
   - VS Code Remote works great for pair programming
   - Can have students help each other

3. **Keep the IP list visible**
   - Project it on a screen or write on whiteboard
   - Students forget which Pi is theirs

4. **Have spare Pis ready**
   - If one fails, swap it out quickly
   - Have pre-configured backups

---

## 🔐 Security Considerations

### Corporate Network:

1. **Coordinate with IT beforehand**
   - Inform them of the workshop
   - Provide Pi MAC addresses for whitelisting
   - Confirm students can SSH on the network

2. **Password Security**
   - Consider changing default password: `passwd`
   - Use same password on all workshop Pis for simplicity
   - Tell students the password verbally (don't write on board)

3. **After Workshop:**
   - Collect all Pis
   - Optionally: reset to fresh image
   - Store securely

---

## 📦 Equipment Checklist

### Per Pi:
- [ ] Raspberry Pi 4 or 5
- [ ] Sense HAT (attached)
- [ ] Camera Module (connected)
- [ ] Power supply (official 5V/3A recommended)
- [ ] microSD card (16GB+, with Raspberry Pi OS)

### For You (Teacher):
- [ ] Monitor, keyboard, mouse (for setup/troubleshooting)
- [ ] Micro HDMI cable (for emergency access)
- [ ] USB drive (for transferring scripts if needed)
- [ ] Printed IP address list
- [ ] Printed Student Quick Reference
- [ ] Backup Pis (at least 2)
- [ ] Extra power supplies
- [ ] Extra micro HDMI cable

### For Students:
- [ ] Laptop with VS Code installed
- [ ] WiFi access on same network as Pis
- [ ] Note-taking materials

---

## 🚀 Quick Reference for Workshop Day

### If a Pi Needs to Be Rebooted:

```bash
# From SSH session
sudo reboot

# OR physically unplug/replug power
# Wait 60 seconds for it to boot
# Read new IP from Sense HAT
```

### If You Need Emergency Monitor Access:

1. Connect micro HDMI cable to Pi and monitor
2. Connect keyboard and mouse
3. Log in directly (no SSH needed)
4. Fix issue
5. Remove peripherals, return to headless

### If Scripts Need to Be Updated Mid-Workshop:

```bash
# From your laptop
scp updated_script.py pi@192.168.1.45:/home/pi/Workshop_Scripts/

# Students just need to refresh in VS Code (F5)
```

---

## 💡 Advantages of Headless Operation

**Explain these benefits to students:**

1. **Professional Skill**
   - Most servers are headless
   - Remote SSH is industry standard
   - Real-world DevOps practice

2. **Scalability**
   - Can manage dozens of Pis from one laptop
   - No monitors = less equipment = less cost

3. **Real-World Applications**
   - Security cameras don't have monitors
   - IoT devices run headless
   - Cloud servers are all headless

4. **Flexibility**
   - Work from anywhere on the network
   - Can access Pi from home (with VPN)
   - Multiple people can monitor one Pi

---

## 📞 Emergency Contacts

### Before Workshop:

- **IT Support:** [Your IT contact] - For network issues
- **Backup Teacher:** [Colleague] - In case you need help
- **Equipment Room:** [Extension] - For replacement hardware

### During Workshop:

Keep these scripts ready for quick recovery:

```bash
# Kill all Python processes (if script won't stop)
sudo pkill python3

# Release camera (if camera stuck)
sudo fuser -k /dev/vchiq

# Restart SSH service
sudo systemctl restart ssh

# Check network connection
ping google.com

# Check IP address
hostname -I
```

---

## ✅ Day-Before Final Checklist

**Run through this the day before:**

- [ ] All Pis boot successfully
- [ ] All Pis connect to WiFi (see IP on Sense HAT)
- [ ] All Pis have scripts in ~/Workshop_Scripts/
- [ ] All cameras are detected (`vcgencmd get_camera`)
- [ ] All Sense HATs work (test with script_1)
- [ ] You can SSH into each Pi from student laptops
- [ ] IP address list is printed/ready
- [ ] Student Quick Reference is printed
- [ ] Backup Pis are ready
- [ ] You know the WiFi password (for troubleshooting)
- [ ] IT department knows about the workshop
- [ ] Room is booked and set up

---

**You're ready! The headless setup is actually easier than managing monitors once you're set up. Good luck! 🚀**
