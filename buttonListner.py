import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import pyautogui


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering



#pin numbers for buttons
HOME = 18
L_ARW = 19
D_ARW = 21
U_ARW = 22
R_ARW = 23
YES = 24
NO = 26
TRIGGER = 29


#Import all button
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

def button_callback(channel):
    if channel == HOME:
        print("Home Button was pushed!")
    if channel == L_ARW:
        print("Left Arrow Button was pushed!")
        pyautogui.press('left')
    if channel == D_ARW:
        print("Down Arrow Button was pushed!")
        pyautogui.press('down')    
    if channel == U_ARW:
        print("Up Arrow Button was pushed!")
        pyautogui.press('up') 
    if channel == R_ARW:
        print("Right Arrow Button was pushed!")
        pyautogui.press('right')
    if channel == YES:
        print("Yes Button was pushed!")
        pyautogui.press('enter')
    if channel == NO:
        print("No Button was pushed!") 
    if channel == TRIGGER:
        print("Trigger Button was pushed!")
    
# Add event detection for both buttons
GPIO.add_event_detect(HOME, GPIO.RISING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(L_ARW, GPIO.RISING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(D_ARW, GPIO.RISING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(U_ARW, GPIO.RISING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(R_ARW, GPIO.RISING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(YES, GPIO.RISING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(NO, GPIO.RISING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(TRIGGER, GPIO.RISING, callback=button_callback, bouncetime=200)

# Main loop
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram stopped by user.\n")
