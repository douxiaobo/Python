from moviepy import VideoFileClip, vfx

clip=VideoFileClip("input.mp4")
mirrored_clip=clip.with_effects([vfx.MirrorX(), vfx.MirrorY()])
mirrored_clip.write_videofile("output.mp4")






# douxiaobo@192 mirror_video % code .
# douxiaobo@192 mirror_video % python3 -m venv moviepy
# douxiaobo@192 mirror_video % source moviepy/bin/activate
# (moviepy) douxiaobo@192 mirror_video %    