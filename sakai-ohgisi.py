from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, GT
from charm.schemes.ibenc.ibenc_sok05 import SOK05
from charm.schemes.ibenc.ibenc_bb04 import BB04

# Initialize the pairing group
group = PairingGroup('SS512')

# Create a SOK05 instance for IBE
ibe = SOK05(group)
(mpk, msk) = ibe.setup()

# Generate a secret key for the user
user_id = "alice@example.com"
sk = ibe.extract(mpk, msk, user_id)

# Encrypt a message for the user
message = "Hello, Alice!"
ct = ibe.encrypt(mpk, message, user_id)

# Decrypt the ciphertext using the user's secret key
decrypted_message = ibe.decrypt(mpk, sk, ct)
print("Decrypted Message:", decrypted_message)

# Create a SOK05 instance for IBS
ibs = SOK05(group)
mpk_ibs, msk_ibs = ibs.setup()

# Generate a secret key for signing
user_id_sign = "bob@example.com"
sk_sign = ibs.extract(mpk_ibs, msk_ibs, user_id_sign)

# Sign a message using the secret key
message_to_sign = "This message is signed by Bob."
signature = ibs.sign(mpk_ibs, sk_sign, message_to_sign)

# Verify the signature
verified = ibs.verify(mpk_ibs, message_to_sign, signature)
print("Signature Verification:", verified)
