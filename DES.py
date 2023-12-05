from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# DES encryption function
def encrypt_des(key, data):
    cipher = DES.new(key, DES.MODE_ECB)
    ct_bytes = cipher.encrypt(pad(data, DES.block_size))
    return ct_bytes

# DES decryption function
def decrypt_des(key, ct_bytes):
    cipher = DES.new(key, DES.MODE_ECB)
    pt = unpad(cipher.decrypt(ct_bytes), DES.block_size)
    return pt

# Example usage
key = get_random_bytes(8) 
data = input("Enter the text to be encrypted : ").encode('UTF-8')

ciphertext = encrypt_des(key, data)
print("DES Encrypted:", ciphertext.hex())

plaintext = decrypt_des(key, ciphertext)
print("DES Decrypted:", plaintext.decode('utf-8'))
