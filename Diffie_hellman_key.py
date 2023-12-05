from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Generate Diffie-Hellman parameters
parameters = dh.generate_parameters(generator=2, key_size=512)

# Generate Alice's private and public keys
alice_private_key = parameters.generate_private_key()
alice_public_key = alice_private_key.public_key()

# Serialize Alice's private key and public key
alice_private_key_bytes = alice_private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

alice_public_key_bytes = alice_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Generate Bob's private and public keys
bob_private_key = parameters.generate_private_key()
bob_public_key = bob_private_key.public_key()

# Serialize Bob's private key and public key
bob_private_key_bytes = bob_private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

bob_public_key_bytes = bob_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print("Alice's Private Key:\n", alice_private_key_bytes.decode())
print("Alice's Public Key:\n", alice_public_key_bytes.decode())
print("Bob's Private Key:\n", bob_private_key_bytes.decode())
print("Bob's Public Key:\n", bob_public_key_bytes.decode())

# Alice sends her public key to Bob (in a real-world scenario, this would be sent over an insecure channel)
alice_shared_key = alice_private_key.exchange(bob_public_key)
bob_received_public_key = serialization.load_pem_public_key(
    alice_public_key_bytes,
    backend=None  # Use the default backend
)

# Bob sends his public key to Alice (in a real-world scenario, this would be sent over an insecure channel)
bob_shared_key = bob_private_key.exchange(alice_public_key)
alice_received_public_key = serialization.load_pem_public_key(
    bob_public_key_bytes,
    backend=None  # Use the default backend
)

# Ensure both parties have computed the same shared key
assert alice_shared_key == bob_shared_key

print("\nShared Key:", alice_shared_key.hex())
