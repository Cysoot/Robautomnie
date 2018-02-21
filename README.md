# Xbox-one controller for linux and python

## Joys.py Description:
Joys.py is a programm that recognize input from the xbox-controller

__bold__attention: for the moment joysticks and triggers are not working

## Requirement
Python 2.4.7/evdev

## Installation:
### step1: Getting xpad
$sudo git clone https://github.com/paroj/xpad.git /usr/src/xpad-0.4

$sudo dkms install -m xpad -v 0.4

reload Driver

$sudo modprobe -r xpad

$sudo modprobe  xpad

### Step2: Getting Joys.py
Clone Joys.py

## Importation:
    from Joys.py import joystick

    joy=joystick()
    
    while 1:

        if joystick.press()=="A"
        
            print("A is pressed")
## Issues ?:
You can report issues here https://github.com/Cysoot/Robautomnie/issues
