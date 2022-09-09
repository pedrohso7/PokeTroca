import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8221))

class ClientSocket():
    def __init__(self, **kwargs):
        super(ClientSocket, self).__init__(**kwargs)

    #Este será o método genérico de requisição
    def req(self, route, params):
        jsonData = {
            "route": route,
            "params": params,
        }
        data = json.dumps(jsonData)
        s.sendall(bytes(data, encoding="utf-8"))
        msg = s.recv(8192)
        if(msg == None):
            return {
                "statusCode": 400
            }
        msgJson = json.loads(msg)
        return msgJson