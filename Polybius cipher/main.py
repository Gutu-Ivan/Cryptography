class polybius_cipher:

    def __init__(self, message):
        self.alphabet = {
            'a': '11', 'b': '12', 'c': '13', 'd': '14', 'e': '15',
            'f': '21', 'g': '22', 'h': '23', 'i': '24', 'j': '25', 'k': '26',
            'l': '31', 'm': '32', 'n': '33', 'o': '34', 'p': '35',
            'q': '41', 'r': '42', 's': '43', 't': '44', 'u': '45',
            'v': '51', 'w': '52', 'x': '53', 'y': '54', 'z': '55', ' ': ' '
        }
        self.message = message
        self.ready_message = ''

    def encrypt(self):
        self.message = self.message.lower()
        return self.ready_message.join(self.alphabet[letter] for letter in self.message)

    def decrypt(self):
        return self.ready_message


test = polybius_cipher('CRIPTOGRAFIA')
print('The encrypted message is:', test.encrypt())
print('The encrypted message is:', test.decrypt())
