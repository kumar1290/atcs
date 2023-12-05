def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_unicode = ord(char) - shift
            if char.islower():
                if shifted_unicode < ord('a'):
                    shifted_unicode += 26
            else:
                if shifted_unicode < ord('A'):
                    shifted_unicode += 26
            decrypted_text += chr(shifted_unicode)
        else:
            decrypted_text += char
    return decrypted_text

def break_shift_cipher(ciphertext):
    for shift in range(1, 26):  # Try all possible shift values
        decrypted = decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted}")

# Example ciphertext to break
ciphertext = "Khoor, zruog brxu dwwdfn!"
print("Ciphertext:", ciphertext)
print("\nAttempting to break the shift cipher:")
break_shift_cipher(ciphertext)
