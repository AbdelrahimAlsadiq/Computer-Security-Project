class VIGENERE:
    def __init__(self, msg=None, key=None, cipher=None) -> None:
        self.msg = msg
        self.key = key
        self.cipher = cipher
    
    def encrypt(self):
        self.cipher = ""
        non_alpha_count = 0

        for i in range(len(self.msg)):
            shift = ord(self.key[i % len(self.key) - non_alpha_count].lower()) % 97
            print(shift)
            
            char = self.msg[i]
            
            if char.isupper():
                self.cipher += chr((ord(char) + shift - 65) % 26 + 65)
            elif char.islower():
                self.cipher += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                non_alpha_count += 1
                self.cipher += char

        return self.cipher
    
    def decrypt(self):
        self.msg = ""
        non_alpha_count = 0

        for i in range(len(self.cipher)):
            shift = ord(self.key[i % len(self.key) - non_alpha_count].lower()) % 97
            char = self.cipher[i]
            
            if char.isupper():
                self.msg += chr((ord(char) - shift - 65) % 26 + 65)
            elif char.islower():
                self.msg += chr((ord(char) - shift - 97) % 26 + 97)
            else:
                non_alpha_count += 1
                self.msg += char

        return self.msg