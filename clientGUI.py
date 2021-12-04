from os import name
import tkinter as tk
import socket
import sys
import time
from tkinter.constants import CENTER, RIGHT, X
import threading


HOST = '127.0.0.1'
PORT = 8000
# 電腦上的hostname IP
SERVER = '192.168.232.1'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = False


def makeConnectToServer():
    name = en1.get()
    if(name == ""):
        lb2.config(text="名稱不可為空白")
        return
    try:
        client.connect((SERVER, PORT))
        lb_name.config(text="聊天室內名稱: " + name)
        lb1.config(text="連線成功，輸入要傳送到server的訊息")
        btnOK.config(text="送出")
        lb2.config(text="")
        connect = True

    except:
        print('server is not ready....')
        lb2.config(text="連接失敗，Server may not be ready to connect...")

    # 第一次傳送訊息為自己的名字
    client.send(name.encode())
    # 建立一個持續等待Server Message的 thread
    thread = threading.Thread(
        target=receivingMessage)
    thread.start()
    # 清除entry中的text
    en1.delete(0, 'end')
    ConnectingState()


def ConnectingState():
    btnOK.config(command=sendMessage)


def sendMessage():
    if(en1.get() != ''):
        mes = en1.get()
        client.send(mes.encode())
        # 清除entry中的text
        en1.delete(0, 'end')
        # messageBox.insert('end', mes)
        # messageBox.config()


def receivingMessage():
    while True:
        mes = client.recv(1024).decode()
        if not mes:
            continue
        print(mes)
        messageBox.insert('end', mes)
        messageBox.config()


def disconnect():
    client.close()
    sys.exit(1)


#----------GUI 繪製-----------#
win = tk.Tk()
win.title("client")
win.geometry("600x300")
# win.minsize("600x300")

lb1 = tk.Label(text="輸入使用者名稱")
lb1.pack()

lb_name = tk.Label(text="")
lb_name.pack()

en1 = tk.Entry()
en1.pack()

btnOK = tk.Button(text="確定")
btnOK.config(command=makeConnectToServer)
btnOK.pack()

lb2 = tk.Label(text="")
lb2.pack()

messageBox = tk.Listbox(win)
messageBox.pack(fill='x')

closeBtn = tk.Button(text='斷開連接並關閉視窗')
closeBtn.config(command=disconnect)
closeBtn.pack(side=RIGHT)
win.mainloop()
