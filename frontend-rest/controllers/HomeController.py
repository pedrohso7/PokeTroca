from kivymd.app import MDApp

from RestRequest import RestRequests

class HomeController():
    def __init__(self, **kwargs):
        super(HomeController, self).__init__(**kwargs)
    def get_users(self, id):
        params = {
            "id": id, 
        }
        return RestRequests.req(self, 'GET', 'get-users', params)['body']

    def get_barter_solicitations(self, id):
        params = {
            "id": id, 
        }
        return RestRequests.req(self, 'GET','trade/solicitations', params)['body']

    def get_self_inventory(self, id):
        params = {
            "id": id, 
        }
        return (RestRequests.req(self, 'GET','user/inventory', params)['body']['inventory_data'])

    def logout(self):
        MDApp.get_running_app().root.current = "Login"
        MDApp.get_running_app().root.transition.direction = 'right'