class GameObj:
    def __init__(self,name,w,h,x,y):
        self.name = name 
        self.dim = (w,h)
        self.pos = (x,y)
        self.pixels = [(i % w, i // w) for i in range(w*h)]
        self.visible = True
    
    def toggleVisible(self):
        self.visible = not self.visible 

    def moveBy(self,dx,dy):
        self.pos = (self.pos[0]+dx,self.pos[1]+dy)

    def moveTo(self,x,y):
        self.pos = (x,y)

    def getPixels(self):
        x,y = self.pos
        return [(p[0]+x,p[1]+y) for p in self.pixels]
