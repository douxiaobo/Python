import tkinter as tk
from tkinter import *

win = tk.Tk()
win.geometry("300x200")

# 直接使用 text 参数而不是 textvariable
label = Label(win, text="Hello, World!", relief=RAISED,
             bg="white", fg="black",
             font=("Arial", 16),
             padx=20, pady=20)

label.pack(pady=50)
win.mainloop()