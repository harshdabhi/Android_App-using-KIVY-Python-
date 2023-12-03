from kivymd.app import MDApp
from kivy.lang import Builder # by importing this all dependencies are imported automatically
from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import Screen

list_helper="""

Screen:
    ScrollView:
        MDList:
            OneLineListItem:
                text:"Item 1"

            OneLineListItem:
                text:"Item 2"




"""

list_helper2="""

Screen:
    ScrollView:
        MDList:
            id:container



"""


class DemoApp(MDApp):
    def build(self):
        screen=Builder.load_string(list_helper2)
        return screen
    
    def on_start(self): ### this will start the program on app open
        for i in range(20):
            item=OneLineListItem(text='Item'+ str(i))
            self.root.ids.container.add_widget(item)
    


DemoApp().run()