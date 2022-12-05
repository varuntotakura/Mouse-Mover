import pyautogui
import math

# Radius 
R = 3
# measuring screen size
(x,y) = pyautogui.size()
# locating center of the screen 
(X,Y) = pyautogui.position() #pyautogui.position(x/2,y/2)
# offsetting by radius 
pyautogui.moveTo(X+R,Y)

while True:
    for i in range(360):
        # setting pace with a modulus 
        if i%36==0:
            (X,Y) = pyautogui.position()
            pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
