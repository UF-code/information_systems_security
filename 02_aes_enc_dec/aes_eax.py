from Crypto.Cipher import AES 
from secrets import token_bytes


# from Crypto.Random import get_random_bytes
# key = get_random_bytes(32) # 32 bytes * 8 = 256 bits (1 byte = 8 bits)
# print(key)


key = token_bytes(16) # for AES-128
# key = token_bytes(24) # for AES-192
# key = token_bytes(32) # for AES-256

print(f'Key: {key}')

def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce 
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii')) # 
    return nonce, ciphertext, tag 

def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii') # 
    except ValueError:
        return False


nonce, ciphertext, tag = encrypt(input("Enter a message: "))
plaintext = decrypt(nonce, ciphertext, tag)

print(f'Cipher text: {ciphertext}')
if not plaintext:
    print('Message is corrupted')
else:
    print(f'Plain text: {plaintext}')



# print(token_bytes(16)) AES-128
# print(token_bytes(24)) AES-192
# print(token_bytes(32)) AES-256



# var MODE_ECB:	Electronic Code Book (ECB)
# var MODE_CBC:	Cipher-Block Chaining (CBC)
# var MODE_CFB:	Cipher FeedBack (CFB)
# var MODE_OFB:	Output FeedBack (OFB)
# var MODE_CTR:	CounTer Mode (CTR)
# var MODE_OPENPGP: OpenPGP Mode
# var MODE_CCM:	Counter with CBC-MAC (CCM) Mode
# var MODE_EAX:	EAX Mode
# var MODE_GCM:	Galois Counter Mode (GCM)
# var MODE_SIV:	Syntethic Initialization Vector (SIV)
# var MODE_OCB:	Offset Code Book (OCB)

