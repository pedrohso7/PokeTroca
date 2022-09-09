# import threading
# import socket
# import json
# from src.main.adapters.socket_adapters import SocketAdapters

# HOST = 'localhost'
# PORT = 8222
# SERVER = socket.gethostbyname(socket.gethostname())
# tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# orig = (HOST, PORT)

# tcp.bind(orig)
# socketAdapters = SocketAdapters()


# def new_client(con, cliente):
#   print('[NOVA CONEXAO]', cliente, "Conectado ")
#   while True:
#     msg = con.recv(2048)
#     if not msg: break
#     socketRequest = json.loads(msg)
#     print(cliente, socketRequest)
#     result = socketAdapters.execute(socketRequest)
#     print('resultServer', result)
#     data = json.dumps(result)
#     con.sendall(bytes(data, encoding="utf-8"))
#   print('Finalizando conexao do cliente', cliente)
#   con.close()

# def start_with_thread():
#   tcp.listen()
#   print("O servidor está ouvindo no endereco:", SERVER)
#   while True:
#     con, cliente = tcp.accept()
#     print('Conectado por', cliente)
#     thread = threading.Thread(target=new_client, args=(con, cliente))
#     thread.start()
#     print('[CONEXOES ATIVAS]', threading.activeCount() - 1)
# print('Servidor rodando...')

# start_with_thread()