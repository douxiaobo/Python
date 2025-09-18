import sounddevice as sd
import scipy.io.wavfile as wav
import whisper
import numpy as np

def record_and_transcribe(duration=5):
    fs = 44100  # 采样率
    
    print("Say something!")
    # 录音
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    print("Recording finished")
    
    # 保存为 WAV 文件
    wav.write('output.wav', fs, audio)
    
    # 语音识别
    print("正在识别...")
    model = whisper.load_model("base")
    result = model.transcribe("output.wav", language="zh")
    
    print("识别结果:", result["text"])

# 使用示例
# record_and_transcribe(5)  # 录制5秒并识别

if __name__ == '__main__':
    record_and_transcribe(5)  # 录制5秒并识别


# (whisper) douxiaobo@192 Whisper % python3 stt2.py
# Say something!
# Recording finished
# 正在识别...
# /Users/douxiaobo/Documents/Practice in Coding/Python/Whisper/whisper/lib/python3.9/site-packages/whisper/transcribe.py:132: UserWarning: FP16 is not supported on CPU; using FP32 instead
#   warnings.warn("FP16 is not supported on CPU; using FP32 instead")
# 识别结果: Hannan, how did you do?
# (whisper) douxiaobo@192 Whisper % python3 stt2.py
# Say something!
# Recording finished
# 正在识别...
# /Users/douxiaobo/Documents/Practice in Coding/Python/Whisper/whisper/lib/python3.9/site-packages/whisper/transcribe.py:132: UserWarning: FP16 is not supported on CPU; using FP32 instead
#   warnings.warn("FP16 is not supported on CPU; using FP32 instead")
# 识别结果: 你好。 nice stuff!
# (whisper) douxiaobo@192 Whisper % python3 stt2.py 
# Say something!
# Recording finished
# 正在识别...
# /Users/douxiaobo/Documents/Practice in Coding/Python/Whisper/whisper/lib/python3.9/site-packages/whisper/transcribe.py:132: UserWarning: FP16 is not supported on CPU; using FP32 instead
#   warnings.warn("FP16 is not supported on CPU; using FP32 instead")
# 识别结果: 你好,你好吗?
# (whisper) douxiaobo@192 Whisper % 
