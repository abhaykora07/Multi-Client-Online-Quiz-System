import socket
import threading

PORT = 5000
SERVER_IP = "192.168.56.101"   # ✅ your server IP

def receive(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            if not msg:
                break
            print(msg)
        except:
            break


def send(client):
    while True:
        try:
            ans = input()
            client.sendall(ans.encode())
        except:
            break


def start():
    name = input("Enter your name: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))   # 🔥 auto connect

    client.sendall(name.encode())

    threading.Thread(target=receive, args=(client,), daemon=True).start()
    threading.Thread(target=send, args=(client,), daemon=True).start()

    while True:
        pass


start()