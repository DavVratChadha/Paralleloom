import time
import board
import digitalio
import time
import board
import digitalio
from adafruit_motor import stepper

DELAY = 0.005
STEPS = 200*3


# To use with a Raspberry Pi:
microstep_pins = (digitalio.DigitalInOut(board.D2),digitalio.DigitalInOut(board.D3),digitalio.DigitalInOut(board.D4))
step_pin = digitalio.DigitalInOut(board.D5)
dirn_pin = digitalio.DigitalInOut(board.D6)

step_pin.direction = digitalio.Direction.OUTPUT
dirn_pin.direction = digitalio.Direction.OUTPUT

# Configure the internal GPIO connected to the button as a digital input
button = digitalio.DigitalInOut(board.D7)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Sets the internal resistor to pull-up

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# set motor to run with full steps (not microsteps)
for pin in microstep_pins:
    pin.direction = digitalio.Direction.OUTPUT
    pin.value = False

def single_step(d):
    """Sends a pulse to the STEP output to actuate the stepper motor through one step."""
    # pulse high to drive step
    step_pin.value = True
    time.sleep(d)

    # bring low in between steps
    step_pin.value = False
    time.sleep(d)


# run one revolution CCW
def forward():
    print("Motor spinning CW")
    dirn_pin.value = True
    for i in range(STEPS):
        single_step(DELAY)


# run one revolution CW
def backward():
    print("Motor spinning CCW")
    dirn_pin.value = False
    for i in range(STEPS):
        single_step(DELAY)
"""
#Function to update the microcontroller everytime the button is pressed
def state_change(duration):
    stop_time = time.monotonic() + duration
    while time.monotonic() < stop_time: #to make sure there is a sufficient delay
        if not button.value:
            check_button = True
"""

global state
state = 1 #1 = forward. 0 = backward
global check_button
check_button = False
"""
global count
count = 0
"""
while True:
    """
    count += 1
    if count == 10:
        if led.value:
            led.value = 0
        else:
            led.value = 1
    if count > 10:
        count = 1
        """

    if not button.value: #button pressed
        #print(state)
        if state: #go forward
            #print("in here")
            forward()
            state = 0
        else:
            backward()
            state = 1
        #state_change(0.5)
    #print(button.value)
    time.sleep(0.05)

# Write your code here :-)
