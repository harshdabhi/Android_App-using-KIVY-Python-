from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.button import MDRectangleFlatButton

class DemoApp(MDApp):
    def build(self):
        screen=Screen()
        table=MDDataTable(
            size_hint=(0.9,0.6),
            rows_num=10,
            pos_hint={'center_x':0.5,'center_y':0.5},
            check=True,
            column_data=[
                ("Name",dp(30)),
                ("Age",dp(30)),
                ("Job",dp(30)),
            ],
            row_data=[
                ("John",20,"Engineer"),
                ("Mary",25,"Teacher"),
                ("Peter",30,"Doctor"),
            ],


        )

        table.bind(on_row_press=self.hello_world)

        screen.add_widget(table)
        return screen
    
    def hello_world(self,instance_table,instance_row):
        ok=MDRectangleFlatButton(
            text="Ok",
            on_release=self.close_dialog

        )

        self.dialog=MDDialog(
            title="Welcome",
            text="Hello World",
            buttons=[
                ok
            ],
        )
        print(instance_row,instance_table)

        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()



DemoApp().run()