import hashlib
data='hello world'      # 单引号和双引号没有区别
md=hashlib.md5()
md.update(data.encode('utf-8'))
result=md.hexdigest()
print(result)

md5_hash=hashlib.md5(b'hello world')
print(md5_hash.hexdigest())