import tkinter as tk
from tkinter import font
from tkinter.constants import X


def hello():
    print("hello")


def changeLabel():
    enText = en.get()
    lb.config(text=enText)
    pass


win = tk.Tk()
# 標題
win.title("tkinter test")

# 大小
win.geometry("400x200")  # 寬*高
win.minsize(width=400, height=200)  # 視窗最小
win.maxsize(width=1024, height=768)
# 限制是否縮放
#win.resizable(False, False)

# ICON
win.iconbitmap()  # ico檔案

# 顏色
win.config(background="skyblue")  # 也可以使用RGB 6碼

# 透明度
win.attributes("-alpha", 1)  # 0~1

# 置頂
win.attributes("-topmost", True)  # true 1 or fasle 0

# image
img = tk.PhotoImage(file="02.png")


# Entry (輸入框)
en = tk.Entry()
en.pack()

# 按鈕
btn = tk.Button(text="按鈕")
#btn.config(width=10, height=5)
# btn.config(image=img)  # 設置按鈕的圖片
btn.config(command=changeLabel)
btn.pack()  # 封裝


# LABEL (text) #config的參數可以都打在同一行中
lb = tk.Label(text="label 測試")
lb.config(fg="white")
lb.config(bg="skyblue")
lb.config(font="微軟正黑體 20")
lb.pack()

#---------布局-----------#
# Grid 網格布局 (不能與pack同時出現在主視窗)
# user = tk.Label(text="User")
# user.grid(row=0, column=0)
# password = tk.Label(text="password")
# password.grid(row=1, column=0)
# en = tk.Entry()
# en.grid(row = 0, column=1, rowspawn = 2)


# Pack 布局 (垂直中心緊密排列，也有可以設定的參數)
# 參數設定順序會對繪製有影響

# Place 布局 (X Y 座標布局)
btn = tk.Button(text="Button")
btn.place(x=20, y=20)  # 預設原點(anchor)是左上角 ，可以設定anchor的參數為center

# 視窗持續顯示
win.mainloop()
