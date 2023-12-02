from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton



class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Orange"  ### theme for the application
        self.theme_cls.primary_hue="500"
        self.theme_cls.theme_style="Dark"
        screen=Screen()
        btn=MDRectangleFlatButton(text="Click Me",pos_hint={'center_x':0.5,'center_y':0.5})
        screen.add_widget(btn)
        return screen
    

DemoApp().run()