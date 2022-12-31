from pynput import keyboard

class Controller:
    def __init__(self,obj,binds,actions):
        self.obj = obj
        self.binds = binds
        self.actions = actions
        self.listener = keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        self.listener.start()

    def on_press(self,key):
        try:
            if key.char in self.binds:
                self.actions[self.binds[key.char]](self.obj)
        except AttributeError:
            print('special key {0} pressed'.format(key))

    def on_release(self,key):
        if key == keyboard.Key.esc:
            return False
