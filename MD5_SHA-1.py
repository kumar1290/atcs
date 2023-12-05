import hashlib

def get_md5(message):
    # Create an MD5 hash object
    md5 = hashlib.md5()
    # Update the hash object with the message
    md5.update(message.encode('utf-8'))
    # Get the hexadecimal representation of the hash
    md5_digest = md5.hexdigest()
    return md5_digest

def get_sha1(message):
    # Create a SHA-1 hash object
    sha1 = hashlib.sha1()
    # Update the hash object with the message
    sha1.update(message.encode('utf-8'))
    # Get the hexadecimal representation of the hash
    sha1_digest = sha1.hexdigest()
    return sha1_digest

# Example message
message = input("Enter the message : ")

# Get MD5 hash of the message
md5_hash = get_md5(message)
print(f"MD5 Hash of the message: {md5_hash}")

# Get SHA-1 hash of the message
sha1_hash = get_sha1(message)
print(f"SHA-1 Hash of the message: {sha1_hash}")
