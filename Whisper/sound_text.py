import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import whisper
import sounddevice as sd
import numpy as np
import os
import tempfile
import scipy.io.wavfile
import requests
import pyttsx3
import threading
def record_audio(duration=5, fs=16000):
    print("🎙️ 正在录音...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    print("✅ 录音完成！")
    temp_wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    scipy.io.wavfile.write(temp_wav.name, fs, audio)
    return temp_wav.name
def speech_to_text(audio_path, model_name='base'):
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path, language='zh')
    return result['text']
def ask_deepseek(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "deepseek-r1-7b",
        "prompt": prompt,
        "stream": False
    }
    res = requests.post(url, json=data)
    return res.json()['response']
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)  # 语速
    engine.setProperty('voice', 'zh')  # 语言（macOS/Windows 自动识别）
    engine.say(text)
    engine.runAndWait()
def update_gui_audio():
    audio_file = record_audio(duration=5)
    question = speech_to_text(audio_file)
    response = ask_deepseek(question)
    text_output_audio.delete(1.0, tk.END)  # 清空文本框
    text_output_audio.insert(tk.END, f"录音识别的文字: {question}\n\n")
    text_output_audio.insert(tk.END, f"DeepSeek 回答: {response}\n")
    speak(response)
def update_gui_text():
    prompt = text_input.get("1.0", tk.END).strip()
    if prompt == "":
        messagebox.showwarning("警告", "请输入问题！")
        return
    response = ask_deepseek(prompt)
    text_output_text.delete(1.0, tk.END)  # 清空文本框
    text_output_text.insert(tk.END, f"你问的问题: {prompt}\n\n")
    text_output_text.insert(tk.END, f"DeepSeek 回答: {response}\n")
    speak(response)
def set_background_image(root):
    background_image = Image.open("但行好事，莫问前程.png")  # 设置本地图片路径
    background_image = background_image.resize((800, 600), Image.Resampling.LANCZOS)  # 调整图片大小适应界面
    background_image = ImageTk.PhotoImage(background_image)  # 转换为Tkinter可用的图片格式
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)  # 让背景填满整个窗口
    background_label.image = background_image  # 保持对图片的引用
def create_gui():
    global root, text_input, text_output_audio, text_output_text
    root = tk.Tk()
    root.title("语音交互系统")
    root.geometry("800x600")
    set_background_image(root)
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="菜单", menu=help_menu)
    help_menu.add_command(label="About", command=show_about)
    help_menu.add_command(label="Exit", command=root.quit)
    notebook = ttk.Notebook(root)
    notebook.pack(padx=10, pady=10, expand=True)
    audio_tab = ttk.Frame(notebook)
    notebook.add(audio_tab, text="语音识别")
    text_output_audio = tk.Text(audio_tab, wrap=tk.WORD, width=70, height=15)
    text_output_audio.pack(padx=10, pady=10)
    button_audio = tk.Button(audio_tab, text="开始录音并获取回答",
                             command=lambda: threading.Thread(target=update_gui_audio).start(), width=25)
    button_audio.pack(pady=10)
    text_tab = ttk.Frame(notebook)
    notebook.add(text_tab, text="直接提问")
    text_input = tk.Text(text_tab, height=3, width=60)
    text_input.pack(padx=10, pady=10)
    text_output_text = tk.Text(text_tab, wrap=tk.WORD, width=70, height=15)
    text_output_text.pack(padx=10, pady=10)
    button_text = tk.Button(text_tab, text="提交问题并获取回答", command=update_gui_text, width=25)
    button_text.pack(pady=10)
    root.mainloop()
def show_about():
    messagebox.showinfo("关于", "语音交互系统\n版本：1.0\n开发者：Zayden Wang")
if __name__ == "__main__":
    os.environ["PATH"] += os.pathsep + r"E:\softwares\ffmpeg-7.0.2-essentials_build\bin"
    create_gui()




# (whisper) douxiaobo@192 Whisper % pip3 install PIL
# ERROR: Could not find a version that satisfies the requirement PIL (from versions: none)
# ERROR: No matching distribution found for PIL
# (whisper) douxiaobo@192 Whisper % pip3 install pillow
# Collecting pillow
#   Downloading pillow-11.3.0-cp39-cp39-macosx_11_0_arm64.whl.metadata (9.0 kB)
# Downloading pillow-11.3.0-cp39-cp39-macosx_11_0_arm64.whl (4.7 MB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.7/4.7 MB 8.4 MB/s  0:00:00
# Installing collected packages: pillow
# Successfully installed pillow-11.3.0

# 你遇到的错误是因为 PIL 已经不再以原始名称发布。现在应该安装的是 Pillow，它是 PIL（Python Imaging Library）的一个活跃分支。

# 你可以通过以下命令来安装 Pillow：

# bash
# pip3 install Pillow
# 在你的代码中，你已经正确地使用了 from PIL import Image，这表明你只需要安装 Pillow 包即可。

# 如果你之前尝试过安装 PIL 并且失败了，那么现在只需要运行上面的命令就可以解决问题。Pillow 是与 PIL 兼容的，并且提供了更多的功能和修复。