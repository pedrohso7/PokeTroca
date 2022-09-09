from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar

class UsersListController():
    def __init__(self, **kwargs):
        super(UsersListController, self).__init__(**kwargs)
    
    def on_item_pressed(self, id, name, get_data_from_user, user_id):
        if(id != -1 & user_id != -1):
            get_data_from_user(user_id=id, name=name, id=user_id)
            MDApp.get_running_app().root.transition.direction = 'left'
            MDApp.get_running_app().root.current = 'inventory_screen'

    def go_to_inventory(self, name, users, id, get_data_from_user):
        def get_user_id(name, users):
            user_id = None
            for user in users:
                if(user.username == name):
                    user_id = user.id
            return user_id
        self.user_id = get_user_id(name, users)

        if(self.user_id == None):
            return Snackbar(text='Nome do usuário incorreto', bg_color=(1, 0, 0, 1),).open()
        get_data_from_user(user_id=self.user_id, name=name, id=id)
        MDApp.get_running_app().root.transition.direction = 'left'
        MDApp.get_running_app().root.current = 'inventory_screen'