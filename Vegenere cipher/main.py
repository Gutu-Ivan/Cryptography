import string


class vigenere_cipher:
    out_text = []

    def __init__(self, message, key):
        self.alphabet = string.ascii_lowercase
        self.message = message.lower()
        self.letter_to_index = dict(zip(self.alphabet, range(len(self.alphabet))))
        self.index_to_letter = dict(zip(range(len(self.alphabet)), self.alphabet))
        self.key = key.lower()
        self.ready_message = ''

    def encrypt(self):
        split_message = [
            self.message[i: i + len(self.key)] for i in range(0, len(self.message), len(self.key))
        ]

        for section in split_message:
            i = 0
            for letter in section :
                if letter == ' ':
                    self.ready_message += ' '
                    i += 1
                else:
                    number = (self.letter_to_index[letter] + self.letter_to_index[self.key[i]]) % len(self.alphabet)
                    self.ready_message += self.index_to_letter[number]
                    i += 1
        return self.ready_message

    def decrypt(self):
        self.ready_message = ''
        self.out_text = []

        return self.ready_message.join(self.out_text)

test = vigenere_cipher('Per as pera adastra', 'SUPER')
print('The encrypted message is:', test.encrypt())
print('The decrypted message is:', test.decrypt())