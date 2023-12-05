from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# AES encryption function
def encrypt_aes(key, data):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    return cipher.iv, ct_bytes

# AES decryption function
def decrypt_aes(key, iv, ct_bytes):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct_bytes), AES.block_size)
    return pt

# Example usage
key = get_random_bytes(16)  # 16 bytes key for AES-128
# data = b"Hello, AES encryption!"
data = input("Enter the text to be encrypted : ").encode('UTF-8')

iv, ciphertext = encrypt_aes(key, data)
print("AES Encrypted:", ciphertext.hex())

plaintext = decrypt_aes(key, iv, ciphertext)
print("AES Decrypted:", plaintext.decode('utf-8'))
