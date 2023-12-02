import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class PongGame(Widget):
    pass

class PongBall(Widget):
    pass

class PongApp(App):
    def build(self):
        return PongGame()
    

PongApp().run()