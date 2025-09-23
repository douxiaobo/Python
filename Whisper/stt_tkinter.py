import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# import tkinter as tk
from tkinter import *
from tkinter.ttk import Separator

root = Tk()
root.title("Speech to Text")

screetWidth = root.winfo_screenwidth()
screetHeight = root.winfo_screenheight()
w=400
h=200
x=(screetWidth-w)//2
y=(screetHeight-h)//2

root.geometry("%dx%d+%d+%d" % (w, h, x, y))
root.maxsize(800, 400)
root.minsize(200, 100)

root.configure(bg="white")

label1 = Label(root, text='speech to text', bg='yellow', font=('华文行楷', 20), fg='blue')
# label.grid(row=0, column=1)
label1.pack(anchor="nw")

sep=Separator(root, orient=HORIZONTAL)
sep.pack(fill=X, pady=10)

label2= Label(root, text='text', bg='grey', font=('微软雅黑', 15), fg='black',height=180, width=280,justify="left")
label2.pack(anchor="s")

# print(type(label1))  # 现在会正确显示 <class 'tkinter.Label'>


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



# $ virtualenv --python="/opt/homebrew/bin/python3.11" venv 
# $ source venv/bin/activate 
# $ pip install --upgrade pip 
# $ pip install customtkinter
# $ brew install python-tk


# douxiaobo@192 Whisper % brew install virtualenv
# ==> Auto-updating Homebrew...
# Adjust how often this is run with HOMEBREW_AUTO_UPDATE_SECS or disable with
# HOMEBREW_NO_AUTO_UPDATE. Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
# ^C==> Downloading https://formulae.brew.sh/api/formula.jws.json
# ==> Downloading https://formulae.brew.sh/api/formula_tap_migrations.jws.json
# ==> Downloading https://formulae.brew.sh/api/cask.jws.json
# ==> Downloading https://ghcr.io/v2/homebrew/core/virtualenv/manifests/20.34.0-1
# ######################################################################### 100.0%
# ==> Fetching virtualenv
# ==> Downloading https://ghcr.io/v2/homebrew/core/virtualenv/blobs/sha256:c8daa92
# ######################################################################### 100.0%
# ==> Pouring virtualenv--20.34.0.all.bottle.1.tar.gz
# 🍺  /opt/homebrew/Cellar/virtualenv/20.34.0: 181 files, 7.4MB
# ==> Running `brew cleanup virtualenv`...
# Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
# Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
# douxiaobo@192 Whisper % brew install virtualenv
# Warning: virtualenv 20.34.0 is already installed and up-to-date.
# To reinstall 20.34.0, run:
#   brew reinstall virtualenv
# douxiaobo@192 Whisper % virtualenv --python="/opt/homebrew/bin/python3.13" whisper
# created virtual environment CPython3.13.7.final.0-64 in 264ms
#   creator CPython3macOsBrew(dest=/Users/douxiaobo/Documents/Practice in Coding/Python/Whisper/whisper, clear=False, no_vcs_ignore=False, global=False)
#   seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=/Users/douxiaobo/Library/Application Support/virtualenv)
#     added seed packages: pip==25.2
#   activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
# douxiaobo@192 Whisper % source whisper/bin/activate
# (whisper) douxiaobo@192 Whisper % pip3 install --upgrade pip
# Requirement already satisfied: pip in ./whisper/lib/python3.13/site-packages (25.2)
# (whisper) douxiaobo@192 Whisper % pip install customtkinter
# Collecting customtkinter
#   Using cached customtkinter-5.2.2-py3-none-any.whl.metadata (677 bytes)
# Collecting darkdetect (from customtkinter)
#   Using cached darkdetect-0.8.0-py3-none-any.whl.metadata (3.6 kB)
# Collecting packaging (from customtkinter)
#   Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
# Using cached customtkinter-5.2.2-py3-none-any.whl (296 kB)
# Using cached darkdetect-0.8.0-py3-none-any.whl (9.0 kB)
# Using cached packaging-25.0-py3-none-any.whl (66 kB)
# Installing collected packages: packaging, darkdetect, customtkinter
# Successfully installed customtkinter-5.2.2 darkdetect-0.8.0 packaging-25.0
# (whisper) douxiaobo@192 Whisper % brew install python-tk 
# Warning: python-tk@3.13 3.13.7 is already installed and up-to-date.
# To reinstall 3.13.7, run:
#   brew reinstall python-tk@3.13



# /opt/homebrew/bin/python3.13 -m venv whisper1
# source whisper1/bin/activate