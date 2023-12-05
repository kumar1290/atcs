from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# Generate Alice's ECDH private key
alice_private_key = ec.generate_private_key(ec.SECP256R1())

# Serialize Alice's public key
alice_public_key = alice_private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Generate Bob's ECDH private key
bob_private_key = ec.generate_private_key(ec.SECP256R1())

# Serialize Bob's public key
bob_public_key = bob_private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Assume Alice sends her public key to Bob and vice versa (in a real-world scenario, this would be sent over an insecure channel)

# Deserialize Alice's public key from bytes
alice_received_public_key = serialization.load_pem_public_key(
    alice_public_key,
    backend=None  # Use the default backend
)

# Deserialize Bob's public key from bytes
bob_received_public_key = serialization.load_pem_public_key(
    bob_public_key,
    backend=None  # Use the default backend
)

# Alice computes the shared key using her private key and Bob's public key
alice_shared_key = alice_private_key.exchange(ec.ECDH(), bob_received_public_key)

# Bob computes the shared key using his private key and Alice's public key
bob_shared_key = bob_private_key.exchange(ec.ECDH(), alice_received_public_key)

# Ensure both parties have computed the same shared key
assert alice_shared_key == bob_shared_key

print("Shared Key:", alice_shared_key.hex())
