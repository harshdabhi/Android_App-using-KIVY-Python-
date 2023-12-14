from kivymd.app import MDApp
from kivy.uix import label
from kivy.uix import button
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import  Screen
from kivy.core.window import Window
import firebase_admin
from firebase_admin import credentials,db,storage
from kivy.clock import Clock
from kivy.utils import platform
import threading
from kivy.core.audio import SoundLoader


Window.size = (360, 640)

cred = credentials.Certificate(
    'serviceAccount.json'    

)
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://cctv-46183-default-rtdb.asia-southeast1.firebasedatabase.app/',
    'storageBucket': 'gs://cctv-46183.appspot.com'
})

system_running_flag=threading.Event()


style="""

ScreenManager:
    LoginPage:
    PasswordResetDialog:
    MainMenu:
    ChatScreen:
    AlarmScreen:


<LoginPage>:

    name: "login"

    MDLabel:
        id: label_login
        text:""
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        font_style: "H6"
        halign: "center"



        
    MDLabel:
        text: "TechVision.AI"
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        font_style: "H6"

    MDTextField:
        hint_text: "Email"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint_x: None
        icon_right: "account"
        icon_right_color: app.theme_cls.primary_color
        on_text:app.submit_email(self.text)
        width: 350
        

    MDTextField:
        hint_text: "Password"
        password: True
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: None
        icon_right: "eye"
        icon_right_color: app.theme_cls.primary_color
        on_text:app.submit_password(self.text)
        width: 350

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

    Image:
        id: image_file
        source: "./App/no_img.jpg"
        size_hint: 0.8, 0.6
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

 
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




class SecurityApp(MDApp):
    status = ""

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(style)
    
    def update_status(self, status):
        self.root.get_screen("menu").ids.status_label.text = status

    def start_system(self):
        self.status = "System is ON"
        self.update_status(self.status)
        db.reference(self.email.split("@")[0]).update({"SystemOn": "True"})


    def stop_system(self):

        status = "System is OFF"
        self.update_status(status)
        db.reference(self.email.split("@")[0]).update({"SystemOn": "False"})



    def login(self):
        global system_running_flag
        system_running_flag.clear()

        try:
            user = db.reference(self.email.split("@")[0]).get()
            if user['Password']==self.password:
                self.thread=threading.Thread(target=self.start_monitoring)
                self.thread.start()
                self.root.current = "menu"

        
        except:
            self.root.current="login"
            self.root.get_screen("login").ids.label_login.text="Incorrect Password/Email"


    def password_reset(self):
        self.root.current = "password_reset"


    def submit_password(self,password):
        self.password=password

    def submit_email(self,email):
        self.email=email

    
    def back_to_main_menu(self):
        self.root.current = "menu"

    def back_to_login(self):
        self.root.current = "login"

    def back_to_image(self):
        destination_path = "image.jpg"
        try:
            storage.reference("images").download(destination_path,"downloaded.jpg")
            self.root.get_screen('Images').ids.image_file.source = "./downloaded.jpg"


        except Exception as e:
            pass

        self.root.current = "Images"

    def sound_play(self):
        self.root.current="Alarm"
        self.sound = SoundLoader.load('alarm.wav')
        if self.sound:
            self.sound.play()
        self.root.current='Alarm'
            
    def sound_stop(self):

        if hasattr(self, 'sound') and self.sound:
            db.reference(self.email.split("@")[0]).update({"Alert": "False"})
            self.sound.stop()
            self.schedule_event.cancel()
            self.scheduled_event = None
            system_running_flag.set()
            self.thread.join()

        self.root.current="menu"

        


    def start_monitoring(self):


        # Check if running on Android
        if platform == 'android':
            from jnius import autoclass
            PythonService = autoclass('org.kivy.android.PythonService')
            PythonService.mService.setAutoRestartService(True)

        self.schedule_event=Clock.schedule_interval(self.monitor_condition, 10)  # Check every 10 seconds

    def monitor_condition(self, dt):
        try:
            condition_path = self.email.split("@")[0]
            condition = db.reference(condition_path).get()
            if condition['Alert']=="True":
                self.sound_play()
                            # self.send_notification("ALert Human detected!")



        except Exception as e:
            print(f"Error while monitoring condition: {e}")

    # def send_notification(self, message):

    #     plyer.notification.notify(title="Notification",message=message,app_name="YourAppName")
    

   
if __name__ == "__main__":
    SecurityApp().run()