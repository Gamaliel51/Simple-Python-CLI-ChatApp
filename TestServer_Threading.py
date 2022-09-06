import socket
import threading

host = socket.gethostname()
port = 5000
data = 0
data1 = 0
cons = []


def accept():
    while 1:
        skt.listen(1)
        conn, adr = skt.accept()
        conn.send("welcome".encode())
        cons.append(conn)
        t = threading.Thread(target=get, args=(conn, adr))
        t.start()


def get(conn, adr):
    global data
    global data1
    while 1:
        data = conn.recv(1024)
        # print(f"{data.decode()}")
        threading.Thread(target=broadcast, args=(conn, adr)).start()


def broadcast(conn, adr):
    for s in range(len(cons)):
        if (cons[s]) == conn:
            pass
        else:
            (cons[s]).send(data)


skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.bind((host, port))

f = threading.Thread(target=accept)
f.start()
