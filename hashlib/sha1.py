import hashlib

sha1_hash = hashlib.sha1(b'hello world')
print(sha1_hash.hexdigest())