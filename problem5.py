def generate_key_square(keyword):
    """
    Generates a 5x5 key square for the Playfair cipher from a keyword.
    """
    # Remove duplicate letters from the keyword and add remaining letters of the alphabet
    keyword = ''.join(sorted(set(keyword), key=keyword.index)).upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' is combined with 'I'
    key_square = [letter for letter in keyword if letter in alphabet]
    key_square += [letter for letter in alphabet if letter not in key_square]
    return [key_square[i:i+5] for i in range(0, 25, 5)]

def find_position(letter, key_square):
    """
    Finds the position (row, column) of a letter in the key square.
    """
    for row in range(5):
        for col in range(5):
            if key_square[row][col] == letter:
                return row, col
    return None

def process_plaintext(plaintext):
    """
    Prepares the plaintext for encryption by handling duplicates and splitting into pairs.
    """
    plaintext = plaintext.upper().replace("J", "I")
    prepared_text = ""
    i = 0
    while i < len(plaintext):
        letter1 = plaintext[i]
        letter2 = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'
        
        # If letters in the pair are the same, insert an 'X' between them
        if letter1 == letter2:
            prepared_text += letter1 + 'X'
            i += 1
        else:
            prepared_text += letter1 + letter2
            i += 2

    # If the last pair has a single letter, add an 'X' to complete the pair
    if len(prepared_text) % 2 != 0:
        prepared_text += 'X'
    return prepared_text

def encrypt_playfair(plaintext, key_square):
    """
    Encrypts plaintext using the Playfair cipher with the provided key square.
    """
    ciphertext = ""
    plaintext_pairs = process_plaintext(plaintext)

    for i in range(0, len(plaintext_pairs), 2):
        letter1, letter2 = plaintext_pairs[i], plaintext_pairs[i + 1]
        row1, col1 = find_position(letter1, key_square)
        row2, col2 = find_position(letter2, key_square)

        # Apply Playfair encryption rules
        if row1 == row2:  # Same row: shift right
            ciphertext += key_square[row1][(col1 + 1) % 5]
            ciphertext += key_square[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column: shift down
            ciphertext += key_square[(row1 + 1) % 5][col1]
            ciphertext += key_square[(row2 + 1) % 5][col2]
        else:  # Rectangle rule: swap columns
            ciphertext += key_square[row1][col2]
            ciphertext += key_square[row2][col1]

    return ciphertext

# Example usage
if __name__ == "__main__":
    keyword = "playfair example"
    plaintext = "Hide the gold in the tree stump"

    # Generate key square
    key_square = generate_key_square(keyword)
    print("Key Square:")
    for row in key_square:
        print(row)

    # Encrypt plaintext
    ciphertext = encrypt_playfair(plaintext, key_square)
    print("\nPlaintext:", plaintext)
    print("Ciphertext:", ciphertext)
