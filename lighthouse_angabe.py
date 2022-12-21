from pyghthouse import Pyghthouse #Muss ggf. installiert werden!
from login import username, token #Nicht vergessen, dort die Daten anzupassen!

p = Pyghthouse(username, token)
Pyghthouse.start(p)

img = Pyghthouse.empty_image()
#...
Pyghthouse.set_image(p, img)