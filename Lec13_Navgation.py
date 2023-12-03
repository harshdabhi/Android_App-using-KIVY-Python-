from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.toolbar import MDTopAppBar


screen_helper="""
Screen:
    BoxLayout:
        orientation:'vertical'

        MDTopAppBar:
            title:'Navigation'
            left_action_items:[["menu",lambda x:app.navigation_draw()]]
            right_action_items:[["clock",lambda x:app.navigation_draw()]]
            elevation:5

        

        

        MDLabel:
            text:'Hello World'
            halign:'center'    



"""

class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette="Green"

        screen=Builder.load_string(screen_helper)
        return screen
    

    def navigation_draw(self):
        print("hello")

DemoApp().run()