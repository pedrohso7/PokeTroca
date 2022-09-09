from kivymd.app import MDApp

from middleware_grpc import runGRPCMethod

class HomeController():
    def __init__(self, **kwargs):
        super(HomeController, self).__init__(**kwargs)
    def get_users(self, id):
        params = {
            "id": id, 
        }
        return runGRPCMethod('get-users', params).users

    def get_barter_solicitations(self, id):
        params = {
            "id": id, 
        }
        return runGRPCMethod( 'trade/solicitations', params).tradeList

    def get_self_inventory(self, id):
        params = {
            "id": id, 
        }
        return (runGRPCMethod( 'user/inventory', params).inventories)

    def logout(self):
        MDApp.get_running_app().root.current = "Login"
        MDApp.get_running_app().root.transition.direction = 'right'