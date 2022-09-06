import socket
import threading


host = socket.gethostname()
port = 5000
check = 0
user = input("Enter your username: ")


def rec():
    global check
    while 1:
        messag = skt.recv(1024)
        messag1 = messag.decode()
        if check != messag1:
            print(f"\n{messag1}")
            check = messag1


def more():
    try:
        skt.connect((host, port))
        t1 = threading.Thread(target=rec)
        t1.start()
        while 1:
            message = input()
            message = f"{user}: " + message
            message1 = message.encode()
            skt.send(message1)

    except ConnectionError:
        print("There was an error connecting to the server")


skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t = threading.Thread(target=more)
t.start()
