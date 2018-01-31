# This is Problem 5

letters = 'abcdefghijklmnopqrstuvwxyz'

def caesar_encrypt(key, message):
    #This will encrypt the message
    output = ''
    for i in message.lower():
        try:
            j = (letters.index(i) + key) % 26
            # Mod will output the placement of the new letters
            output += letters[j]
        except ValueError:
            output += i
    return output.lower()


def caesar_decrypt(key, message):
    #This will decrypt the message
    output = ''
    for i in message:
        try:
            j = (letters.index(i) - key) % 26
            # Mod will output the placement of the new letters
            output += letters[j]
        except ValueError:
            output += i
    return output

#mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp
text = "mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp!"
keys = 15

encrypted = caesar_encrypt(keys, text)
print('Encrypted:', encrypted)

decrypted = caesar_decrypt(keys, encrypted)
