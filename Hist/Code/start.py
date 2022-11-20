from menu import Main
import sound

class Start():
    def __init__(self):
        self.main = Main()
        self.son = sound.Musique()
    def start(self):
        self.son.jouer('go')
        self.main.main_menu()


start = Start()
start.start()