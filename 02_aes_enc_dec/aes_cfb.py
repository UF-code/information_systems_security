from base64 import b64decode, b64encode
from Crypto.Cipher import AES

def encryption(text, key, i_v):
    cipher = AES.new(key, AES.MODE_CFB, iv= i_v)
    ct_bytes = cipher.encrypt(text)
    cipher_text = b64encode(ct_bytes).decode('utf-8')
    
    print(f"Cipher Text: {cipher_text}")
    print(f"Key: {key}")
    print(f"Initial Vector: {i_v}")

encryption(b"Grup uyelerinin okul numaralarini virgul ile ayirarak G6 hucresine giriniz", b"rnop3TnHwJ7P9zzLb0Z3qUjfhu1Cx9bW", b"YsiebTh0Sjr8dZKo")
encryption(b"http://yaz.tf.firat.edu.tr/tr", b'wEgDCNvhccofPTkFt9zUdDgZDIVdGC9L', b'crGTopEfBGXE1k1x')


def decryption(cipher_text, key, i_v):
    cipher_text_decryption = b64decode(cipher_text)
    cipher = AES.new(key, AES.MODE_CFB, iv = i_v)
    plain_text = cipher.decrypt(cipher_text_decryption)

    print(f"Plain Text: {plain_text}")

decryption(b"p4psltayVQ7eTjVEfXVhJh2KMl3BCeHj8eJz7OvWjpNVLbwsqDeIp492KHNqlD54w/FTTFLIYxb4ABTEZfCj3r7uT4PDWWZMjhQ=", b'rnop3TnHwJ7P9zzLb0Z3qUjfhu1Cx9bW', b'YsiebTh0Sjr8dZKo')
decryption(b"40YLp07vJIuR0TfMaNByWwXdtsp5YFy56MU37H8=", b'wEgDCNvhccofPTkFt9zUdDgZDIVdGC9L', b'crGTopEfBGXE1k1x')
    
