from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
# 加载无声视频和有声音频文件
video = VideoFileClip("Fran_is_hungry_-_The_London_to_1080p_1761030248437.1.mp4")
audio = AudioFileClip("Fran_is_hungry_-_The_London_to_1080p_1761030248437.mp4")

# 将音频设置给视频
final_video = video.with_audio(audio)

# 输出最终文件
final_video.write_videofile(
    "Fran_is_hungry_-_The_London_to_1080p_1761030248437_final.mp4",
    codec='libx264',  # 通用视频编码器
    audio_codec='aac' # 音频编码器
)

# 释放资源（重要，避免内存泄漏）
video.close()
audio.close()
final_video.close()

# pip install moviepy