from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget, IconRightWidget
from kivymd.uix.list import MDList
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField


from controllers.UsersListController import UsersListController
class UsersListScreen(Screen):
    def __init__(self, users, get_data_from_user, user_id):
        super(UsersListScreen, self).__init__()
        self.users = users
        self.main_layout = GridLayout(padding=[0, 70, 0, 0])
        self.main_layout.cols = 1
        self.main_layout.spacing = 40
        self.main_layout.add_widget(MDLabel(text='Treinadores Pokemon', valign='top', halign='center', font_style='H4'))
        self.layout_button = MDGridLayout(cols=2, padding=[150, 30, 150, 200], spacing=40)
        self.field = MDTextField(hint_text='Acessar inventário de ', mode='rectangle')
        self.layout_button.add_widget(self.field)
        self.barter_button = MDRaisedButton(text='Buscar inventário', on_release=lambda x: UsersListController.go_to_inventory(self, self.field.text, self.users, user_id, get_data_from_user))
        self.button_container = MDGridLayout(cols=1, padding=[0, 10, 0, 0])
        self.button_container.add_widget(self.barter_button)
        self.layout_button.add_widget(self.button_container) 
        self.main_layout.add_widget(self.layout_button)
        self.spacing = MDGridLayout(padding=[0, 0, 0, 400])
        self.main_layout.add_widget(self.spacing)
        self.layout = MDList()
        self.scroll = ScrollView(size_hint=(1, None), size=(200, 300))
        for user in self.users:
            self.item = OneLineAvatarIconListItem(text=user.username)
            self.item.add_widget(IconLeftWidget(icon='account-outline'))
            self.layout.add_widget(self.item)
        self.scroll.add_widget(self.layout)
        self.main_layout.add_widget(self.scroll)
        self.add_widget(self.main_layout)