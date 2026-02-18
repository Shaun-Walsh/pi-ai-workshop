# Project Context: Raspberry Pi Workshop for PLC Students

## Audience Profile
- **Target Audience:** Irish PLC (Post Leaving Certificate) students.
- **Streams:** Basic IT and Multimedia.
- **Skill Level:** Beginner to Low-Intermediate. They are comfortable with computers but may be new to Python or hardware GPIO.
- **Learning Style:** Visual, practical, and hands-on. They prefer "doing" over long theory lectures.

## Hardware Configuration
- **Computer:** Raspberry Pi (Model 4 or 5).
- **Add-on:** Raspberry Pi Sense HAT (attached via GPIO).
- **Peripheral:** Raspberry Pi Camera Module.

## Environment Constraints (CRITICAL)
- **Headless Mode:** The Pis are **headless** (no monitors in the workshop room).
- **Remote Access:** Students connect via **VS Code Remote - SSH** to their assigned Pi.
- **Network:** Pis are connected to corporate WiFi.
- **Working Directory:** All scripts are located in the home directory (`/home/pi/` or equivalent).
- **No GUI Support:** Commands like `camera.start_preview()` will **NOT work** because there is no HDMI display output.
- **File Viewing:** Any visual output (photos, charts) must be **saved to a file** so students can view it in the VS Code file explorer or using the built-in image viewer.
- **LED Matrix as Display:** The Sense HAT LED matrix serves as the primary visual output device for immediate feedback (countdowns, status, IP addresses).

## Coding Standards & Constraints
1. **Language:** Python 3.
2. **Libraries:**
   - `sense_hat` (standard library).
   - `picamera` (for camera operations). *Note: Assume Legacy Camera support is enabled or provide clear comments if using `libcamera`.*
   - `time`, `random`, `socket` (for network operations), `datetime`.
3. **Style:**
   - Code must be heavily commented.
   - Variable names must be descriptive (e.g., use `temperature_celsius` not `t`).
   - Avoid complex classes/OOP; stick to procedural code and basic functions.
4. **Headless Constraints:**
   - **NEVER use** `camera.start_preview()` or `camera.stop_preview()` - they require an HDMI display.
   - Use the **Sense HAT LED matrix** for countdowns, status indicators, and visual feedback.
   - Always **save photos to files** with descriptive names so students can open them in VS Code.
   - Print clear messages to the console indicating where files are saved.

## Tone of Voice
- Encouraging and accessible.
- Avoid heavy jargon.
- Use analogies relevant to multimedia (pixels, frames) or basic IT (inputs/outputs).