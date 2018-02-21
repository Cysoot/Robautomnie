#import evdev
from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event11')


#prints out device info at start
print(gamepad)
print("----Info----")
print("from Joys import joystick")
print("joy=joystick")
print("         .get gives you the button data")
print("         .")
####InputVariables
##Boutons
aBtn=304
bBtn=305
yBtn=308
xBtn=307
select=314
start=315
L3=317
R3=318
Lb=310
Rb=311
xbox=316
##Joystick
joy_plusL=0
joy_moinsL=1
##Gachettes
Lt=2
Rt=5
#flag
flag=False

class joystick:
    def __init__(self):
        self.name=gamepad
    def press(self):
        #loop and filter by event code and print the mapped label
        for event in gamepad.read_loop():
            
            if event.type == ecodes.EV_KEY:
                
                if event.value == 1:
                    if event.code == yBtn:
                        return "Y"
                    elif event.code == bBtn:
                        return "B"  
                    elif event.code == aBtn:
                        return "A"
                    elif event.code == xBtn:
                        return "X"
                    elif event.code == select:
                        return "Select"
                    elif event.code == start:
                        return "Start"
                    elif event.code == L3:
                        return "L3"
                    elif event.code == R3:
                        return "R3"
                    elif event.code == Lb:
                        return "LB"
                    elif event.code == Rb:
                        return "RB"
                    elif event.code==xbox:
                        return "Home"
            
               





    #elif event.type == ecodes.EV_ABS:
    #    print(event)