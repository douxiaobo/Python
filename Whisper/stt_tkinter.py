import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as tk
# from tkinter import *

root = tk.Tk()
screetWidth = root.winfo_screenwidth()
screetHeight = root.winfo_screenheight()
w=400
h=200
x=(screetWidth-w)/2
y=(screetHeight-h)/2
root.title("Speech to Text")
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
root.maxsize(800, 400)
root.minsize(200, 100)


# root.config(bg="green") # 设置窗口背景颜色为绿色    无效

# root["bg"] = "green"  # 使用这种方式设置背景色   无效

# root.configure(bg="green") # 使用这种方式设置背景色   无效

# label = tk.Label(root, text="Speech to Text App", bg="green", fg="white")
# label.pack(pady=20)

# create a label widget
root.mainloop()


# export TK_SILENCE_DEPRECATION=1
# python3 stt_tkinter.py

# brew install tcl-tk       # 使用 Homebrew 安装最新 Tcl/Tk（长期解决）