from kivymd.app import MDApp
from kivy.lang.builder import Builder

from kivy.uix.screenmanager import ScreenManager, Screen

screen_helper="""

ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:


<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_release:root.manager.current='profile'

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Welcome User'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_release:root.manager.current='Upload'
    
<UploadScreen>:
    name: 'Upload'
    MDLabel:
        text: 'Lets upload files'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_release:root.manager.current='menu'




"""

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class UploadScreen(Screen):
    pass

sm=ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='Upload'))



class DemoApp(MDApp):
    def build(self):
        screen=Builder.load_string(screen_helper)
        return screen 
    


DemoApp().run()