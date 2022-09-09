import socket
import json
from src.main.adapters.socket_adapters import SocketAdapters

HOST = 'localhost'
PORT = 8222
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
socketAdapters = SocketAdapters()
print(f'Servidor rodando na porta {PORT}...')
while True:
  con, cliente = tcp.accept()
  print('Conectado por', cliente)
  while True:
    msg = con.recv(2048)
    if not msg: break
    socketRequest = json.loads(msg)
    print(cliente, socketRequest)
    result = socketAdapters.execute(socketRequest)
    print('resultServer', result)
    data = json.dumps(result)
    con.sendall(bytes(data, encoding="utf-8"))
  print('Finalizando conexao do cliente', cliente)
  con.close()
