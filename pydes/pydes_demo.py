import pyDes
import base64

data="Microsoft,Hello!微软，你好！"
des=pyDes.des(b"abcdefgh", pyDes.ECB, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
ciphertext=des.encrypt(data.encode('utf-8'))
print(ciphertext)
print(str(base64.b64encode(ciphertext), 'utf-8'))
plaintext=des.decrypt(ciphertext)
print(str(plaintext, 'utf-8'))


# douxiaobo@192 pydes % python3 -m venv pydes
# douxiaobo@192 pydes % source pydes/bin/activate
# (pydes) douxiaobo@192 pydes % pip3 install pyDes
# Collecting pyDes
#   Downloading pyDes-2.0.1.tar.gz (9.9 kB)
#   Installing build dependencies ... done
#   Getting requirements to build wheel ... done
#   Preparing metadata (pyproject.toml) ... done
# Building wheels for collected packages: pyDes
#   Building wheel for pyDes (pyproject.toml) ... done
#   Created wheel for pyDes: filename=pydes-2.0.1-py2.py3-none-any.whl size=9638 sha256=f2b4932fba01c9746adae9d4665eba383f8ce535801407b6d26213a917138c2b
#   Stored in directory: /Users/douxiaobo/Library/Caches/pip/wheels/aa/77/e5/0308929831f8d7954333810a935f36400df3274b18e1a2e6d6
# Successfully built pyDes
# Installing collected packages: pyDes
# Successfully installed pyDes-2.0.1

# [notice] A new release of pip is available: 25.2 -> 26.1.2
# [notice] To update, run: pip install --upgrade pip

# (pydes) douxiaobo@192 pydes % python3 pydes_demo.py
# b"L\x9e\xa6a80\xdc\xc3\x94\x9d\xddWF\x1b\xae5\x14K\x9b\x83D\x8f\xe8Z\x96\x81\xa80\xb8x\xdd\xc6\x0b0M'\xfb\x13\xffb"
# TJ6mYTgw3MOUnd1XRhuuNRRLm4NEj+haloGoMLh43cYLME0n+xP/Yg==
# Microsoft,Hello!微软，你好！
# (pydes) douxiaobo@192 pydes % 