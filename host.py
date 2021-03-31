import socket




host = socket.gethostbyname(socket.gethostname())
port = 9090

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

q = False
print('[ Server Started ]')

while not q:
    try:
        data, addr = s.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)
        for client in clients:
            if addr == client:
                s.sendto(data, client)
    except:
        print('[ Server Stopped ]')
        q = True
s.close()
