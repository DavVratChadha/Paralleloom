import time
import board
import digitalio
import time
import board
import digitalio
from adafruit_motor import stepper
import pwmio

DELAY = 0.005
STEPS = 200*3


## To use with a Raspberry Pi:
microstep_pins = (digitalio.DigitalInOut(board.D2),digitalio.DigitalInOut(board.D3),digitalio.DigitalInOut(board.D4))
step_pin = digitalio.DigitalInOut(board.D5)
dirn_pin = digitalio.DigitalInOut(board.D6)

step_pin.direction = digitalio.Direction.OUTPUT
dirn_pin.direction = digitalio.Direction.OUTPUT


## Configure the internal GPIO connected to the button as a digital input
button = digitalio.DigitalInOut(board.D7)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Sets the internal resistor to pull-up

##Emergency Switch
Em_switch = digitalio.DigitalInOut(board.D8)
Em_switch.direction = digitalio.Direction.INPUT
Em_switch.pull = digitalio.Pull.UP # Sets the internal resistor to pull-up



##LEDs
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT


ledR = digitalio.DigitalInOut(board.D9)
ledR.direction = digitalio.Direction.OUTPUT

ledG = digitalio.DigitalInOut(board.D10)
ledG.direction = digitalio.Direction.OUTPUT



## set motor to run with full steps (not microsteps)
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





def forward():
    print("Motor spinning CW")
    dirn_pin.value = True
    for i in range(STEPS):
        if not Em_switch.value:    #while toggle high, stop
            emergency_toggle()
        else:
            single_step(DELAY)


def backward():
    print("Motor spinning CCW")
    dirn_pin.value = False
    for i in range(STEPS):
        if not Em_switch.value:    #while toggle high, stop
            emergency_toggle()
        else:
            single_step(DELAY)


def emergency_toggle():
    toggle_led(1)
    soundtrack = 1 #toggles between 0 and 1

    while(not Em_switch.value):        # while toggle switch high
        buzzer.duty_cycle = 1000
        if soundtrack:
            ledR.value = 1
            for f in range(50,750,50):
                # increasing frequency
                buzzer.frequency = f# Up
                time.sleep(0.1)
            soundtrack = 0
        else:
            ledR.value = 0
            for f in range(750,50,-50):
                # decreasing frequency
                buzzer.frequency = f# Down
                time.sleep(0.1)
            soundtrack = 1
        ledR.value = 0
        buzzer.duty_cycle = 0
    time.sleep(1)
    toggle_led(0)                      # return leds back to normal
   # once switch is back to normal, leaves while loop, exits else, and continues for loop.

def toggle_led(emergency):
    if emergency:
        ledR.value = True
        ledG.value = False
    else:
        ledR.value = False
        ledG.value = True


# Global Vars
global state
state = 1 #1 = forward. 0 = backward
global check_button
check_button = False

# set up buzzer as PWM output
buzzer = pwmio.PWMOut(board.D11, duty_cycle = 0, frequency = 150, variable_frequency = True)
mode = "freq"

def play_song():
    speed = 0.12
    buzzer.duty_cycle = 1000
    song_chorus_rhythmn = [2, 2, 3, 3, 6, 1, 1, 1, 1, 3, 3, 3, 1, 2, 1, 1, 1, 1, 3, 3, 3, 1, 2, 2, 2, 4, 8, 1, 1, 1, 1, 3, 3, 6, 1, 1, 1, 1, 3, 3, 3, 1, 2, 1, 1, 1, 1, 3, 3, 3, 1, 2, 2, 4, 8]
    song_chorus_melody = [466, 415, 698, 699, 622, 466, 466, 415, 415, 622, 622, 554, 523, 466, 554, 554, 554, 554, 554, 622, 523, 466, 415, 415, 415, 622, 554, 466, 466, 415, 415, 698, 698, 622, 466, 466, 415, 415, 831, 523, 554, 523, 466, 554, 554, 554, 554, 554, 622, 523, 466, 415, 415, 622, 554]
    for i in range(0,4):
        for j in range(song_chorus_rhythmn[i]):
            buzzer.frequency = song_chorus_melody[i]
            time.sleep(speed)
    buzzer.duty_cycle = 0
    time.sleep(0.1)
    buzzer.duty_cycle = 1000
    ledR.value = 0
    ledG.value = 0
    for i in range(4,14):
        for j in range(song_chorus_rhythmn[i]):
            buzzer.frequency = song_chorus_melody[i]
            time.sleep(speed)
    buzzer.duty_cycle = 0
    time.sleep(0.15)
    buzzer.duty_cycle = 1000
    ledR.value = 1
    ledG.value = 1
    for i in range(15,24):
        for j in range(song_chorus_rhythmn[i]):
            buzzer.frequency = song_chorus_melody[i]
            time.sleep(speed)
    buzzer.duty_cycle = 0
    time.sleep(0.08)
    buzzer.duty_cycle = 1000
    ledR.value = 0
    ledG.value = 0
    for i in range(24,27):
        for j in range(song_chorus_rhythmn[i]):
            buzzer.frequency = song_chorus_melody[i]
            time.sleep(speed)
    buzzer.duty_cycle = 0
    time.sleep(0.1)
    buzzer.duty_cycle = 1000
    ledR.value = 1
    ledG.value = 1
    for i in range(27,34):
        for j in range(song_chorus_rhythmn[i]):
            buzzer.frequency = song_chorus_melody[i]
            time.sleep(speed)
    buzzer.duty_cycle = 0
    time.sleep(0.1)
    buzzer.duty_cycle = 1000
    ledR.value = 0
    ledG.value = 0
    for i in range(34,43):
        for j in range(song_chorus_rhythmn[i]):
            buzzer.frequency = song_chorus_melody[i]
            time.sleep(speed)
    buzzer.duty_cycle = 0
    time.sleep(0.15)
    buzzer.duty_cycle = 1000
    ledR.value = 1
    ledG.value = 1
    for i in range(43,52):
        for j in range(song_chorus_rhythmn[i]):
            buzzer.frequency = song_chorus_melody[i]
            time.sleep(speed)
    buzzer.duty_cycle = 0
    time.sleep(0.15)
    buzzer.duty_cycle = 1000
    ledR.value = 0
    ledG.value = 0
    for i in range(52,55):
        for j in range(song_chorus_rhythmn[i]):
            buzzer.frequency = song_chorus_melody[i]
            time.sleep(speed)
    buzzer.duty_cycle = 0
    ledR.value = 1
    ledG.value = 1

global song_mode
song_mode = 0 #0 = OFF, 1 = ON

#Main
while True:
    toggle_led(0)
    if song_mode:
        ledR.value = 1
        ledG.value = 1
        if not button.value:
            play_song()
    if not button.value: #button pressed

        if state: #go forward

            forward()
            state = 0   #next press poll, it runs backwards.
            #forward_count = 0

        else:

            backward()
            state = 1
            #backward_count = 0

    time.sleep(0.05)
