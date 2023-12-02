
from kivymd.app import MDApp
from kivymd.uix.label import MDIcon,MDLabel
 ## all UI functions are in this module

from kivy.uix.label import Label


class DemoApp(MDApp):
    def build(self):
        label=Label(text="Hello World",halign='center',valign='top',color=(0.89,0.56,0,1))
        icon_label=MDIcon(icon='language-python',)
        return icon_label




DemoApp().run()