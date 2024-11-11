# decrypt.py

import string

# Define the alphabet and create mappings
alphabet = string.ascii_uppercase
mp = dict(zip(alphabet, range(len(alphabet))))
mp2 = dict(zip(range(len(alphabet)), alphabet))

def generate_key(cipher_text, keyword):
    """
    Generates a repeating key based on the ciphertext and keyword.
    """
    key = ''
    keyword = keyword.upper()
    for i in range(len(cipher_text)):
        key += keyword[i % len(keyword)]
    return key

def decrypt(cipher_text, keyword):
    """
    Decrypts the ciphertext using the Poly-Alphabetic Cipher with the provided keyword.
    """
    key = generate_key(cipher_text, keyword)
    plain_text = ''
    for i in range(len(cipher_text)):
        cipher_char = cipher_text[i].upper()
        if cipher_char in mp:
            shift = mp[key[i].upper()]  # Shift based on key character
            decrypted_index = (mp[cipher_char] - shift + 26) % 26
            plain_char = mp2[decrypted_index]
            plain_text += plain_char
        else:
            # Non-alphabet characters are added unchanged
            plain_text += cipher_text[i]
    return plain_text

if __name__ == "__main__":
    # Example usage
    cipher_text = "AIHUBVIWSVFKYHPIYVUIAOXMRWXZ"
    keyword = "DECEPTIVE"
    
    decrypted_text = decrypt(cipher_text, keyword)
    print("Ciphertext :", cipher_text)
    print("Keyword    :", keyword)
    print("Decrypted Text:", decrypted_text)
