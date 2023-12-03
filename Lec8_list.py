from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineIconListItem,TwoLineListItem,MDList
from kivy.uix .scrollview import ScrollView  ## this will help to scroll  across the items
class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        list_view=MDList()  # this wil help to create list view of items
        scroll=ScrollView()
        scroll.add_widget(list_view)
        ## the below code will overlap everything so we need to importvmdlist
        for i in range(100):
            item = TwoLineListItem(text=f"Item {i}",secondary_text="Secondary text")
            list_view.add_widget(item)

        screen.add_widget(scroll)

        return screen
    


DemoApp().run()