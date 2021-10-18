import string


class affine_cipher:
    out_text = []

    def __init__(self, message, key1, key2):
        self.alphabet = string.ascii_lowercase
        self.message = message
        self.key1 = key1
        self.key2 = key2
        self.ready_message = ''

    def encrypt(self):
        self.message = self.message.lower()
        for symbol in self.message:
            index = self.alphabet.index(symbol)
            trans_key = (self.key1 * index + self.key2) % len(self.alphabet)
            new_letter = self.alphabet[trans_key]
            self.out_text.append(new_letter)

        return self.ready_message.join(self.out_text)

    def decrypt(self):
        return self.ready_message


test = affine_cipher('CRIPTOGRAFIA', 3, 2)
print('The encrypted message is:', test.encrypt())
print('The decrypted message is:', test.decrypt())
