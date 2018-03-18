import socket
import time
import threading
from threading import Thread

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

port = 443
s.bind(("" , port  ))
s.listen(5)

print("Waiting Connection to kr1y0sX Server")

client,addr = s.accept()
print ("Client" +str(addr[0]) =+"Connected")

def listen():
    global s
    global client,addr

    while True:
        data,addr = s.recv(1024)
        print("Local Host>" +str(data))


def send():
    global s
    global client,addr

    while True:
        msg = input("->")
        s.send(msg)


if __name__ == "__main__":
    Thread(target = listen).start()
    Thread(target = send).start()