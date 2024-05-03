import random

class SUBSTITUTION:

    global alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, msg, key, cipher) -> None:
        self.msg = msg
        self.key = key
        self.cipher = cipher
        self.alphabet = alphabet
    
    def generate_key(self):
        self.key = ""    
        while len(self.key) < 26:
            ch = chr(random.randint(97,122))
            if ch not in self.key:
                self.key += ch
        return self.key

    def is_valid_key(self):
        return list(self.alphabet.lower()) == sorted(list(self.key))
    
    def encrypt(self):
        if self.key == "":
            self.generate_key()

        self.cipher = ""
        for i in range(len(self.msg)):
            if self.msg[i].lower() not in self.key:
                self.cipher += self.msg[i]
            else:
                if self.msg[i].isupper():
                    self.cipher += self.key[self.alphabet.index(self.msg[i].lower())].upper()
                else:
                    self.cipher += self.key[self.alphabet.index(self.msg[i])]

        return self.cipher
    
    def decrypt(self):

        self.msg = ""
        for i in range(len(self.cipher)):
            if self.cipher[i].lower() not in self.alphabet:
                self.msg += self.cipher[i]
            else:
                if self.cipher[i].isupper():
                    self.msg += self.alphabet[self.key.index(self.cipher[i].lower())].upper()
                else:
                    self.msg += self.alphabet[self.key.index(self.cipher[i])]

        return self.msg