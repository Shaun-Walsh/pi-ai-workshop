"""
================================================================================
BONUS SCRIPT: IP ADDRESS DISPLAY ON BOOT
================================================================================

TEACHER'S NOTE:
---------------
This script is NOT part of the student workshop - it's a setup tool for YOU.

PURPOSE: When Pis boot up headless (no monitor), you need to know their IP
addresses so students can SSH in. This script:
1. Waits for the Pi to connect to WiFi
2. Gets the IP address
3. Scrolls it across the Sense HAT LED matrix
4. Makes workshop setup much easier!

SETUP INSTRUCTIONS:
-------------------
1. Copy this file to /home/pi/show_ip_on_boot.py on each Pi
2. Make it run automatically on boot:

   crontab -e

   Add this line to the bottom:
   @reboot python3 /home/pi/show_ip_on_boot.py &

3. Reboot the Pi: sudo reboot

4. When the Pi boots up, the Sense HAT will display:
   - "No WiFi" (red) if not connected
   - "IP: 192.168.1.45" (green) when connected

USAGE IN WORKSHOP:
------------------
- Plug in all Pis (they boot automatically)
- Wait 30-60 seconds for them to boot and connect
- Read the IP addresses from each Sense HAT
- Students SSH in using: ssh pi@<ip-address>

ALTERNATIVE: UNIQUE HOSTNAMES
-----------------------------
If your corporate network supports mDNS (many don't), you can instead:
1. Give each Pi a unique hostname: sudo raspi-config → Hostname → workshop-pi-01
2. Students SSH using: ssh pi@workshop-pi-01.local

But the IP display method is more reliable on corporate networks.

================================================================================
"""

import time
import socket
from sense_hat import SenseHat

# Initialize Sense HAT
sense = SenseHat()

# Adjust rotation if your Pis are in cases that flip the display
# Try 0, 90, 180, or 270 to get it right-side-up
sense.set_rotation(180)

# Define colors
GREEN = (0, 255, 0)    # Connected successfully
RED = (255, 0, 0)      # No WiFi connection
BLUE = (0, 0, 255)     # Searching for connection

def get_ip_address():
    """
    Gets the Pi's current IP address on the local network.
    Returns '127.0.0.1' (localhost) if not connected to WiFi.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # This doesn't actually send data - just determines the route
        # We use a non-routable address to find our local IP
        sock.connect(('10.255.255.255', 1))
        ip_address = sock.getsockname()[0]
    except Exception:
        # Not connected to network - return localhost
        ip_address = '127.0.0.1'
    finally:
        sock.close()

    return ip_address

# Give the Pi time to boot and connect to WiFi
# Adjust this if your network takes longer to connect
print("Waiting for WiFi connection...")
sense.show_message("Boot...", text_colour=BLUE, scroll_speed=0.05)
time.sleep(15)

# Try to get IP address (with retries)
max_attempts = 10
attempt = 0

while attempt < max_attempts:
    ip_address = get_ip_address()

    if ip_address != '127.0.0.1':
        # Successfully connected to WiFi!
        print(f"Connected! IP Address: {ip_address}")

        # Display IP on LED matrix 10 times, then exit
        # This gives enough time to read it, but doesn't run forever
        for repeat in range(10):
            sense.show_message(f"IP: {ip_address}", text_colour=GREEN, scroll_speed=0.05)
            time.sleep(1)  # Brief pause between repeats

        # Clear display and exit cleanly
        sense.clear()
        print("IP display complete. Exiting.")
        exit(0)

    else:
        # Not connected yet - try again
        attempt += 1
        print(f"No WiFi yet... attempt {attempt}/{max_attempts}")
        sense.show_message("No WiFi", text_colour=RED, scroll_speed=0.05)
        time.sleep(5)  # Wait 5 seconds before trying again

# If we get here, max attempts reached without connecting
print("Failed to connect to WiFi after multiple attempts")
sense.show_message("WiFi FAILED - Check settings", text_colour=RED, scroll_speed=0.05)
sense.clear()
exit(1)

"""
================================================================================
TROUBLESHOOTING
================================================================================

ISSUE: Script doesn't run on boot
FIX:
1. Check crontab is set up: crontab -l (should show the @reboot line)
2. Make sure the file path is correct: /home/pi/show_ip_on_boot.py
3. Check for Python errors: python3 /home/pi/show_ip_on_boot.py

ISSUE: Shows "No WiFi" but Pi is connected
FIX:
1. Increase the initial wait time (line 81) from 15 to 30 seconds
2. Your network might take longer to connect
3. Check WiFi credentials are correct: cat /etc/wpa_supplicant/wpa_supplicant.conf

ISSUE: IP shown is 127.0.0.1 (localhost)
FIX:
1. Pi is not actually connected to the network
2. Check WiFi settings in raspi-config
3. Try connecting to WiFi manually first to verify credentials

ISSUE: LED matrix is upside down
FIX:
1. Change sense.set_rotation(180) to 0, 90, or 270 (line 46)

ISSUE: Script works manually but not on boot
FIX:
1. The @reboot cron job runs before WiFi is ready
2. Increase the sleep time on line 81 (try 30 or 45 seconds)
3. Alternatively, add a longer retry loop

CORPORATE NETWORK NOTES:
-----------------------
Some corporate networks have restrictions:
- May require web portal login (captive portal) - won't work with headless Pi
- May block device-to-device communication
- May have MAC address filtering

If Pis can't get on the network:
1. Talk to your IT department beforehand
2. They may need to whitelist the Pi MAC addresses
3. Consider using a separate router/access point for the workshop

================================================================================
"""
