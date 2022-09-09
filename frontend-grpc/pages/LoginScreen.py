from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar

from controllers.LoginController import LoginController

class LoginScreen(MDScreen):
    def __init__(self, get_user_id,**kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.main_layout = MDGridLayout(cols=1)
        self.main_layout.add_widget(MDToolbar(title='PokeTroca', icon='git',))
        self.layout = MDGridLayout(cols=1, padding=[150, 30, 150, 100], spacing=20)
        self.layout.add_widget(MDLabel(text='LOGIN', valign='top', halign='center', font_style='H3'))
        self.field_layout = MDGridLayout(cols=1, spacing=6)
        self.field_1 = MDTextField(hint_text='Nome de usuário', mode='rectangle', )
        self.field_layout.add_widget(self.field_1)
        self.field_2 = MDTextField(hint_text='Senha', password=True, mode='rectangle')
        self.field_layout.add_widget(self.field_2)
        self.layout.add_widget(self.field_layout)
        self.login_button = MDRaisedButton(text='Entrar', pos_hint= {"center_x": .5, "center_y": .5}, size_hint=[1, 0.15])
        self.login_button.bind(on_release=lambda x: LoginController.on_login_pressed(self, self.field_1.text, self.field_2.text, get_user_id))
        self.button_container = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, 1))
        self.button_container.add_widget(self.login_button)
        self.register_button = MDRectangleFlatButton(text='Cadastrar', pos_hint= {"center_x": .5, "center_y": .5}, size_hint= [1, 0.15])
        self.register_button.bind(on_release=LoginController.on_register_pressed)
        self.button_container.add_widget(self.register_button)
        self.layout.add_widget(self.button_container)
        self.main_layout.add_widget(self.layout)
        self.add_widget(self.main_layout)