import time
import RPi.GPIO as GPIO
import subprocess

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# --- SAFE GPIO PINS (BOARD numbering) ---
# These avoid EEPROM, I2C, and floating pins
HOME    = 18
L_ARW   = 19
D_ARW   = 21
U_ARW   = 22
R_ARW   = 23
YES     = 24
NO      = 26
TRIGGER = 31   # moved off pin 29 (unsafe)

ALL_PINS = [HOME, L_ARW, D_ARW, U_ARW, R_ARW, YES, NO, TRIGGER]

# --- Setup pins ---
print("Setting up GPIO pins...")
for pin in ALL_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    print(f"Pin {pin} configured as INPUT with PULL-DOWN")

print("\nChecking initial pin states...")
initial_states = {}
for pin in ALL_PINS:
    state = GPIO.input(pin)
    initial_states[pin] = state
    print(f"Pin {pin} initial state: {'HIGH (1)' if state else 'LOW (0)'}")

print("\nValidating pins before enabling edge detection...")
safe_for_edge = []
unsafe_pins = []

for pin in ALL_PINS:
    if initial_states[pin] == 1:
        print(f"WARNING: Pin {pin} is HIGH at startup — skipping edge detection")
        unsafe_pins.append(pin)
    else:
        safe_for_edge.append(pin)

def press_key(key):
    print(f"Sending keystroke: {key}")
    subprocess.run(["xdotool", "key", key])

def button_callback(channel):
    print(f"\nDEBUG: Callback fired for pin {channel}")

    if channel == HOME:
        print("Home Button pressed!")

    if channel == L_ARW:
        print("Left Arrow Button pressed!")
        press_key("Left")

    if channel == D_ARW:
        print("Down Arrow Button pressed!")
        press_key("Down")

    if channel == U_ARW:
        print("Up Arrow Button pressed!")
        press_key("Up")

    if channel == R_ARW:
        print("Right Arrow Button pressed!")
        press_key("Right")

    if channel == YES:
        print("Yes Button pressed!")
        press_key("Return")

    if channel == NO:
        print("No Button pressed!")

    if channel == TRIGGER:
        print("Trigger Button pressed!")

print("\nAdding edge detection to safe pins...")
for pin in safe_for_edge:
    try:
        GPIO.add_event_detect(pin, GPIO.RISING, callback=button_callback, bouncetime=200)
        print(f"Edge detection ENABLED on pin {pin}")
    except RuntimeError as e:
        print(f"ERROR enabling edge detection on pin {pin}: {e}")

print("\nPins skipped due to unsafe startup state:")
for pin in unsafe_pins:
    print(f" - Pin {pin}")

print("\nSystem ready. Listening for button presses...\n")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram stopped by user.\n")