from kivymd.app import MDApp
from kivy.uix import label
from kivy.core.window import Window
from kivy.uix import button
from kivy.lang.builder import Builder
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen
Window.size = (350, 550)

style="""

ScreenManager:
    AlarmScreen:

    LoginPage:
    PasswordResetDialog:
    MainMenu:
    ChatScreen:


<LoginPage>:

    name: "login"

    MDLabel:
        text: "TechVision.AI"
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        font_style: "H6"

    MDTextField:
        hint_text: "Username"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint_x: None
        icon_right: "account"
        icon_right_color: app.theme_cls.primary_color
        width: 300
        

    MDTextField:
        hint_text: "Password"
        password: True
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: None
        icon_right: "eye"
        icon_right_color: app.theme_cls.primary_color
        width: 300

    MDFillRoundFlatIconButton:
        text: "Login"
        icon: "login"
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        on_press: app.login()

    MDTextButton:
        text: "Forgot Password?"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1  # Blue color
        on_press: app.password_reset()

<PasswordResetDialog>:
    name: "password_reset"
    auto_dismiss: False
    title: "Password Reset"


    MDTextField:
        hint_text: "Enter your email"
        icon_right: "email"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        size_hint_x: None
        width: 300

    MDRaisedButton:
        text: "Reset Password"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_press: app.back_to_login()

    MDRaisedButton:
        text: "Cancel"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        on_press: app.back_to_login()



<MainMenu>:
    name: "menu"
    
    MDScreen:
        MDNavigationLayout:
            MDScreenManager:
                MDScreen
                    MDTopAppBar:
                        title: "TechVision.AI"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["image", lambda x: app.back_to_image()],["logout", lambda x: app.back_to_login()]]
                        pos_hint: {"top": 1}
                    
                    MDLabel:
                        text: "Welcome User"
                        halign: "center"
                        valign: "bottom"
                        pos_hint: {"center_x": 0.5, "center_y": 0.8}
                        font_style: "H6"

                    MDLabel:
                        text: "AI-CCTV security system"
                        halign: "center"
                        valign: "bottom"
                        pos_hint: {"center_x": 0.5, "center_y": 0.7}
                        font_style: "H6"

                    MDLabel:
                        id: status_label
                        text: app.status
                        halign: "center"
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        font_style: "H6"

                    MDFillRoundFlatIconButton:
                        text: "On"
                        icon: "power"
                        pos_hint: {"center_x": 0.5, "center_y": 0.4}
                        on_press: app.start_system()

                    MDFillRoundFlatIconButton:
                        text: "Off"
                        icon: "power-plug-off"
                        pos_hint: {"center_x": 0.5, "center_y": 0.3}
                        on_press: app.stop_system()




            MDNavigationDrawer:
                id: nav_drawer
                size_hint: .65, 1

                MDNavigationDrawerMenu:
                    MDNavigationDrawerHeader:
                        title: "Support"
                        font_style: "H2"
                        spacing: "20dp"
                        padding: "10dp"
                        opposite_colors: True

                    MDNavigationDrawerDivider:

                    MDNavigationDrawerLabel:
                        text: "MENU"
                        opposite_colors: True


                    MDNavigationDrawerItem:
                        text: "Call Us"
                        icon: "phone"
                        on_release: nav_drawer.set_state("close")
                        icon_color: app.theme_cls.primary_color
                        text_color: app.theme_cls.primary_color
                        
          


                    
<ChatScreen>:
    name: "Images"
    MDTopAppBar:
        title: "TechVision.AI"
        left_action_items: [["backspace", lambda x: app.back_to_main_menu()]]
        pos_hint: {"top": 1}    

    MDLabel:
        text: "Chat Screen"
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        font_style: "H6"
    
 
<AlarmScreen>:
    name:"Alarm"
    MDTopAppBar:
        title: "TechVision.AI"
        left_action_items: [["backspace", lambda x: app.back_to_main_menu()]]
        pos_hint: {"top": 1}    

    MDFillRoundFlatIconButton:
        text: "Alarm-on"
        icon: "alarm"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_press: app.sound_play()

    MDFillRoundFlatIconButton:
        text: "Alarm-off"
        icon: "alarm"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        on_press: app.sound_stop()
                
               
        
 

            

            


    
 



"""
class LoginPage(Screen):
    pass

class MainMenu(Screen):
    pass

class ChatScreen(Screen):
    pass
class PasswordResetDialog(Screen):
    pass

class AlarmScreen(Screen):
    pass



class DemoApp(MDApp):
    status = ""
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(style)
    
    def update_status(self, status):
        self.root.get_screen("menu").ids.status_label.text = status

    def start_system(self):
        self.status = "System is ON"
        self.update_status(self.status)

    def stop_system(self):

        status = "System is OFF"
        self.update_status(status)


    def login(self):
        condition=True
        if condition==True:
            self.root.current = "menu"

    def password_reset(self):
        self.root.current = "password_reset"

    
    def back_to_main_menu(self):
        self.root.current = "menu"

    def back_to_login(self):
        self.root.current = "login"

    def back_to_image(self):
        self.root.current = "Images"
    
    def sound_play(self):
        self.sound = SoundLoader.load('alarm.wav')
        if self.sound:
            self.sound.play()
            
    def sound_stop(self):
        if hasattr(self, 'sound') and self.sound:
            self.sound.stop()
    


    

        
    

   
    

DemoApp().run()