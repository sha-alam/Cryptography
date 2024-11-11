class MonoalphabeticCipher:
    def __init__(self):
        self.normal_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        self.coded_char = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O',
                           'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
                           'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

    def string_encryption(self, s):
        encrypted_string = ""
        for char in s:
            for i in range(26):
                if char == self.normal_char[i]:
                    encrypted_string += self.coded_char[i]
                    break
                elif char < 'a' or char > 'z':
                    encrypted_string += char
                    break
        return encrypted_string

    def string_decryption(self, s):
        decrypted_string = ""
        for char in s:
            for i in range(26):
                if char == self.coded_char[i]:
                    decrypted_string += self.normal_char[i]
                    break
                elif char < 'A' or char > 'Z':
                    decrypted_string += char
                    break
        return decrypted_string


def main():
    cipher = MonoalphabeticCipher()
    plain_text = "I am ICEIAN"

    print("Plain text:", plain_text)

    # Changing the whole string to lowercase
    encrypted_message = cipher.string_encryption(plain_text.lower())
    print("Encrypted message:", encrypted_message)

    decrypted_message = cipher.string_decryption(encrypted_message)
    print("Decrypted message:", decrypted_message)


main()
