from vector import Vector2D

class GameObj:
    def __init__(self,name,w,h,pos):
        self.name = name 
        self.w = w
        self.h = h
        self.pos = Vector2D.fromTuple(pos) 
        self.acc = Vector2D()
        self.vel = Vector2D()
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
    
    def update(self):
        self.applyForce(Vector2D(0.0,0.7))
        self.acclerate()
        self.clearAcc()
        self.move()

        displ_h=14
        displ_w=28

        if self.pos.y + self.h > displ_h:
            x,y = self.pos.x, (displ_h - self.h)
            self.moveTo(x,y)
            self.vel = self.vel * Vector2D(0.8,-0.8)

        if self.pos.y < 0:
            x,y = self.pos.x, 0.0
            self.moveTo(x,y)
            self.vel = self.vel * Vector2D(0.8,-0.8)

        if self.pos.x + self.w > displ_w:
            x,y = (displ_w - self.w), self.pos.y
            self.moveTo(x,y)
            self.vel = self.vel * Vector2D(-0.8,0.8)

        if self.pos.x < 0:
            x,y = 0.0 , self.pos.y
            self.moveTo(x,y)
            self.vel = self.vel * Vector2D(-0.8,0.8)
        

    def getPixels(self):
        x,y = self.pos.x,self.pos.y
        return [(px+x,py+y) for px,py in self.pixels]

    def __str__(self):
        return self.name + \
               " P" + str((self.w,self.h)) + \
               " A" + str(self.acc) + \
               " V" + str(self.vel)
