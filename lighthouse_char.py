from pyghthouse import Pyghthouse #Muss ggf. installiert werden!
from login import username, token #Nicht vergessen, dort die Daten anzupassen!
from time import sleep

bitmap = {'A': 
["0000000000000000000000000000",
 "0000000000111111110000000000",
 "0000000111000000001110000000",
 "0000001110000000000111000000",
 "0000001110000000000111000000",
 "0000001110000000000111000000",
 "0000001110000000000111000000",
 "0000001110000000000111000000",
 "0000001111111111111111000000",
 "0000001110000000000111000000",
 "0000001110000000000111000000",
 "0000001110000000000111000000",
 "0000001110000000000111000000",
 "0000001110000000000111000000"]
}

def displayChar(c):
    # Für jedes "Pixel" des Hochhauses, einmal schauen ob in der Bitmaske für das darzustellende
    # Zeichen c eine 1 steht oder nicht
    # => Farbe entweder auf weiß oder schwarz setzen.
    for y in range(len(img)):
        for x in range(len(img[y])):
            if bitmap[c][y][x] == "1":
                img[y][x] = [255,255,255]
            else:
                img[y][x] = [0,0,0]                    
    
    
p = Pyghthouse(username, token)
Pyghthouse.start(p)

img = Pyghthouse.empty_image()

text = "A" # Mehr geht leider noch nicht... :)

for t in text:
    displayChar(t)
    print(img)
    Pyghthouse.set_image(p, img)
    sleep(1)

input("Warten auf Ende")
