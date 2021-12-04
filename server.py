# -*- coding: utf-8 -*-
from ctypes import sizeof
import socket
import threading
import sys
import time

HOST = '127.0.0.1'
PORT = 8000
SERVER = socket.gethostbyname(socket.gethostname())  # 本機的IP
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
clients = []


def on_new_client(conn, addr, clientName):
    print(f"[NEW CONNECTION] {addr} connected.")
    welcomeMes = "新用戶: " + clientName + " 加入到聊天室中"
    print(welcomeMes)
    sendToAllClient(welcomeMes)
    clientName = clientName
    connected = True
    while connected:
        try:
            clientMessage = str(conn.recv(1024), encoding='utf-8')
        except:
            disconnectMes = 'Disconnect to ' + \
                str(addr) + ' <' + clientName + '>'
            print(disconnectMes)
            disconnectMesToClient = clientName + " 已離開聊天室..."
            sendToAllClient(disconnectMesToClient)
            break
        if(clientMessage != ''):
            seconds = time.time()
            local_time = time.localtime(seconds)
            timeRecordMes = str(local_time.tm_year)+"/"+str(local_time.tm_mon) + "/" + str(
                local_time.tm_mday) + " " + str(local_time.tm_hour)+":"+str(local_time.tm_min)
            # print(time.ctime(seconds))
            print(timeRecordMes + ' Client message from ' + str(addr) +
                  ' ' + clientName + ' : ' + clientMessage)
            otherClientMessage = clientName + " : " + clientMessage
            sendToAllClient(otherClientMessage)
            # serverMessage = 'server response--> ' + clientMessage
            # conn.sendall(serverMessage.encode())
    conn.close()
    print(f"[ACTIVE CONNECTION ] {threading.active_count()-2}")
    sys.exit()


def sendToAllClient(otherClientMessage):
    for client in clients:
        client.send(otherClientMessage.encode())


def start():
    server.listen(5)
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        # 把新的連線加入倒clients 陣列中
        clients.append(conn)
        clientName = str(conn.recv(1024), encoding='utf-8')
        thread = threading.Thread(
            target=on_new_client, args=(conn, addr, clientName))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")


print("[STARTING] server is starting...")
start()

# print('server start at: %s:%s' % ADDR)
# print('wait for connection.....')
# while True:
#     conn, addr = server.accept()
#     #第�??次�?��?��????�client端�??�????: client??????�?
#     clientName = str(conn.recv(1024), encoding='utf-8')
#     print('Connected by ', str(addr) + ' <' + clientName + '>\n')

#     t = threading.Thread(target=on_new_client, args=(conn, addr, clientName,))
#     t.start()
