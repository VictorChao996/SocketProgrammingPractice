import socket
import sys
import time
import threading

HOST = '127.0.0.1'
PORT = 8000
# 電腦上的hostname IP
SERVER = '192.168.232.1'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def receivingMessage():
    while True:
        mes = client.recv(1024).decode()
        if not mes:
            continue
        print(mes)


print('please input your name: ')
# 輸入client端的名字
name = input()
clientMessage = name
try:
    client.connect((SERVER, PORT))
except:
    print('server is not ready....')
    # 結束client 程式
    sys.exit(1)
# 第一次傳送訊息為自己的名字
client.send(clientMessage.encode())
thread = threading.Thread(
    target=receivingMessage)
thread.start()

while True:
    print('輸入要傳送到server的訊息')
    clientMessage = input()
    if(clientMessage == 'EXIT'):
        print('client close...')
        client.close()
        break
    print('send: {' + clientMessage + '} to server....')
    client.send(clientMessage.encode())

    # # 以下為server回覆message
    # serverMessage = str(client.recv(1024), encoding='utf-8')
    # print('Server:', serverMessage)
    # if(len(serverMessage) == 0):
    #     client.close()
    #     print('server closed connection.')
    #     print('client close...')
    #     break
