import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# import tkinter as tk
from tkinter import *
from tkinter.ttk import Separator
import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile
import threading
import whisper
import numpy as np
class SpeechToTextApp:
    def __init__(self):
        self.recording=False
        self.audio_file=None
        self.fs=44100
        self.audio_data=None

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

        # 初始化StringVar用于动态更新文本
        self.label_text = StringVar()
        self.label_text.set("点击开始录音...")
        
        self.main_frame = Frame(self.root, bg="white")
        self.main_frame.pack(fill=BOTH, expand=True)

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

        # 使用StringVar关联的Label显示转录文本
        label_text = Label(bottom_frame, textvariable=self.label_text, bg='grey', font=('微软雅黑', 15), fg='black', justify="left")
        label_text.pack(fill=BOTH, expand=True, padx=3, pady=3)

    def chat_mode(self):
        if not self.recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        # 确保之前线程已经结束
        if hasattr(self, 'record_thread') and self.record_thread.is_alive():
            self.label_text.set("请等待当前录音结束...")
            return
        
        self.recording=True
        self.record_button.config(text='Recording...',bg="lightcoral")
        self.label_text.set("正在录音...")

        # 在新线程中开始录音，避免阻塞GUI
        self.record_thread = threading.Thread(target=self.record_audio)
        self.record_thread.daemon = True  # 设置为守护线程
        self.record_thread.start()

    def record_audio(self):
        # # 持续录音直到停止
        # self.audio_data = sd.rec(int(100 * self.fs), samplerate=self.fs, channels=1, dtype='int16')
        # sd.wait()
        # 开始录音并持续监听直到停止
        self.audio_buffer = []  # 用于存储录音数据
    
        # 音频数据回调函数
        # 当有新音频数据时被调用，将数据存入缓冲区
        def callback(indata, frames, time, status):
            if self.recording:
                self.audio_buffer.append(indata.copy())
    
        try:
            with sd.InputStream(samplerate=self.fs, channels=1, dtype='int16', callback=callback):
                while self.recording:
                    sd.sleep(100)  # 短暂休眠以减少CPU占用
        
            # 合并录音数据
            if self.audio_buffer:
                self.audio_data = np.concatenate(self.audio_buffer, axis=0)
            else:
                self.audio_data = np.array([], dtype='int16')  # 空数组作为默认值
        except Exception as e:
            print(f"录音过程中出现错误: {e}")
            self.audio_data = np.array([], dtype='int16')  # 出错时设置默认值

    def stop_recording(self):
        self.recording = False

        # 等待录音线程结束
        if hasattr(self, 'record_thread') and self.record_thread.is_alive():
            self.record_thread.join(timeout=2)  # 最多等待2秒

        self.record_button.config(text='Stop Recording',bg="lightblue")
        # temp_wav=tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        # temp_wav.write('output.wav', self.fs,self.audio_data)
        # temp_wav.close()

        
        # 检查是否有录音数据
        if self.audio_data is None or len(self.audio_data) == 0:
            self.label_text.set("没有录制到音频数据")
            return
        
        try:
            # 使用 scipy.io.wavfile.write 来保存音频数据
            wav.write('output.wav', self.fs, self.audio_data)
            print("Audio saved to output.wav")
            
            # 确认whisper模块是否正确导入
            if not hasattr(whisper, 'load_model'):
                print("Error: whisper module does not have load_model function")
                print("Please check your whisper installation")
                self.label_text.set("Whisper模型加载失败")
                return
            
            self.label_text.set("正在转录中...")  # 显示处理状态
            self.root.update()  # 强制更新界面

            whisper_model = whisper.load_model("small")
            result = whisper_model.transcribe(
                "output.wav",
                language="zh",
                task="transcribe",
                temperature=0.2,
                best_of=5,
                beam_size=5
            )
            # 注意：您还需要初始化self.label_text才能使用set()方法
            # self.label_text.set(result["text"])
            # 显示转录结果
            self.label_text.set(result["text"])
            print(f"Transcription result: {result['text']}")
        except ImportError as e:
            print(f"Failed to import whisper: {e}")
            self.label_text.set("导入Whisper失败")
        except Exception as e:
            print(f"Error during transcription: {e}")
            self.label_text.set("转录过程中出现错误")
    

    def run(self):
        try:
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.root.mainloop()
        except TclError as e:
            print(f"Tkinter error occurred: {e}")

    def on_closing(self):
        self.recording = False  # 确保停止录音
        # 如果有其他需要清理的资源在这里处理
        self.root.destroy()

if __name__ == "__main__":
    app = SpeechToTextApp()
    app.run()

# pip3 install openai-whisper