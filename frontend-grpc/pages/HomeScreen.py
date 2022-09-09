from controllers.HomeController import HomeController

from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem

from pages.BarterSolicitationScreen import BarterSolicitationScreen
from pages.SelfInventoryScreen import SelfInventoryScreen
from pages.UsersListScreen import UsersListScreen

class HomeScreen(MDScreen):
    def __init__(self, id, get_data_from_users, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.user_id = id
        self.main_layout = MDGridLayout()     
        self.main_layout.cols = 1
        self.home_toolbar = MDToolbar(title='PokeTroca', icon='git')
        self.home_toolbar.right_action_items = [['logout', HomeController.logout]]
        self.main_layout.add_widget(self.home_toolbar)
        self.bottom_navigator = MDBottomNavigation()
        self.user_screen = UsersListScreen(HomeController.get_users(self, self.user_id), get_data_from_users, self.user_id)
        self.user_item = MDBottomNavigationItem(name='UsersList', text='Treinadores', icon='pokeball')
        self.user_item.bind(on_tab_press=lambda x: self.user_callback(get_data_from_user=get_data_from_users))
        self.user_item.add_widget(self.user_screen)
        self.barter_item = MDBottomNavigationItem(name='BarterSolicitation', text='Trocas', icon='swap-horizontal-circle-outline')
        self.barter_item.bind(on_tab_press=self.barter_callback)
        self.barter_screen = BarterSolicitationScreen([])
        self.barter_item.add_widget(self.barter_screen)
        self.inventory_item = MDBottomNavigationItem(name='SelfInventory', text='Inventário', icon='bag-personal')
        self.inventory_item.bind(on_tab_press=self.inventory_callback)
        self.inventory_screen = SelfInventoryScreen([])
        self.inventory_item.add_widget(self.inventory_screen)
        self.bottom_navigator.add_widget(self.user_item)
        self.bottom_navigator.add_widget(self.barter_item)
        self.bottom_navigator.add_widget(self.inventory_item)
        self.main_layout.add_widget(self.bottom_navigator)
        self.add_widget(self.main_layout)

        
    def user_callback(self, *args, get_data_from_user):
        self.user_item.remove_widget(self.user_screen)
        users = HomeController.get_users(self, self.user_id)
        self.user_screen = UsersListScreen(users, get_data_from_user, self.user_id)
        self.user_item.add_widget(self.user_screen)

    def barter_callback(self, *args):
        self.barter_item.remove_widget(self.barter_screen)
        barters = HomeController.get_barter_solicitations(self, self.user_id)
        self.barter_screen = BarterSolicitationScreen(barters)
        self.barter_item.add_widget(self.barter_screen)
    
    
    def inventory_callback(self, *args):
        self.inventory_item.remove_widget(self.inventory_screen)
        pokemons = HomeController.get_self_inventory(self, self.user_id)
        self.inventory_screen = SelfInventoryScreen(pokemons)
        self.inventory_item.add_widget(self.inventory_screen)