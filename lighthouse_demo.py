from pyghthouse import Pyghthouse #Muss ggf. installiert werden!
from login import username, token #Nicht vergessen, dort die Daten anzupassen!
from random import randint
from time import sleep

p = Pyghthouse(username, token)
Pyghthouse.start(p)

img = Pyghthouse.empty_image()

class gameObj:
    __init__(obj,x,y):
        self.shape = obj
        self.x = x
        self.y = y
        self.visible = True
    
    def setVisible(b):
        self.visible = b

    def isVisible():
        return self.visible

    def pos():
        return (x,y)

    def move(dx,dy):
        self.x += dx
        self.y += dy


while True:
    for x in range(0, 28):
        for y in range(0, 14):
            img[y][x] = [randint(0, 255), randint(0, 255), randint(0,255)]
    sleep(0.5)
    Pyghthouse.set_image(p, img)
