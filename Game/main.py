from kivy.uix.button import Button
from kivy.app import App


#main class
class Main(App):
    def build(self):
        return Button(text = "Lol")


#start
if __name__ == '__main__':
    Main().run()