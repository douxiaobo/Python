import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# import tkinter as tk
from tkinter import *
from tkinter.ttk import Separator
import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile
import threading

class SpeechToTextApp:
    def __init__(self):
        self.recording=False
        self.audio_file=None
        self.fs=44100

        self.root = Tk()
        self.root.title("Speech to Text")
        self.screetWidth = self.root.winfo_screenwidth()
        self.screetHeight = self.root.winfo_screenheight()
        self.w=400
        self.h=200
        self.x=(self.screetWidth-self.w)//2
        self.y=(self.screetHeight-self.h)//2
        self.root.geometry("%dx%d+%d+%d" % (self.w, self.h, self.x, self.y))
        self.root.maxsize(800, 400)
        self.root.minsize(200, 100)
        self.root.configure(bg="white")
        
        self.main_frame = Frame(self.root, bg="white")
        self.main_frame.pack(fill=BOTH, expand=True)

        self.label2=None
        self.frame()

    def frame(self):
        # 创建主框架来更好地控制布局
        main_frame = Frame(self.root, bg="white")
        main_frame.pack(fill=BOTH, expand=True)

        # 上方框架（占总高度的10%）
        top_frame = Frame(main_frame, bg="white")
        top_frame.pack(fill=X, side=TOP)

        # 使用grid布局管理器放置label1和button
        label1 = Label(top_frame, text='speech to text', bg='yellow', font=('华文行楷', 20), fg='blue')
        label1.grid(row=0, column=0, sticky=W+E, padx=3, pady=3)

        self.record_button = Button(top_frame, text='Start', command=self.chat_mode, bg='green',highlightbackground='blue', fg='red', font=('微软雅黑', 15))
        self.record_button.grid(row=0, column=1, sticky=W+E, padx=3, pady=3)

        # 配置列权重，使两个组件各占一半宽度
        top_frame.columnconfigure(0, weight=1)
        top_frame.columnconfigure(1, weight=1)

        # 分隔符
        sep = Separator(main_frame, orient=HORIZONTAL)
        sep.pack(fill=X, pady=3)

        # 下方框架（占总高度的90%）
        bottom_frame = Frame(main_frame, bg="white")
        bottom_frame.pack(fill=BOTH, expand=True)

        label2 = Label(bottom_frame, text='text', bg='grey', font=('微软雅黑', 15), fg='black', justify="left")
        label2.pack(fill=BOTH, expand=True, padx=3, pady=3)
    def chat_mode(self):
        if not self.recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        self.recording=True
        self.record_button.config(text='Recording...',bg="lightcoral")

        # 在新线程中开始录音，避免阻塞GUI
        self.record_thread = threading.Thread(target=self.record_audio)
        self.record_thread.start()

    def record_audio(self):
        # 持续录音直到停止
        self.audio_data = sd.rec(int(100 * self.fs), samplerate=self.fs, channels=1, dtype='int16')
        sd.wait()

    def stop_recording(self):
        self.recording = False
        self.record_button.config(text='Stop Recording',bg="lightblue")
        # temp_wav=tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        # temp_wav.write('output.wav', self.fs,self.audio_data)
        # temp_wav.close()

        # 使用 scipy.io.wavfile.write 来保存音频数据
        wav.write('output.wav', self.fs, self.audio_data)
        print("Audio saved to output.wav")

    def run(self):
        try:
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.root.mainloop()
        except TclError as e:
            print(f"Tkinter error occurred: {e}")

    def on_closing(self):
        self.root.destroy()

if __name__ == "__main__":
    app = SpeechToTextApp()
    app.run()

# (whisper) douxiaobo@192 Whisper % python stt_tkinter.py
# (whisper) douxiaobo@192 Whisper % git add .
# (whisper) douxiaobo@192 Whisper % git commit -m "stt_tkinter.py"
# [main 0f2b9ed7] stt_tkinter.py
#  2 files changed, 94 insertions(+), 55 deletions(-)
# (whisper) douxiaobo@192 Whisper % git push orign main
# fatal: 'orign' does not appear to be a git repository
# fatal: Could not read from remote repository.

# Please make sure you have the correct access rights
# and the repository exists.
# (whisper) douxiaobo@192 Whisper % git push origin main
# Enumerating objects: 9, done.
# Counting objects: 100% (9/9), done.
# Delta compression using up to 14 threads
# Compressing objects: 100% (5/5), done.
# Writing objects: 100% (5/5), 1.27 KiB | 1.27 MiB/s, done.
# Total 5 (delta 4), reused 0 (delta 0), pack-reused 0 (from 0)
# remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
# To github.com:douxiaobo/Python.git
#    17100406..0f2b9ed7  main -> main
# (whisper) douxiaobo@192 Whisper % 
