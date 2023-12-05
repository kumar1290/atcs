from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.exceptions import InvalidSignature

def generate_key():
    # Generate ECDSA private key using the SECP256R1 curve
    private_key = ec.generate_private_key(ec.SECP256R1())
    return private_key

def sign_message(private_key, message):
    # Sign the message using the private key
    signature = private_key.sign(
        message.encode('utf-8'),
        ec.ECDSA(hashes.SHA256())
    )
    return signature

def verify_signature(public_key, message, signature):
    # Verify the signature using the public key
    try:
        public_key.verify(
            signature,
            message.encode('utf-8'),
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except InvalidSignature:
        return False

# Generate ECDSA key pair
private_key = generate_key()
public_key = private_key.public_key()

# Example message to sign and verify
message = "This is a test message for ECDSA."

# Sign the message using the private key
signature = sign_message(private_key, message)
print("Message Signature:", signature.hex())

# Verify the signature using the public key
verification_result = verify_signature(public_key, message, signature)
if verification_result:
    print("Signature Verification: Valid")
else:
    print("Signature Verification: Invalid")
