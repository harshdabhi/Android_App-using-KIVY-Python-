from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRoundFlatIconButton,MDFillRoundFlatIconButton
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.toolbar import MDBottomAppBar,MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationDrawer 
import pyrebase

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

firebase=pyrebase.initialize_app(config)
db=firebase.database()


class AlertApp(MDApp):


    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.status=''


        icon=MDIcon(icon="cctv",
                    pos_hint={'center_x':0.5,'center_y':0.6},
                    font_size='20')

        label_head=MDLabel(
            text="Welcome User",
            halign='center',
            valign='bottom',
            pos_hint={'center_x':0.5,'center_y':0.8},
            font_style= 'H6' 
        )

        self.label_status=MDLabel(
            text=self.status,
            halign='center',
            pos_hint={'center_x':0.5,'center_y':0.5},
        )
        label=MDLabel(
            text="AI-CCTV security system",
            halign='center',
            valign='bottom',
            pos_hint={'center_x':0.5,'center_y':0.7},
            font_style= 'H6' 
        )

        tool_bar=MDTopAppBar(
            title="TechVision.AI",
            pos_hint={'top':1},
            left_action_items=[["menu", lambda x:x]],
            right_action_items=[["chat", lambda x: x]],

            
        )
    
        screen=Screen()
        self.On_button = MDFillRoundFlatIconButton(
            text="On",
            icon="power",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            on_release=self.start_system,

        )

        self.Off_button = MDFillRoundFlatIconButton(
            text="Off",
            icon="power",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            on_release=self.stop_system,
            width=50
        )
        screen.add_widget(tool_bar)
        screen.add_widget(label)
        screen.add_widget(label_head)
        screen.add_widget(icon)
        screen.add_widget(self.On_button)
        screen.add_widget(self.Off_button)
        screen.add_widget(self.label_status)

        return screen
    


    def start_system(self, obj):

        
        close=MDRoundFlatIconButton(text="Ok",on_release=self.close_dialog)

        self.dialog=MDDialog(
            title="Alert",
            text="System has started",
            buttons=[close],
            size_hint=(0.5,1),
    

        )
        db.child("Darshan").update({"SystemOn": "True"})
        self.status="System is ON"
        self.label_status.text=self.status

        self.dialog.open()


    def stop_system(self, obj):
        close=MDRoundFlatIconButton(text="Ok",on_release=self.close_dialog)

        self.dialog=MDDialog(
            title="Alert",
            text="System has stopped ",
            buttons=[close],
            size_hint=(0.5,1)

        )
        db.child("Darshan").update({"SystemOn": "False"})
        self.status="System is OFF"
        self.label_status.text=self.status

        self.dialog.open()


    def close_dialog(self, obj):
            self.dialog.dismiss()




        
AlertApp().run()