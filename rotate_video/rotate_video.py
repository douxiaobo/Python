from moviepy import VideoFileClip, vfx

clip = VideoFileClip("test.mp4")
rotated_clip = clip.with_effects([vfx.Rotate(90)])
rotated_clip.write_videofile("rotated_video.mp4")


# Last login: Wed Jul  8 15:29:16 on console
# douxiaobo@192 rotate_video % code .
# douxiaobo@192 rotate_video % python3 -m venv moviepy
# douxiaobo@192 rotate_video % source moviepy/bin/activate
# (moviepy) douxiaobo@192 rotate_video % pip3 install moviepy
# Collecting moviepy
#   Using cached moviepy-2.2.1-py3-none-any.whl.metadata (6.9 kB)
# Collecting decorator<6.0,>=4.0.2 (from moviepy)
#   Downloading decorator-5.3.1-py3-none-any.whl.metadata (3.9 kB)
# Collecting imageio<3.0,>=2.5 (from moviepy)
#   Downloading imageio-2.37.3-py3-none-any.whl.metadata (9.7 kB)
# Collecting imageio_ffmpeg>=0.2.0 (from moviepy)
#   Using cached imageio_ffmpeg-0.6.0-py3-none-macosx_11_0_arm64.whl.metadata (1.5 kB)
# Collecting numpy>=1.25.0 (from moviepy)
#   Downloading numpy-2.5.1-cp313-cp313-macosx_14_0_arm64.whl.metadata (6.6 kB)
# Collecting proglog<=1.0.0 (from moviepy)
#   Using cached proglog-0.1.12-py3-none-any.whl.metadata (794 bytes)
# Collecting python-dotenv>=0.10 (from moviepy)
#   Using cached python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
# Collecting pillow<12.0,>=9.2.0 (from moviepy)
#   Using cached pillow-11.3.0-cp313-cp313-macosx_11_0_arm64.whl.metadata (9.0 kB)
# Collecting tqdm (from proglog<=1.0.0->moviepy)
#   Downloading tqdm-4.68.4-py3-none-any.whl.metadata (57 kB)
# Using cached moviepy-2.2.1-py3-none-any.whl (129 kB)
# Downloading decorator-5.3.1-py3-none-any.whl (10 kB)
# Downloading imageio-2.37.3-py3-none-any.whl (317 kB)
# Using cached pillow-11.3.0-cp313-cp313-macosx_11_0_arm64.whl (4.7 MB)
# Using cached proglog-0.1.12-py3-none-any.whl (6.3 kB)
# Using cached imageio_ffmpeg-0.6.0-py3-none-macosx_11_0_arm64.whl (21.1 MB)
# Downloading numpy-2.5.1-cp313-cp313-macosx_14_0_arm64.whl (5.3 MB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.3/5.3 MB 158.6 kB/s  0:00:33
# Using cached python_dotenv-1.2.2-py3-none-any.whl (22 kB)
# Downloading tqdm-4.68.4-py3-none-any.whl (676 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 676.6/676.6 kB 221.0 kB/s  0:00:03
# Installing collected packages: tqdm, python-dotenv, pillow, numpy, imageio_ffmpeg, decorator, proglog, imageio, moviepy
# Successfully installed decorator-5.3.1 imageio-2.37.3 imageio_ffmpeg-0.6.0 moviepy-2.2.1 numpy-2.5.1 pillow-11.3.0 proglog-0.1.12 python-dotenv-1.2.2 tqdm-4.68.4

# [notice] A new release of pip is available: 25.2 -> 26.1.2
# [notice] To update, run: pip install --upgrade pip
# (moviepy) douxiaobo@192 rotate_video % 

# (moviepy) douxiaobo@192 rotate_video % python3 rotate_video.py
# MoviePy - Building video rotated_video.mp4.
# MoviePy - Writing audio in rotated_videoTEMP_MPY_wvf_snd.mp3
# MoviePy - Done.                                                                
# MoviePy - Writing video rotated_video.mp4

# MoviePy - Done !                                                               
# MoviePy - video ready rotated_video.mp4
# (moviepy) douxiaobo@192 rotate_video % 

