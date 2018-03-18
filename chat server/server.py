import socket
import time
import threading
from threading import Thread

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

port = 443
deger = 0

while deger == 0:
    try:
        s.connect(("localhost" , port))
        deger += 1
    except:
        pass

print("Connected kr1y0sX Server ")

def listen():
    global s
    

    while True:
        data,addr = s.recv(1024)
        print("Local Host>" +str(data))


def send():
    global s
    

    while True:
        msg = input("->")
        client.send(msg)

if __name__ == "__main__":
    Thread(target = listen).start()
    Thread(target = send).start()