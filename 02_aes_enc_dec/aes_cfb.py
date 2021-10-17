from base64 import b64decode, b64encode
from Crypto.Cipher import AES
import sys 

def encryption(text, key, i_v):
    cipher = AES.new(key, AES.MODE_CFB, iv= i_v)
    ct_bytes = cipher.encrypt(text)
    cipher_text = b64encode(ct_bytes).decode('utf-8')
    
    print(f"Cipher Text: {cipher_text}")
    print(f"Key: {key}")
    print(f"Initial Vector: {i_v}")

def decryption(cipher_text, key, i_v):
    cipher_text_decryption = b64decode(cipher_text)
    cipher = AES.new(key, AES.MODE_CFB, iv = i_v)
    plain_text = cipher.decrypt(cipher_text_decryption)

    print(f"Plain Text: {plain_text}")

if __name__ == "__main__":
    # if system argument is "enc" Encryption & if you wanna chose decryption you have to specify system arg as 'dec'
    decryption(input('Cipher Text: ').encode('utf-8'), input('Key: ').encode('utf-8'), input('Initial Vector: ').encode('utf-8')) if sys.argv[1] == 'dec' else encryption(input('Text: ').encode('utf-8'), input('Key: ').encode('utf-8'), input('Initial Vector: ').encode('utf-8')) 

# First Encryption Test
# Text: Grup uyelerinin okul numaralarini virgul ile ayirarak G6 hucresine giriniz
# Key: rnop3TnHwJ7P9zzLb0Z3qUjfhu1Cx9bW
# Initial Vector: YsiebTh0Sjr8dZKo

# First Decryption Test
# Cipher Text: p4psltayVQ7eTjVEfXVhJh2KMl3BCeHj8eJz7OvWjpNVLbwsqDeIp492KHNqlD54w/FTTFLIYxb4ABTEZfCj3r7uT4PDWWZMjhQ=
# Key: rnop3TnHwJ7P9zzLb0Z3qUjfhu1Cx9bW
# Initial Vector: YsiebTh0Sjr8dZKo



# Second Encryption Test
# Text: http://yaz.tf.firat.edu.tr/tr
# Key: wEgDCNvhccofPTkFt9zUdDgZDIVdGC9L
# Initial Vector: crGTopEfBGXE1k1x

# Second Decryption Test
# Cipher Text: 40YLp07vJIuR0TfMaNByWwXdtsp5YFy56MU37H8=
# Key: wEgDCNvhccofPTkFt9zUdDgZDIVdGC9L
# Initial Vector: crGTopEfBGXE1k1x
