"""
================================================================================
SCRIPT 2: ENVIRONMENT MONITOR - Reading Sensors
================================================================================

TEACHER'S INTRO:
----------------
This script introduces students to:
1. Reading data from physical sensors
2. Working with variables and data types (floats)
3. Formatting output for readability
4. Making decisions with if/else statements
5. Understanding temperature, humidity, and pressure

ANALOGY: The Sense HAT sensors are like a weather station. Just like the
weather app on your phone reads temperature from sensors, our Pi can do
the same thing!

REAL-WORLD CONNECTION: These same types of sensors are used in smart
thermostats, weather stations, and even smartphones.

EXPECTED OUTCOME: Students will see live sensor readings displayed on
screen and watch the LED matrix change color based on temperature.

================================================================================
"""

# Import required libraries
from sense_hat import SenseHat
import time

# Create the SenseHat object
sense = SenseHat()

# Clear the display to start fresh
sense.clear()

print("=== ENVIRONMENT MONITOR STARTING ===")
print("Reading sensors... (Press Ctrl+C to stop)\n")

# Run the monitoring loop
# This will keep checking the sensors until you stop the program
try:
    while True:
        # Read temperature from the sensor
        # NOTE: The Sense HAT reads temperature in Celsius by default
        temperature_celsius = sense.get_temperature()

        # Round to 1 decimal place for easier reading
        temperature_celsius = round(temperature_celsius, 1)

        # Read humidity (moisture in the air) as a percentage
        humidity_percent = sense.get_humidity()
        humidity_percent = round(humidity_percent, 1)

        # Read atmospheric pressure in millibars
        pressure_mb = sense.get_pressure()
        pressure_mb = round(pressure_mb, 1)

        # Display the readings in the console
        print(f"🌡️  Temperature: {temperature_celsius}°C")
        print(f"💧 Humidity: {humidity_percent}%")
        print(f"🔽 Pressure: {pressure_mb} mb")
        print("-" * 40)

        # NOW LET'S MAKE A DECISION BASED ON THE DATA!
        # If temperature is high, turn LEDs red (hot)
        # If temperature is comfortable, turn LEDs green (good)
        # If temperature is low, turn LEDs blue (cold)

        if temperature_celsius > 25:
            # Hot temperature - show RED
            sense.clear((255, 0, 0))  # Red
            print("🔥 STATUS: Hot!")
        elif temperature_celsius < 20:
            # Cold temperature - show BLUE
            sense.clear((0, 0, 255))  # Blue
            print("❄️  STATUS: Cold!")
        else:
            # Comfortable temperature - show GREEN
            sense.clear((0, 255, 0))  # Green
            print("✅ STATUS: Comfortable!")

        print("\nNext reading in 3 seconds...\n")

        # Wait 3 seconds before taking the next reading
        time.sleep(3)

except KeyboardInterrupt:
    # This runs when you press Ctrl+C to stop the program
    print("\n\n=== ENVIRONMENT MONITOR STOPPED ===")
    sense.clear()  # Turn off the LEDs
    print("Display cleared. Goodbye!")

"""
================================================================================
TROUBLESHOOTING & CHALLENGES
================================================================================

COMMON ISSUES:
--------------
1. Temperature seems too high:
   → The Sense HAT sits on top of the Pi CPU, which generates heat
   → For more accurate readings, subtract 10-15 degrees:
     temperature_celsius = sense.get_temperature() - 10

2. Humidity reading seems off:
   → The CPU heat also affects humidity readings
   → This is a known limitation of the Sense HAT placement

3. Program won't stop:
   → Press Ctrl+C on your keyboard
   → The "try/except" block catches this and exits cleanly

4. "NameError" when running:
   → Make sure you've imported sense_hat and time at the top

CHALLENGES FOR EARLY FINISHERS:
-------------------------------
EASY:
1. Change the temperature thresholds (try 23 and 27 instead of 20 and 25)
2. Add a fourth condition: if temp is VERY hot (>30), flash red rapidly
3. Change the display colors to different shades

MEDIUM:
4. Display the temperature NUMBER on the LED matrix instead of just a color
   (hint: use sense.show_message() inside the if statement)

5. Create a humidity alert: if humidity > 70%, flash blue (wet/humid)

6. Add Fahrenheit conversion:
   temperature_fahrenheit = (temperature_celsius * 9/5) + 32
   Then display both readings

HARD:
7. Create a "feels like" temperature that combines temp and humidity
8. Log the data to a text file (research Python file writing)
9. Create a visual "thermometer" on the LED matrix using set_pixel()
   - Bottom rows light up for cold (blue)
   - Middle rows for comfortable (green)
   - Top rows for hot (red)

EXTENSION ACTIVITY:
-------------------
Challenge: "Can you trick the sensor?"
- Breathe on it (adds warmth and moisture)
- Hold an ice pack near it
- Put it in sunlight
Discuss: Why do sensor readings change? What affects them?

DISCUSSION QUESTIONS:
--------------------
1. Why might temperature sensors in your phone not always be accurate?
2. What other devices in your home use temperature sensors?
3. How could you make this into a weather station?

================================================================================
"""
