from Crypto.Cipher import AES

import base64

# def encrypt(text):   # 加密
#     key='12345678901234567890123456789012'     #AES的密钥长度要求有16，24，32位
#     aes=AES.new(key.encode('utf-8'),AES.MODE_ECB)
#     text=text.encode('utf-8')
#     text=text+(16-len(text)%16)*chr(16-len(text)%16).encode('utf-8')
#     encrypt_text=aes.encrypt(text)
#     result=base64.b64encode(encrypt_text).decode('utf-8')
#     return result
# def decrypt(text):  # 解密
#     key='12345678901234567890123456789012'
#     aes=AES.new(key.encode('utf-8'),AES.MODE_ECB)
#     text=base64.b64decode(text.encode('utf-8'))
#     decrypt_text=aes.decrypt(text)
#     result=decrypt_text.decode('utf-8').rstrip(chr(decrypt_text[-1]))
#     return result

def encrypt(text):
    key = '12345678901234567890123456789012'
    aes = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    
    text_bytes = text.encode('utf-8')
    # 标准 PKCS7 填充
    padding_len = 16 - (len(text_bytes) % 16)
    text_padded = text_bytes + bytes([padding_len] * padding_len)
    
    encrypt_text = aes.encrypt(text_padded)
    return base64.b64encode(encrypt_text).decode('utf-8')

def decrypt(text):
    key = '12345678901234567890123456789012'
    aes = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    
    text_decoded = base64.b64decode(text.encode('utf-8'))
    decrypt_text = aes.decrypt(text_decoded)
    
    # 去除填充
    padding_len = decrypt_text[-1]
    return decrypt_text[:-padding_len].decode('utf-8')

if __name__ == '__main__':
    text='hello world'
    encrypt_text=encrypt(text)
    print(f'加密结果：{encrypt_text}')
    decrypt_text=decrypt(encrypt_text)
    print(f'解密结果：{decrypt_text}')








# 兼容性：pycryptodome 完美支持 Python 3.13 和 macOS ARM64 (M1/M2/M3) 架构。
# 安全性：pycrypto 已知存在多个安全漏洞，不应再用于任何生产或学习环境。
# 无缝切换：pycryptodome 使用相同的包名 Crypto，所以你的 from Crypto.Cipher import AES 无需更改。




# douxiaobo@192 AES % python3 -m venv aes
# douxiaobo@192 AES % source aes/bin/activate
# (aes) douxiaobo@192 AES % pip3 install pycrypto 
# Collecting pycrypto
#   Downloading pycrypto-2.6.1.tar.gz (446 kB)
#   Installing build dependencies ... done
#   Getting requirements to build wheel ... done
#   Preparing metadata (pyproject.toml) ... done
# Building wheels for collected packages: pycrypto
#   Building wheel for pycrypto (pyproject.toml) ... done
#   Created wheel for pycrypto: filename=pycrypto-2.6.1-cp313-cp313-macosx_15_0_arm64.whl size=473098 sha256=cc35a35dd68dee56780ae450b3683eda6fb1a1a82acb7c0413430eee0e400861
#   Stored in directory: /Users/douxiaobo/Library/Caches/pip/wheels/c7/ae/81/5c1908cbdf01335895e75ce933d098bfcc978a111e861f7b93
# Successfully built pycrypto
# Installing collected packages: pycrypto
# Successfully installed pycrypto-2.6.1

# [notice] A new release of pip is available: 25.2 -> 26.1.2
# [notice] To update, run: pip install --upgrade pip
# (aes) douxiaobo@192 AES % 

# (aes) douxiaobo@192 AES % pip uninstall pycrypto
# Found existing installation: pycrypto 2.6.1
# Uninstalling pycrypto-2.6.1:
#   Would remove:
#     /Users/douxiaobo/Documents/Practice in Coding/Python/AES/aes/lib/python3.13/site-packages/Crypto/*
#     /Users/douxiaobo/Documents/Practice in Coding/Python/AES/aes/lib/python3.13/site-packages/pycrypto-2.6.1.dist-info/*
# Proceed (Y/n)? y
#   Successfully uninstalled pycrypto-2.6.1
# (aes) douxiaobo@192 AES % pip3 install pycryptodome
# Collecting pycryptodome
#   Downloading pycryptodome-3.23.0-cp37-abi3-macosx_10_9_universal2.whl.metadata (3.4 kB)
# Downloading pycryptodome-3.23.0-cp37-abi3-macosx_10_9_universal2.whl (2.5 MB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 MB 32.2 kB/s  0:01:02
# Installing collected packages: pycryptodome
# Successfully installed pycryptodome-3.23.0

# [notice] A new release of pip is available: 25.2 -> 26.1.2
# [notice] To update, run: pip install --upgrade pip
# (aes) douxiaobo@192 AES % python3 aes_demo.py      
# 加密结果：0UBET6L5fwkwIhTkzd8nhg==
# 解密结果：hello world
# (aes) douxiaobo@192 AES % 
