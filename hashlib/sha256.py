import hashlib
data='hello world'
sha=hashlib.sha256()
sha.update(data.encode('utf-8'))
result=sha.hexdigest()
print(result)

sha256_hash=hashlib.new('sha256')
sha256_hash.update(b'hello world')
print(sha256_hash.hexdigest())


sha256_hash1=hashlib.sha256()
sha256_hash1.update(b'hello ')
sha256_hash1.update(b'world')
print(sha256_hash1.hexdigest())