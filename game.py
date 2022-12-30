from pyghthouse import Pyghthouse, VerbosityLevel
from login import username, token
from time import sleep

from vector import Vector2D
from gameobj import GameObj, Color

def draw(p,gameObjs):
    img = p.empty_image()

    for _,obj in gameObjs.items():
        if obj.visible:
            for x,y in obj.getPixels():
                x = int(x)
                y = int(y)
                if y>=0 and y<len(img) and x>=0 and x<len(img[0]):
                    img[y][x] = [255, 255, 255]
    p.set_image(img)

def update(objs):
    for _,obj in objs.items():
        obj.update()

def initGameObj():
    displDim = (28,14) 
    BALL_START = (displDim[0]//2,0)
    
    objects = {"ball" : GameObj("ball",1,1,BALL_START)}
    objects["ball"].vel = Vector2D(1,1)
    
    return objects

def main():
    p = Pyghthouse(username, token, verbosity=VerbosityLevel.NONE)
    p.start()
    
    objects = initGameObj()

    while True:
        update(objects)
        draw(p,objects)
        print(objects["ball"])
        sleep(0.08)


# TODO Ball ändert die Farbe, wenn Bildschirmrand

if __name__ == '__main__':
    main()
