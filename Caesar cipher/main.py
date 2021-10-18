import string


class caesar_cipher:
    out_text = []

    def __init__(self, message, key):
        self.alphabet = string.ascii_lowercase
        self.table = self.alphabet[key:] + self.alphabet[:key]
        self.message = message
        self.key = key
        self.ready_message = ''

    def encrypt(self):
        self.message = self.message.lower()
        for symbol in self.message:
            index = self.alphabet.index(symbol)
            newLetter = self.table[index]
            self.out_text.append(newLetter)
        return self.ready_message.join(self.out_text)

    def decrypt(self):
        return self.ready_message


test = caesar_cipher('Cryptography', 12)
print('The encrypted message is:', test.encrypt())
print('The decrypted message is:', test.decrypt())