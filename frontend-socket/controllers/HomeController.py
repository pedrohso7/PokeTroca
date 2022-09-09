from kivymd.app import MDApp

from client_socket import ClientSocket

class HomeController():
    def __init__(self, **kwargs):
        super(HomeController, self).__init__(**kwargs)
    def get_users(self, id):
        params = {
            "id": id, 
        }
        return ClientSocket.req(self, 'get-users', params)['body']

    def get_barter_solicitations(self, id):
        params = {
            "id": id, 
        }
        return ClientSocket.req(self, 'trade/solicitations', params)['body']

    def get_self_inventory(self, id):
        params = {
            "id": id, 
        }
        return (ClientSocket.req(self, 'user/inventory', params)['body']['inventory_data'])

    def logout(self):
        MDApp.get_running_app().root.current = "Login"
        MDApp.get_running_app().root.transition.direction = 'right'