import sounddevice as sd
import scipy.io.wavfile as wav
import tkinter as tk
from tkinter import messagebox
import tempfile
import threading

class VoiceRecorder:
    def __init__(self):
        self.recording = False
        self.audio_data = None
        self.fs = 44100  # sampling rate
        
        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("语音录音器")
        self.root.geometry("300x150")
        
        # 创建按钮
        self.record_button = tk.Button(
            self.root, 
            text="开始录音", 
            command=self.toggle_recording,
            height=2,
            width=15,
            bg="lightblue"
        )
        self.record_button.pack(pady=30)
        
    def toggle_recording(self):
        if not self.recording:
            # 开始录音
            self.start_recording()
        else:
            # 停止录音
            self.stop_recording()
    
    def start_recording(self):
        self.recording = True
        self.record_button.config(text="停止录音", bg="lightcoral")
        
        # 在新线程中开始录音，避免阻塞GUI
        self.record_thread = threading.Thread(target=self.record_audio)
        self.record_thread.start()
        
        messagebox.showinfo("录音开始", "录音已开始，请讲话...")
    
    def record_audio(self):
        # 持续录音直到停止
        self.audio_data = sd.rec(int(100 * self.fs), samplerate=self.fs, channels=1, dtype='int16')
        sd.wait()
    
    def stop_recording(self):
        self.recording = False
        self.record_button.config(text="开始录音", bg="lightblue")
        
        # 保存录音文件
        temp_wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        wav.write('output.wav', self.fs, self.audio_data)
        temp_wav.close()
        
        messagebox.showinfo("录音结束", "录音已完成，已保存为output.wav")
        
    def run(self):
        self.root.mainloop()

# 运行应用
if __name__ == "__main__":
    app = VoiceRecorder()
    app.run()




# 设置环境变量临时屏蔽警告
# 在运行程序前设置环境变量：

# bash
# export TK_SILENCE_DEPRECATION=1
# python3 voice1.py
# 或者直接在命令行中运行：

# bash
# TK_SILENCE_DEPRECATION=1 python3 voice1.py