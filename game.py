import random

from pyghthouse import Pyghthouse, VerbosityLevel
from login import username, token
from time import sleep

from vector import Vector2D
from gameobj import GameObj, Color

class Paddle(GameObj):

    def update(self,f=Vector2D(0,0)):
        self.applyForce(f)
        self.acclerate()
        self.clearAcc()
        self.move()

        displ_h=14
        displ_w=28
        boundry = False
        if self.pos.y + self.h > displ_h:
            x,y = self.pos.x, (displ_h - self.h)
            self.moveTo(x,y)
            self.vel = self.vel * Vector2D(1,-1)
            boundry = True

        if self.pos.y < 0:
            x,y = self.pos.x, 0.0
            self.moveTo(x,y)
            self.vel = self.vel * Vector2D(1,-1)
            boundry = True

        if self.pos.x + self.w > displ_w:
            x,y = (displ_w - self.w), self.pos.y
            self.moveTo(x,y)
            self.vel = self.vel * Vector2D(-1,1)
            boundry = True

        if self.pos.x < 0:
            x,y = 0.0 , self.pos.y
            self.moveTo(x,y)
            self.vel = self.vel * Vector2D(-1,1)
            boundry = True

        if boundry:
            r = random.randint(100,255)
            g = random.randint(100,255)
            b = random.randint(100,255)
            self.color = Color(r,g,b)

# Ball
class Ball(GameObj):


    def update(self,f=Vector2D(0,0)):
        self.applyForce(f)
        self.acclerate()
        self.clearAcc()
        self.move()

        displ_h=14
        displ_w=28
        boundry = False
        if self.pos.y + self.h > displ_h:
            x,y = self.pos.x, (displ_h - self.h)
            self.moveTo(x,y)
            self.vel = self.vel * Vector2D(1,-1)
            boundry = True

        if self.pos.y < 0:
            x,y = self.pos.x, 0.0
            self.moveTo(x,y)
            self.vel = self.vel * Vector2D(1,-1)
            boundry = True

        if self.pos.x + self.w > displ_w:
            x,y = (displ_w - self.w), self.pos.y
            self.moveTo(x,y)
            self.vel = self.vel * Vector2D(-1,1)
            boundry = True

        if self.pos.x < 0:
            x,y = 0.0 , self.pos.y
            self.moveTo(x,y)
            self.vel = self.vel * Vector2D(-1,1)
            boundry = True

        if boundry:
            r = random.randint(100,255)
            g = random.randint(100,255)
            b = random.randint(100,255)
            self.color = Color(r,g,b)



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

def initGameObj():
    displDim = (28,14) 
    BALL_START = (displDim[0]//2,displDim[1]//2)
    PL1_START = (displDim[0]//2,1)
    PL2_START = (displDim[0]//2,displDim[1]-2)
    
    objects = {"ball" : Ball("ball",2,1,BALL_START,Color(255,0,0)),
               "pl1" : GameObj("pl1",5,1,PL1_START,Color(255,255,255)),
               "pl2" : GameObj("pl2",5,1,PL2_START,Color(255,255,255))}
    objects["ball"].vel = Vector2D(0.5,0.5)
    
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
