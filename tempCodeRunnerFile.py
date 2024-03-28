context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
conn = HTTPSConnection("https://fanyi.baidu.com", context=context)