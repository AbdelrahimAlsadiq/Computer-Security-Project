class BASE64:
    global alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    def __init__(self, data=None, encoded=None) -> None:
        self.data = data
        self.encoded = encoded
    
    def encode(self):


        self.data = self.data.encode()

        # Padding the input string with zero bytes to make its length a multiple of 3
        padding = 0
        while len(self.data) % 3 != 0:
            self.data += b'\x00'
            padding += 1

        # Encode the data
        result = ''
        for i in range(0, len(self.data), 3):
            chunk = (self.data[i] << 16) + (self.data[i + 1] << 8) + self.data[i + 2]

            # First 6 bits
            result += alphabet[(chunk >> 18) & 63]

            # Second 6 bits
            result += alphabet[(chunk >> 12) & 63]

            # Third 6 bits (may be a padding)
            result += alphabet[(chunk >> 6) & 63]
            
            # Fourth 6 bits (may be a padding)
            result += alphabet[chunk & 63]

        list_result = list(result)
        if padding > 0:
            for i in range(padding):
                list_result[len(result)-(i+1)] = "="
        result = ''.join(list_result)
        return result
    
    def decode(self):
        bit_str = ""
        self.data = ""

        for char in self.encoded:
            if char in alphabet:
                bin_char = bin(alphabet.index(char)).lstrip("0b")
                bin_char = bin_char.zfill(6)
                bit_str += bin_char

        brackets = [bit_str[x:x+8] for x in range(0,len(bit_str),8)]

        for bracket in brackets:
            self.data += chr(int(bracket,2))
        
        self.data = self.data.replace("\x00","")
        return self.data

