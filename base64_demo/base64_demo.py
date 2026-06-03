import base64

data="黑暗跑团 为爱奔跑"

ciphertext=base64.b64encode(data.encode('utf-8'))
print(str(ciphertext))
      
plaintext=base64.b64decode(ciphertext)  
print(str(plaintext,'utf-8'))