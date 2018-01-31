# This is Problem 3

letters = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(key, message):
    "This will encrypt the message"
    output = ''
    for i in message.lower():
        try:
            j = (letters.index(i) + key) % 26
            output += letters[j]
        except ValueError:
            output += i
    return output.lower()


def decrypt(key, message):
    "This will decrypt the message"
    output = ''
    for i in message:
        try:
            j = (letters.index(i) - key) % 26
            output += letters[j]
        except ValueError:
            output += i
    return output


text = "Roman is cool and has so many more friends than Bhavya!"
keys = 5

encrypted = encrypt(keys, text)
print('Encrypted:', encrypted)

decrypted = decrypt(keys, encrypted)
print('Decrypted:', decrypted)
