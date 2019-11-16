import cv2
import numpy as np
import kociemba
import serial
import time
import array
import keyboard




#arduino = serial.Serial("COM16", 9600)
time.sleep(1)

id={}
moves=[]
letter=['U','R','F','D','L','B']
j=0
for i in letter:
   id[ord(i)]= j= j+1;

perm= 'LBBFULRDRBFDLRDRRUDLDBFUFUBUBUBDULRBUDFFLLDDRLRFRBULFF'
ans= kociemba.solve(perm)

for i in ans:
   if(i==' ' or i=='2'):
      moves.append(x)
   elif(i==chr(39)):
      x= x+6
   else:
      x= id[ord(i)]
moves.append(x)
print(moves)
print(ans)

strmoves=""
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
    time.sleep(.5)

    keyboard.press_and_release('ctrl+tab')
    desbug()
    time.sleep(.6)

    keyboard.write(robot)
    keyboard.press_and_release('enter')
    keyboard.write(strn)
    keyboard.press_and_release('enter')
    time.sleep(.5)

def desbug():
    time.sleep(.5)
    keyboard.press_and_release('alt+tab')
    time.sleep(.5)
    keyboard.press_and_release('alt+tab')
    time.sleep(.8)

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
#arduino.write( str.encode(ans) )
