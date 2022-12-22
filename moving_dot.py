from pyghthouse import Pyghthouse, VerbosityLevel
from game import GameObj
from login import username, token

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
                img[x][y] = [255, 255, 255]

def main_loop():
    p = Pyghthouse(username, token, verbosity=VerbosityLevel.NONE)
    ball = GameObj(4,4,5,6)
    p.start()
    while True:
        img = p.empty_image()
        composeImg([ball],img)
        p.set_image(img)
        s = input()
        for c in s.upper():
            if c == 'A':
                ball.moveBy(-1,0)
            elif c == 'D':
                ball.moveBy(1,0)
            elif c == 'W':
                ball.moveBy(0,1)
            elif c == 'S':
                ball.moveBy(0,-1)

if __name__ == '__main__':
    main_loop()
