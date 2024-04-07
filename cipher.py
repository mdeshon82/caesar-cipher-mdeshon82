# add your code here
def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    text = input("Enter text to encrypt: ")
    shift = int(input("Enter shift value: "))
    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
