import kivy
kivy.require(kivy.__version__) # replace with your current kivy version !

from kivy.uix.screenmanager import ScreenManager

from kivymd.app import MDApp


from pages.LoginScreen import LoginScreen
from pages.RegisterScreen import RegisterScreen
from pages.HomeScreen import HomeScreen
from pages.InventoryScreen import InventoryScreen

class RootWidget(ScreenManager):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.login_screen = LoginScreen(self.get_user_id_from_login)
        self.login_screen.name = "Login"
        self.add_widget(self.login_screen)
        self.register_screen = RegisterScreen()
        self.register_screen.name = "Register"
        self.add_widget(self.register_screen)
        self.inventory_screen = InventoryScreen(-1, '', -1)
        self.inventory_screen.name = "inventory_screen"
        self.add_widget(self.inventory_screen)
        self.home_screen = HomeScreen(-1, self.get_data_from_users)
        self.home_screen.name = "Home"
        self.add_widget(self.home_screen)
        
    
    def get_user_id_from_login(self, *args, user_id):
        self.remove_widget(self.home_screen)
        self.home_screen = HomeScreen(user_id, self.get_data_from_users)
        self.home_screen.name = "Home"
        self.add_widget(self.home_screen)

    def get_data_from_users(self, *args, user_id, name, id):
        self.remove_widget(self.inventory_screen)
        self.inventory_screen = InventoryScreen(user_id, name, id)
        self.inventory_screen.name = "inventory_screen"
        self.add_widget(self.inventory_screen)

class PokeTroca(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.accent_palette = "Yellow"
        return RootWidget()
    def on_start(self):
        # ClientSocket()
        return super().on_start()
        
PokeTroca().run()