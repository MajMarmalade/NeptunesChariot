import time
import RPi.GPIO as GPIO
import subprocess

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# --- SAFE GPIO PINS (BOARD numbering) ---
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

# --- Key mapping ---
KEY_MAP = {
    HOME:    None,
    L_ARW:   "Left",
    D_ARW:   "Down",
    U_ARW:   "Up",
    R_ARW:   "Right",
    YES:     "Return",
    NO:      None,
    TRIGGER: None
}

# --- Debounce tracking ---
last_state = {pin: 0 for pin in ALL_PINS}
last_time  = {pin: 0 for pin in ALL_PINS}
DEBOUNCE_MS = 200

def press_key(key):
    print(f"Sending keystroke: {key}")
    subprocess.run(["xdotool", "key", key])

print("\nStarting POLLING MODE (works in Raspberry Pi Connect)...")
print("Press buttons to see debug output.\n")

try:
    while True:
        now = time.time() * 1000  # current time in ms

        for pin in ALL_PINS:
            current = GPIO.input(pin)

            # Detect rising edge manually
            if current == 1 and last_state[pin] == 0:
                # Debounce check
                if now - last_time[pin] > DEBOUNCE_MS:
                    print(f"\nDEBUG: Button press detected on pin {pin}")

                    key = KEY_MAP[pin]
                    if key:
                        press_key(key)
                    else:
                        print(f"Pin {pin} has no assigned keystroke.")

                    last_time[pin] = now

            last_state[pin] = current

        time.sleep(0.01)  # 10ms polling interval

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram stopped by user.\n")
