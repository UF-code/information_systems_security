# test
from base64 import b64decode, b64encode
from Crypto import Cipher
from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes

data = b"secret"
key = get_random_bytes(32)
print(b64encode(key))
cipher = AES.new(key, AES.MODE_CFB)
ct_bytes = cipher.encrypt(data)
iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')

iv_dec = b64decode(iv)
ct_dec = b64decode(ct)
cipher = AES.new(key, AES.MODE_CFB, iv= iv_dec)
pt = cipher.decrypt(ct_dec)
print(pt)


# soru 1
from base64 import b64decode
from Crypto.Cipher import AES 

data = b"p4psltayVQ7eTjVEfXVhJh2KMl3BCeHj8eJz7OvWjpNVLbwsqDeIp492KHNqlD54w/FTTFLIYxb4ABTEZfCj3r7uT4PDWWZMjhQ="
key = b'rnop3TnHwJ7P9zzLb0Z3qUjfhu1Cx9bW'
iv = b'YsiebTh0Sjr8dZKo'

iv_dec = iv
ct_dec = b64decode(data)
cipher = AES.new(key, AES.MODE_CFB, iv= iv_dec)
pt = cipher.decrypt(ct_dec)
print(pt)


# soru 2
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b"40YLp07vJIuR0TfMaNByWwXdtsp5YFy56MU37H8="
key = b'wEgDCNvhccofPTkFt9zUdDgZDIVdGC9L'
iv = b'crGTopEfBGXE1k1x'
print(b64decode(data))
print(b64decode(key))

iv_dec = iv
ct_dec = b64decode(data)
cipher = AES.new(key, AES.MODE_CFB, iv= iv_dec)
pt = cipher.decrypt(ct_dec)
print(pt)