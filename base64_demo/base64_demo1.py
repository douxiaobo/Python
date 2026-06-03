import base64

orriginal_string = "黑暗跑团 为爱奔跑"

encoded_bytes = base64.b64encode(orriginal_string.encode('utf-8')).decode('utf-8')
print(f"Encoded string is {encoded_bytes}")

stripped_edcoded=encoded_bytes.rstrip('=')
print(f"Stripped encoded string is {stripped_edcoded}")

padding=4-(len(stripped_edcoded)%4)
if padding != 4:
    stripped_edcoded += '='*padding

decoded_bytes=base64.b64decode(stripped_edcoded)
decoded_string=decoded_bytes.decode('utf-8')
print(f"Decoded string is {decoded_string}")


## 暂时不写图片和文件流的base64编码