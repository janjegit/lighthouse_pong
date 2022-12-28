from pyghthouse import Pyghthouse, VerbosityLevel
from login import username, token
from time import sleep
from random import randint

from game import GameObj
from control import Controller

def clip(val, min_val, max_val):
    if val < min_val:
        return min_val
    if val > max_val:
        return max_val
    return val

def composeImg(gameObjects,img):
    for obj in gameObjects:
        if obj.visible:
            for p in obj.getPixels():
                x,y = p
                img[y][x] = [255, 255, 255]

def collidesX(gameObj,max_x):
    pixels = gameObj.getPixels()
    for p in pixels:
        if p[0]<=0 or p[0]>=max_x:
            return True
    return False

def collidesY(gameObj,max_y):
    pixels = gameObj.getPixels()
    for p in pixels:
        if p[1]<=0 or p[1]>=max_y:
            return True
    return False

def main_loop():
    p = Pyghthouse(username, token, verbosity=VerbosityLevel.NONE)
    p.start()

    displDim = (28,14) 
    ball = GameObj("ball",1,1,displDim[0]//2,displDim[1]//2)
    pl1  = GameObj("p1",4,1,displDim[0]//2,displDim[1]-1)
    pl2  = GameObj("p2",4,1,displDim[0]//2,0)
        
    actions = { "left"  : (lambda obj : obj.moveBy(-1,0)),
                "right" : (lambda obj : obj.moveBy(1,0))}

    binds_pl1 = {"a" : "left",
                 "d" : "right"}
    binds_pl2 = {"j" : "left",
                 "l" : "right"}

    contr_pl1 = Controller(pl1,binds_pl1,actions)
    contr_pl2 = Controller(pl2,binds_pl2,actions)

    objects = [ball,pl1,pl2]

    velx = 1 
    vely = 1

    while True:
        img = p.empty_image()
        composeImg(objects,img)
        p.set_image(img)

        x,y = ball.pos
        if collidesX(ball,displDim[0]-1):
            velx *= -1
        if collidesY(ball,displDim[1]-1):
            vely *= -1
        ball.moveBy(velx,vely)
        sleep(0.10)

# TODO Ball ändert die Farbe, wenn Bildschirmrand

if __name__ == '__main__':
    main_loop()
