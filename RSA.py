from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Generate RSA keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=1024
)

public_key = private_key.public_key()

# Serialize and save the keys (optional)
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Write private and public keys to files (optional)
# with open('private_key.pem', 'wb') as file:
#     file.write(private_pem)

# with open('public_key.pem', 'wb') as file:
#     file.write(public_pem)

# Encrypt and Decrypt example
# message = b"Hello, RSA encryption!"
message = input("Enter the text to be encrypted : ").encode('UTF-8')

# Encrypt the message with the public key
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decrypt the ciphertext with the private key
decrypted_message = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Original Message:", message.decode('utf-8'))
print("Encrypted text:", ciphertext.hex())
# print("Encrypted text:", ciphertext.decode('utf-8'))
print("Decrypted Message:", decrypted_message.decode('utf-8'))
