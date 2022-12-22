class GameObj:
    def __init__(self,w,h,x,y):
        self.dim = (w,h)
        self.pos = (x,y)
        self.pixels = [(i % w, i // w) for i in range(w*h)]
        self.visible = True
    
    def setVisiblility(self,b):
        self.visible = b

    def toggleVisible(self):
        self.visible = not self.visible 

    def moveBy(self,dx,dy):
        self.pos = (self.pos[0]+dx,self.pos[1]+dy)

    def moveTo(self,x,y):
        self.pos = (x,y)

    def getPixels(self):
        x,y = self.pos
        return [(p[0]+x,p[1]+y) for p in self.pixels]
