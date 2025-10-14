import os
import platform
import subprocess
def open_folder(path):
    # check os system
    if platform.system() == 'Windows':
        os.startfile(path)
    elif platform.system() == 'Darwin':
        subprocess.Popen(['open', path])
    else:
        subprocess.Popen(['xdg-open', path])

open_folder('/Users/douxiaobo/Documents/Practice in Coding/Python')