from pyghthouse import Pyghthouse #Muss ggf. installiert werden!
from login import username, token #Nicht vergessen, dort die Daten anzupassen!
from random import randint
from time import sleep

p = Pyghthouse(username, token)
Pyghthouse.start(p)

img = Pyghthouse.empty_image()



while True:
    for x in range(0, 28):
        for y in range(0, 14):
            img[y][x] = [randint(0, 255), randint(0, 255), randint(0,255)]
    sleep(0.10)
    Pyghthouse.set_image(p, img)
