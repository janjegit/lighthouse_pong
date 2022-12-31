import random

from vector import Vector2D

class Color:
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

class GameObj:
    def __init__(self,name,w,h,pos,color):
        self.name = name 
        self.w = w
        self.h = h
        self.pos = Vector2D.fromTuple(pos) 
        self.acc = Vector2D()
        self.vel = Vector2D()
        self.color = color
        self.pixels = [(i % w, i // w) for i in range(w*h)]
        self.visible = True
    
    def toggleVisible(self):
        self.visible = not self.visible 

    def move(self):
        self.pos = self.pos + self.vel

    def moveTo(self,x,y):
        self.pos = Vector2D(x,y) 

    def acclerate(self):
        self.vel = self.vel + self.acc

    def clearAcc(self):
        self.acc = Vector2D()

    def applyForce(self,f):
        self.acc = self.acc + f
    
    def setVel(self,vel):
        self.vel = vel
    
    def update(self):
        pass
        
    def getPixels(self):
        x,y = self.pos.x,self.pos.y
        return [(px+x,py+y) for px,py in self.pixels]

    def __str__(self):
        return self.name + \
               " P" + str((self.w,self.h)) + \
               " A" + str(self.acc) + \
               " V" + str(self.vel)

# Kindklasse Paddle von Elternklasse GameObj
class Paddle(GameObj):

    def update(self,f=Vector2D(0,0)):
        self.applyForce(f)
        self.acclerate()
        self.clearAcc()
        self.move()

        displ_h=14
        displ_w=28
        changecolor = False

        if self.pos.x + self.w > displ_w:
            x,y = (displ_w - self.w), self.pos.y
            self.moveTo(x,y)
            self.vel = Vector2D()
            changecolor = True

        if self.pos.x < 0:
            x,y = 0.0 , self.pos.y
            self.moveTo(x,y)
            self.vel = Vector2D()
            changecolor = True

        if changecolor:
            r = random.randint(100,255)
            g = random.randint(100,255)
            b = random.randint(100,255)
            self.color = Color(r,g,b)

# Kindklasse Ball von Elternklasse GameObj
class Ball(GameObj):
    
    def __init__(self,name,w,h,pos,color,pl1=None,pl2=None):
        super().__init__(name,w,h,pos,color)
        self.reset = True 
        self.pl1 = pl1
        self.pl2 = pl2
    
    def launch(self):
        if self.reset == True:
            rx = 0
            ry = 0
            while rx == 0 and ry == 0:
                r = random.randint(0,1)
                neg = [-1,1]
                rx = 0.2*neg[r]
                ry = 0.5*neg[r]
            self.vel = Vector2D(rx,ry)
            self.reset = False

    def resetPosTo(self,x,y):
        self.moveTo(x,y)
        self.vel = Vector2D()
        self.reset = True

    def update(self,f=Vector2D(0,0)):
        self.applyForce(f)
        self.acclerate()
        self.clearAcc()
        self.move()

        displ_h=14
        displ_w=28
        center_x = (displ_w-1)//2
        center_y = (displ_h-1)//2

        changecolor = False

        if self.collide(self.pl1):
            x,y = self.pos.x, self.pl1.pos.y+1
            self.moveTo(x,y)
            self.vel = self.vel * Vector2D(1,-1)
            self.vel = self.vel + self.pl1.vel
            changecolor = True
        elif self.collide(self.pl2):
            x,y = self.pos.x, self.pl2.pos.y-self.h
            self.moveTo(x,y)
            self.vel = self.vel * Vector2D(1,-1)
            self.vel = self.vel + self.pl2.vel
            changecolor = True
        else:
            if self.pos.y - self.h > displ_h:
                self.resetPosTo(center_x,center_y)
                changecolor = True

            if self.pos.y + self.h < 0:
                self.resetPosTo(center_x,center_y)
                changecolor = True

            if self.pos.x + self.w > displ_w:
                x,y = (displ_w - self.w), self.pos.y
                self.moveTo(x,y)
                self.vel = self.vel * Vector2D(-1,1)
                changecolor = True

            if self.pos.x < 0:
                x,y = 0.0 , self.pos.y
                self.moveTo(x,y)
                self.vel = self.vel * Vector2D(-1,1)
                changecolor = True

        if changecolor:
            r = random.randint(100,255)
            g = random.randint(100,255)
            b = random.randint(100,255)
            self.color = Color(r,g,b)

    def collide(self,other):
        if other != None:
            for p in self.getPixels():
                for q in other.getPixels():
                    if int(p[0]) == int(q[0]) and int(p[1]) == int(q[1]):
                        return True
        return False
