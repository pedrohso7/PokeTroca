from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar

from client_socket import ClientSocket

class RegisterController():
    def __init__(self, **kwargs):
        super(RegisterController, self).__init__(**kwargs)
        
    def on_back_pressed(self):
        MDApp.get_running_app().root.transition.direction = 'right'
        MDApp.get_running_app().root.current = "Login"

    def on_register(self, name, username, password):
        userData = {
            "name": name, 
            "username": username, 
            "password": password
        }
        res = ClientSocket.req(self, 'user/create', userData)
        if(res["statusCode"] == 400):
            return Snackbar(text=res['body']['msg'], bg_color=(1, 0, 0, 1),).open()
        Snackbar(text='Usuário cadastrado com sucesso', bg_color=(0, 1, 0, 1),).open()
        MDApp.get_running_app().root.transition.direction = 'right'
        MDApp.get_running_app().root.current = "Login"