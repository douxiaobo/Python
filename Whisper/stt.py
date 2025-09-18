import whisper

model=whisper.load_model("base")
result=model.transcribe("output.wav",language="zh")
print(result["text"])


# 重新安装 llvmlite 和相关依赖
# bash
# # 卸载现有包
# pip uninstall llvmlite numba whisper torch

# # 重新安装
# pip install llvmlite
# pip install numba
# pip install torch torchvision torchaudio
# pip install openai-whisper


# (whisper) douxiaobo@192 Whisper % python3 stt.py  
# 100%|███████████████████████████████████████| 139M/139M [00:09<00:00, 15.2MiB/s]
# /Users/douxiaobo/Documents/Practice in Coding/Python/Whisper/whisper/lib/python3.9/site-packages/whisper/transcribe.py:132: UserWarning: FP16 is not supported on CPU; using FP32 instead
#   warnings.warn("FP16 is not supported on CPU; using FP32 instead")
# 女孩,本今欢迎你,欢迎你来到山海。谢谢你。
# (whisper) douxiaobo@192 Whisper % 

# 下载进度条：100%|███████████████████████████████████████| 139M/139M [00:09<00:00, 15.2MiB/s]

# 这表示 Whisper 模型正在下载，大小约为 139MB，下载完成需要约 9 秒钟
# 警告信息：UserWarning: FP16 is not supported on CPU; using FP32 instead

# 这是一个正常的警告，表示在 CPU 上不支持 FP16 精度计算，所以自动使用 FP32 精度
# 这在 Mac 或普通 PC 上是正常的，只有在支持的 GPU 上才能使用 FP16
# 识别结果：女孩,本今欢迎你,欢迎你来到山海。谢谢你。

# 这是语音识别的结果，将音频中的语音转换为了中文文本