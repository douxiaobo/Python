import whisper
import pyaudio
import numpy as np
import wave
import time

class LanguageDetector:
    def __init__(self, model_size="base"):
        self.model = whisper.load_model(model_size)
        
    def record_audio(self, filename, duration=5):
        """录制音频"""
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        
        p = pyaudio.PyAudio()
        
        stream = p.open(format=FORMAT,
                       channels=CHANNELS,
                       rate=RATE,
                       input=True,
                       frames_per_buffer=CHUNK)
        
        print("🎤 开始录音... 请说话")
        frames = []
        
        for i in range(0, int(RATE / CHUNK * duration)):
            data = stream.read(CHUNK)
            frames.append(data)
        
        print("⏹️ 录音结束")
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        # 保存文件
        wf = wave.open(filename, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        
        return filename
    
    def detect_language_detailed(self, audio_path):
        """详细语言检测"""
        # 使用Whisper的detect_language功能
        audio = whisper.load_audio(audio_path)
        audio = whisper.pad_or_trim(audio)
        
        # 制作log-Mel频谱图
        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
        
        # 检测语言
        _, probs = self.model.detect_language(mel)
        
        # 获取概率最高的前5种语言
        top_languages = sorted(probs.items(), key=lambda x: x[1], reverse=True)[:5]
        
        # 语言代码映射
        language_map = {
            'en': '英语 English', 'zh': '中文 Chinese', 'ja': '日语 Japanese',
            'ko': '韩语 Korean', 'fr': '法语 French', 'de': '德语 German',
            'es': '西班牙语 Spanish', 'it': '意大利语 Italian', 
            'ru': '俄语 Russian', 'ar': '阿拉伯语 Arabic',
            'hi': '印地语 Hindi', 'pt': '葡萄牙语 Portuguese',
            'vi': '越南语 Vietnamese', 'th': '泰语 Thai',
            'nl': '荷兰语 Dutch', 'tr': '土耳其语 Turkish'
        }
        
        print("🔍 语言检测结果:")
        print("-" * 40)
        for lang_code, prob in top_languages:
            lang_name = language_map.get(lang_code, lang_code)
            print(f"📍 {lang_name}: {prob:.2%}")
        
        # 完整转录
        result = self.model.transcribe(audio_path)
        print(f"\n📝 转录文本: {result['text']}")
        
        return top_languages[0][0], result["text"]

# 使用示例
def main():
    detector = LanguageDetector("base")
    
    while True:
        input("按回车键开始录音（5秒），或 Ctrl+C 退出...")
        
        audio_file = "output.wav"
        
        # 录制音频
        detector.record_audio(audio_file, duration=5)
        
        # 检测语言
        main_language, text = detector.detect_language_detailed(audio_file)
        
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()