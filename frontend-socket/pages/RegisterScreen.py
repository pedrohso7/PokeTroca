from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar

from controllers.RegisterController import RegisterController

class RegisterScreen(MDScreen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        self.main_layout = MDGridLayout(cols=1)
        self.register_toolbar = MDToolbar(title='PokeTroca')
        self.register_toolbar.icon = 'pokeball'
        self.register_toolbar.left_action_items = [['arrow-left', RegisterController.on_back_pressed]]
        self.main_layout.add_widget(self.register_toolbar)
        self.layout = MDGridLayout(cols=1, padding=[150, 0, 150, 0], spacing=20)
        self.layout.add_widget(MDLabel(text='CADASTRO', valign='top', halign='center', font_style='H3'))
        self.field_layout = MDGridLayout(cols=1, spacing=6)
        self.field_1 = MDTextField(hint_text='Nome', mode='rectangle', )
        self.field_2 = MDTextField(hint_text='Nome de usuário', mode='rectangle', ) 
        self.field_3 = MDTextField(hint_text='Senha', password=True, mode='rectangle')
        self.field_layout.add_widget(self.field_1)
        self.field_layout.add_widget(self.field_2)
        self.field_layout.add_widget(self.field_3)
        self.layout.add_widget(self.field_layout)
        self.main_layout.add_widget(self.layout)
        self.register_button = MDRaisedButton(text='Cadastrar', pos_hint= {"center_x": .5, "center_y": .5}, size_hint=[1, None])
        self.register_button.bind(on_release=lambda x: RegisterController.on_register(self, self.field_1.text, self.field_2.text, self.field_3.text))
        # self.button_container = MDGridLayout(cols=1, orientation='tb-rl', size_hint=(1, 0.24))
        # self.button_container.add_widget(self.register_button)
        # self.button_container = MDGridLayout(cols=1, padding=[150, 0, 150, 0])
        # self.button_container.add_widget(self.register_button)
        self.main_layout.add_widget(self.register_button)

        
        self.add_widget(self.main_layout)