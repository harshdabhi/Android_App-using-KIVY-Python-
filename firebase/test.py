from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.utils import platform
from pyrebase import pyrebase
import plyer 

config={
    "apiKey": "AIzaSyCIFPQHlmOeGSx2bb5ipxmFl7g_TsRuhlw",
    "authDomain": "cctv-46183.firebaseapp.com",
    "projectId": "cctv-46183",
    "storageBucket": "cctv-46183.appspot.com",
    "messagingSenderId": "224356173278",
    "appId": "1:224356173278:web:6755a161c1ed679656494f",
    "measurementId": "G-6RN7WDZT8F",
    "serviceAccount":"./firebase/serviceAccount.json",
    "databaseURL":"https://cctv-46183-default-rtdb.asia-southeast1.firebasedatabase.app"
    }


firebase_db = pyrebase.initialize_app(config).database()

class MyApp(App):
    def build(self):
        btn = Button(text="Start Monitoring", on_press=self.start_monitoring)
        return btn

    def start_monitoring(self, instance):
        # Check if running on Android
        if platform == 'android':
            from jnius import autoclass
            PythonService = autoclass('org.kivy.android.PythonService')
            PythonService.mService.setAutoRestartService(True)

        Clock.schedule_interval(self.monitor_condition, 10)  # Check every 10 seconds

    def monitor_condition(self, dt):
        try:
            condition_path = "darshan"
            condition = firebase_db.child(condition_path).get().val()
            for i in condition.each():
                if i.key()=="SystemOn":
                        print(i.val())
                        if i.val()=="True":
                            self.send_notification("Condition is True!")

        except Exception as e:
            print(f"Error while monitoring condition: {e}")

    def send_notification(self, message):

        plyer.notification.notify(title="Notification",message=message,app_name="YourAppName")

if __name__ == "__main__":
    MyApp().run()
