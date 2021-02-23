import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import requests

URL_BASE = 'http://volumio.local:4005/'
URL_NEXT = 'song/next'
URL_PREV = 'song/prev'

BUTTON_NEXT = 16
BUTTON_PREV = 18

def button_callback_next(channel):
    print("Button NEXT was pushed!")
    x = requests.post(URL_BASE + URL_NEXT)
    print(x.text)
	
def button_callback_prev(channel):
    print("Button PREV was pushed!")
    x = requests.post(URL_BASE + URL_PREV)
    print(x.text)

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# Button 1 - NEXT
GPIO.setup(BUTTON_NEXT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin BUTTON_NEXT to be an input pin and set initial value to be pulled low (off)
# Button 2 - PREV
GPIO.setup(BUTTON_PREV, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin BUTTON_PREV to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(BUTTON_NEXT,GPIO.RISING,callback=button_callback_next) # Setup event on pin BUTTON_NEXT rising edge
GPIO.add_event_detect(BUTTON_PREV,GPIO.RISING,callback=button_callback_prev) # Setup event on pin BUTTON_PREV rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up