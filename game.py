import random

from pyghthouse import Pyghthouse, VerbosityLevel
from time import sleep

from login import username, token
from vector import Vector2D
from control import Controller
from gameobj import Ball, Paddle, Color

def draw(p,gameObjs):
    img = p.empty_image()

    for _,obj in gameObjs.items():
        if obj.visible:
            for x,y in obj.getPixels():
                x = int(x)
                y = int(y)
                if y>=0 and y<len(img) and x>=0 and x<len(img[0]):
                    c = obj.color
                    img[y][x] = [c.r, c.g, c.b]
    p.set_image(img)

def update(objs):
    for name,obj in objs.items():
        obj.update()

def initGameObjects():
    displDim = (28,14) 
    BALL_START= (displDim[0]//2,displDim[1]//2)
    PL1_START = ((displDim[0]//2)-2,1)
    PL2_START = ((displDim[0]//2)-2,displDim[1]-2)
    
    objects = {"ball" : Ball("ball",2,1,BALL_START,Color(255,0,0)),
               "pl1" : Paddle("pl1",5,1,PL1_START,Color(255,255,255)),
               "pl2" : Paddle("pl2",5,1,PL2_START,Color(255,255,255))}
    objects["ball"].pl1 = objects["pl1"]
    objects["ball"].pl2 = objects["pl2"]
    
    return objects

def reset(objects):
    pass

def initLighthouse():
    p = Pyghthouse(username, token, verbosity=VerbosityLevel.NONE)
    p.start()
    return p

def initControls(objects):
    

    actions = {"left" : lambda obj : obj.applyForce(Vector2D(-0.5,0)),
               "stop" : lambda obj : obj.setVel(Vector2D()),
               "launch" : lambda obj : obj.launch(),
               "right" : lambda obj : obj.applyForce(Vector2D(0.5,0))}
    
    ball_binds= {"g" : "launch"}

    pl1_binds = {"a" : "left",
                 "s" : "stop",
                 "d" : "right"}

    pl2_binds = {"j" : "left",
                 "k" : "stop",
                 "l" : "right"}

    return [Controller(objects["ball"],ball_binds,actions),
            Controller(objects["pl1"],pl1_binds,actions),
            Controller(objects["pl2"],pl2_binds,actions)]

def main():
    p = initLighthouse()
    objects = initGameObjects()
    controls = initControls(objects)

    while True:
        update(objects)
        draw(p,objects)
        sleep(0.08)

if __name__ == '__main__':
    main()
