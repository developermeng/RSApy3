import socket

ip = "0.0.0.0"
port = 8888

server_addr = (ip, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_addr)
server.listen(5)

while True:
    print("wait for connected")
    client, client_addr = server.accept()
    while True:
        cmd = client.recv(1024)
        print("cmd: %s"%str(cmd))
        client.send(b"ok")

server.close()
