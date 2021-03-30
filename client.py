import socket, threading, json
from pynput.mouse import Button, Controller
from pynput import mouse

m = Controller()

shutdown = False
join = False

def on_move(x, y):
    print(f'{x} : {y}')
    data = {
        'action': 'move',
        'X': x,
        'Y': y
    }
    s.sendto(json.dumps(data), server)

def on_click(x, y, button, pressed):
    ps = "p" if pressed else 'r'
    print()
    data = {
        'action': 'cli',
        'X': x,
        'Y': y,
        'button': button,
        'ps': ps
    }
    s.sendto(json.dumps(data), server)


def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                data = json.loads(data)
                if data[action] == 'move':
                    pass
                else:
                    pass
        except:
            pass

host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("192.168.1.18",9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

alias = input("Namer: ")

rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()

while shutdown == False:
    if join == False:
        s.sendto(("[" + alias + "] :: connected").encode("utf-8"), server)
        join = True
    else:
        try:
            with mouse.Listener(on_move=on_move,
                                       on_click=on_click, suppress=True) as listener:
                listener.join()

            listener = mouse.Listener(on_move=on_move,
                                             on_click=on_click, suppress=True)
            listener.start()
        except:
            s.sendto(("[" + alias + "] :: disconnected").encode("utf-8"), server)
            shutdown = True

rT.join()
s.close()