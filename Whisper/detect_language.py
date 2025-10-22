import whisper

def detect_language(audio_path):
    """
    检测音频中的语言
    """
    # 加载模型
    model = whisper.load_model("base")
    
    # 检测语言
    result = model.transcribe(audio_path)
    
    # 获取检测到的语言
    detected_language = result["language"]
    # confidence = getattr(result, 'language_probability', 'N/A')
    confidence = result.get('language_probability', 'N/A')
    text = result["text"]
    
    # 语言代码到名称的映射
    language_names = {
        'en': '英语', 'zh': '中文', 'ja': '日语', 'ko': '韩语',
        'fr': '法语', 'de': '德语', 'es': '西班牙语', 'it': '意大利语',
        'ru': '俄语', 'ar': '阿拉伯语', 'hi': '印地语', 'pt': '葡萄牙语'
    }
    
    language_name = language_names.get(detected_language, detected_language)
    
    print("=" * 50)
    print(f"📝 识别文本: {text}")
    print(f"🌍 检测语言: {language_name} ({detected_language})")
    if confidence != 'N/A':
        print(f"📊 置信度: {confidence:.2%}")
    print("=" * 50)

    # 在获取confidence后添加调试信息
    print("Result keys:", list(result.keys()))  # 查看result中包含的所有键

    # 或者更安全地处理置信度显示
    if isinstance(confidence, (int, float)):
        print(f"📊 置信度: {confidence:.2%}")
    else:
        print("📊 置信度: 未提供")

    
    return detected_language, text

# 使用示例
if __name__ == "__main__":
    audio_file = "output.wav"  # 替换为你的音频文件
    detect_language(audio_file)