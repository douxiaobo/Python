import whisper

# 使用更大的模型以提高准确率（但需要更多内存和处理时间）
model = whisper.load_model("small")  # 或 "medium", "large"

# 添加更多参数来优化识别
result = model.transcribe(
    "output.wav",
    language="zh",
    task="transcribe",  # 或 "translate" 来翻译为英文
    temperature=0.2,    # 调整温度参数
    best_of=5,          # 生成候选项数量
    beam_size=5         # 搜索束大小
)

print("识别文本:", result["text"])
print("识别语言:", result["language"])
print("置信度:", result["avg_logprob"])


# (whisper) douxiaobo@192 Whisper % python3 stt1.py
# 100%|███████████████████████████████████████| 461M/461M [00:32<00:00, 15.0MiB/s]
# /Users/douxiaobo/Documents/Practice in Coding/Python/Whisper/whisper/lib/python3.9/site-packages/whisper/transcribe.py:132: UserWarning: FP16 is not supported on CPU; using FP32 instead
#   warnings.warn("FP16 is not supported on CPU; using FP32 instead")
# 识别文本: 你好,本金欢迎你,欢迎你来到上海。谢谢你。请点赞,订阅,转发,打赏,打赏,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点�点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点赞,点
# 识别语言: zh
# Traceback (most recent call last):
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/Whisper/stt1.py", line 18, in <module>
#     print("置信度:", result["avg_logprob"])
# KeyError: 'avg_logprob'
# (whisper) douxiaobo@192 Whisper % 
