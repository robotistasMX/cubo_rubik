import keyboard
import time
strmoves= ""
moves=[1, 8, 7, 3, 2, 11, 7, 6, 2, 6, 2, 2, 6, 6, 1, 2, 2, 5, 5, 4, 6, 6, 5, 5, 3, 3, 1, 1]
robot=""

time.sleep(1)
keyboard.press_and_release('alt+tab')
time.sleep(.5)

def run():
    strn="n="+str(pos)+";"
    print(robot)
    print(strn)

    keyboard.write(robot)
    keyboard.press_and_release('enter')
    keyboard.write(strn)
    keyboard.press_and_release('enter')

    keyboard.press_and_release('ctrl+tab')
    desbug()

    keyboard.write(robot)
    keyboard.press_and_release('enter')
    keyboard.write(strn)
    keyboard.press_and_release('enter')

    """if(last==True):
        keyboard.press_and_release('F5')
        time.sleep(2.5)
        keyboard.press_and_release('F12')
        time.sleep(r-l+1)
        keyboard.press_and_release('F7')
        time.sleep(.5)"""

def desbug():
    time.sleep(.3)
    keyboard.press_and_release('alt+tab')
    time.sleep(.2)
    keyboard.press_and_release('alt+tab')
    time.sleep(.5)

strmoves="0"
for i in moves:
    strmoves=strmoves+","+str(i)
print(strmoves)

keyboard.write(strmoves)
keyboard.press_and_release('down')
#keyboard.press_and_release('f5')
keyboard.press_and_release('ctrl+tab')
desbug()
keyboard.write(strmoves)
keyboard.press_and_release('down')
keyboard.press_and_release('ctrl+tab')
desbug()


pos=0
l=1
r=1
robot="int robot[]={0"
last=0
curr=(moves[0]>=1 and moves[0]<=4) or (moves[0]>=7 and moves[0]<=10)

for i in moves:
    pos=pos+1
    curr=(i>=1 and i<=4) or (i>=7 and i<=10)
    robot=robot+","+str(int(curr))
robot=robot+"};"
run()
