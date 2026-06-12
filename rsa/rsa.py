from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import serialization,hashes

def generate_key():
    private_key=rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key=private_key.public_key()
    private_pem=private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    public_pem=public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    return private_pem,public_pem


def encrypt(public_pem,message):
    public_key=serialization.load_pem_public_key(public_pem)
    ciphertext=public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return ciphertext


def decrypt(private_pem,ciphertext):
    private_key=serialization.load_pem_private_key(private_pem,password=None,)
    plaintext=private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return plaintext.decode()


if __name__ == "__main__":
    private_pem,public_pem=generate_key()
    ciphertext=encrypt(public_pem,"hello,Microsoft!")
    print('ciphertext:',ciphertext)
    plaintext=decrypt(private_pem,ciphertext)
    print('plaintext:',plaintext)



# douxiaobo@192 rsa % python3 -m venv rsa
# douxiaobo@192 rsa % source rsa/bin/activate
# (rsa) douxiaobo@192 rsa % pip3 install cryptography
# Collecting cryptography
#   Downloading cryptography-48.0.1-cp311-abi3-macosx_10_9_universal2.whl.metadata (4.3 kB)
# Collecting cffi>=2.0.0 (from cryptography)
#   Using cached cffi-2.0.0-cp313-cp313-macosx_11_0_arm64.whl.metadata (2.6 kB)
# Collecting pycparser (from cffi>=2.0.0->cryptography)
#   Downloading pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
# Downloading cryptography-48.0.1-cp311-abi3-macosx_10_9_universal2.whl (8.0 MB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.0/8.0 MB 47.0 kB/s  0:02:47
# Using cached cffi-2.0.0-cp313-cp313-macosx_11_0_arm64.whl (181 kB)
# Downloading pycparser-3.0-py3-none-any.whl (48 kB)
# Installing collected packages: pycparser, cffi, cryptography
# Successfully installed cffi-2.0.0 cryptography-48.0.1 pycparser-3.0

# [notice] A new release of pip is available: 25.2 -> 26.1.2
# [notice] To update, run: pip install --upgrade pip
# (rsa) douxiaobo@192 rsa % 

# (rsa) douxiaobo@192 rsa % python3 rsa.py
# ciphertext: b'\x9e\xb0\xc3\x9f\x90\xc0\x10v\xaf9\xaf\xb0\x9f\x93\x01\r\x1d1\xe3\x84\xa69\xe8\xe6\xec\xbdG4\xb1\x0b\xd49\xa3\xc2\x88?\x11]\xcc\x90$\x90p\xf2\x8a;;\xa9\xbd\x86v\xd3\xcc\xaf7\x1d\xb0\x03\xd5\xda\xcc\x19\xa1b\tJ\xc3\xe6\xe9\x83\xa8[\xe4?\xdbk@\xefo\xb52B\x0c\xac\xdd\x96\xda\xdf\x05\x9f\x80\xa4\x02\x8aS\xea\x9a\x8a:\xcdQ\rk\xac\xc5\xa1\xc0#\x1d%R\xeeE\xde"2\n\xc8\xceD\x07e\xc3\xd3Br\xe0\xd9\xc3\xe9%\x1e\x95\xe40?WB\x1e\\\xa9\xea\xbc\xe4{\xeaY+\x8fs\x8e\xb6}\x0c\xf0\x1e\xa6\xd2\x19m\x88Y\x04\xc3\xab\xf0%(\x8a\xec\xd5\x1as\xe1A\x00\t-\x95\x1b\x9e\x9f`\x0c\xde\xc2\x19S\x19\xf7w2\x99\xbb\x96\x1f*\xe8\xc2\xc1\xd8\xfbv\x0c\x13\x10\xc8a\x86G\xbc]\xf0\xd7\x93\x16\x03]~\xff/\xe3!\x0c\xe2QrLk\x11\x0c\xc9j\x01J\x7f\xe9\xb6.nOaj}\xa3\n\x0f\x9d\x94:\x922\xfaK\xf5\x93'
# plaintext: hello,Microsoft!
# (rsa) douxiaobo@192 rsa % 
