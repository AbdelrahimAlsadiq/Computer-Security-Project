class CAESAR:
    def __init__(self, msg=None, key=None, cipher=None) -> None:
        self.msg = msg
        self.key = int(key,10)
        self.cipher = cipher

    def encrypt(self):
        self.cipher = ""
        for i in range(len(self.msg)):
            char = self.msg[i]
            if char.isupper():
                self.cipher += chr((ord(char) + self.key - 65) % 26 + 65)
            elif char.islower():
                self.cipher += chr((ord(char) + self.key - 97) % 26 + 97)
            else:
                self.cipher += char
        return self.cipher
    
    def decrypt(self):
        self.msg = ""
        for i in range(len(self.cipher)):
            char = self.cipher[i]
            if char.isupper():
                self.msg += chr((ord(char)  - self.key - 65) % 26 + 65)
            elif char.islower():
                self.msg += chr((ord(char)  - self.key - 97) % 26 + 97)
            else:
                self.msg += char
        return self.msg