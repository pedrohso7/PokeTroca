from client_socket import ClientSocket
from kivymd.uix.snackbar import Snackbar

class BarterSolicitationController():
    def __init__(self, **kwargs):
        super(BarterSolicitationController, self).__init__(**kwargs)
        
    def on_barter_accepted(self, barter_id):
        params = {
            "id": barter_id,
        }
        res = ClientSocket.req(self, 'trade/accept', params)
        if(res["statusCode"] == 400):
            return Snackbar(text=res['body']['msg'], bg_color=(1, 0, 0, 1),).open()
        return Snackbar(text='Troca aceita', bg_color=(0, 1, 0, 1),).open()

    def on_barter_refused(self, barter_id):
        params = {
            "id": barter_id,
        }
        res = ClientSocket.req(self, 'trade/refuse', params)
        if(res["statusCode"] == 400):
            return Snackbar(text=res['body']['msg'], bg_color=(1, 0, 0, 1),).open()
        return Snackbar(text='Troca recusada', bg_color=(0, 1, 0, 1),).open()