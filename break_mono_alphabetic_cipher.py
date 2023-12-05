from collections import Counter
import string

def decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_text += key.get(char, char)
            else:
                decrypted_text += key.get(char.lower(), char).upper()
        else:
            decrypted_text += char
    return decrypted_text

def frequency_analysis(ciphertext):
    letter_freq = Counter(c for c in ciphertext if c.isalpha())
    most_common_letters = letter_freq.most_common()

    # English letter frequency in descending order
    english_freq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

    key = {}
    for i in range(len(most_common_letters)):
        encrypted_letter = most_common_letters[i][0]
        decrypted_letter = english_freq[i]
        key[encrypted_letter] = decrypted_letter

    return key

# Example ciphertext to break
ciphertext = "Gwc uivioml bw nqvl bpm zqopb apqnb."

print("Ciphertext:", ciphertext)

key = frequency_analysis(ciphertext)
decrypted_text = decrypt(ciphertext, key)

print("\nDecrypted Text:")
print(decrypted_text)
