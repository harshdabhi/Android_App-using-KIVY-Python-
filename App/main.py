from kivymd.app import MDApp
from kivy.uix import label
from kivy.uix import button
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import  Screen
import firebase_admin
from firebase_admin import credentials,db,storage
from kivy.clock import Clock
from kivy.utils import platform
import threading
from kivy.core.audio import SoundLoader




cred = credentials.Certificate(
    {
  "type": "service_account",
  "project_id": "cctv-46183",
  "private_key_id": "702159e32b76082913f63118e07e959b67b4f9e6",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDc63BHNIm61Ug5\nU7B1TwRF25yMVTiGknRifc0r3JfOn9L9PfiWYfslHFggxObqBZz8XnicM9obfURy\nUH8V53lCAv5RjcS3E6PXfbKIZW6CPDkjse0ZFfdJeDMA/N2tD+/XPzArVP+UPXoo\nailT7iGrLJ0b6JGJrUQicgQ+InuAmtuZbq2eCrC9Yw7nvJdawnumoPKNVcaEv6Id\n8NG01EaJ/LUJCKChrCLXmoNQ9mR1xxm+9ZiMiH5mcGTJ6bsIOsAMBz0zTS0L5FgS\nSDdUNJ96DqOm//6DIrQjcaXoxj7E5YryZz+zM0Sl8d7gy6P+uaCPFk64IilClAop\nmMIhDMVJAgMBAAECggEAAXDpuRUvJtBYWcNhfcpnqTr/AO1XYo1XBAN1EKmuNdNW\nEX/TfMuj00CllIUkSneB6CWHnOE7tX0yMpqy0YZChLs3RHnrxBP1OCUiQoCC4Yea\nCdERzl2V0N1fW8zKd2QIuPs5CbdSuXlTMCtNHLaLcq3mUnXIaUD/lkfvHiakbpjQ\n5S471SeXC6ZStuXVr95TEx7IQL2+SZ0jXiEAeiLTnVuWVFhuFH7w9efO+8QNtHua\nuJeYdv9P62GYpKoR4cFw4qrmfflBhd9ltViLofXZ5zVbLNYxTIPNx/W/hV5B2BBh\nBJzm7y35teLvqqmJPLb19jR82x5VuxEhwpiRgimB2QKBgQD8p+kc/eWOFEnR5qqH\n6jI48ID8+60KNESq4JGdXHF1IEBQbNXUsJB9Oh/3a/TutXzzfV7e/dwjyN641oMo\n/Xshch55TxUHMNZ4p6cR8Qz24JB7zABAWk2DiCHD7IjIIFX1ADBrucUE/YB0tbpI\nMZYO9W1SJ/WkRxE2Bem2ZDpEFQKBgQDf1/6FUIwDrV58DGs8OvYYhucldh19hdIb\nTx2RriLkdxa0S4AXI7JHZCEWerDvSrvOHEWMluQYVDPwqQSiUJ5My72NxdRx1IPL\nNcfIkKz65y96rZEtavEoXVDK3FXjcAeaJJBTLUiWkjLOHSxdvz9PB+AK3xrxup7H\nIMrUNS2FZQKBgQCU1RzfdTlavtzVhzoBopY/MH3riR5gGnYw6uUce65iPsNkHRjB\nl9kly621BKVeUQ7wKHRQi964PcXlwIe3B8sW4rDM6ScL+1r77FbgnMz0SUkThBLJ\n1eg/iVvKnHXe3h2Em73qV56V1/dpyPuZN4yb9zuU3/E1+p9K4aTRSq2AGQKBgQDK\nj8GJjqxFn5vDEdHwvUJ6S4ncwphJQNIzWFLfw/9bU9E98pzFU84/AINYvkpjIPP2\nvmrJoLpksb4W6DyDTgUSZcTxCLcJE1D4kYBrJVED9DVpBKw9t2roJhm4mc83c+fN\nO41HV9E6QK6tCoVdiHWX5P5/mAnf+gs5E5m4ky7QaQKBgCNz2OAqPZEnB16tld3L\nl0uaP247V+XtqDCNfXuPzsKr9+FyVIpeXwl7YpHdc0WCwAFB/AbjhcDAhP7T6p6x\nmsQLTiVonxpGbHqmaFIiGpEe9wTv42kdxd3XkmeqDTwuQpDM+6NjjH/CNiOBpgrS\n4n0vTkIHh6T5rmZU9wr5ELsM\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-kqo6l@cctv-46183.iam.gserviceaccount.com",
  "client_id": "116518382647140434338",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-kqo6l%40cctv-46183.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

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