class BASE64:
    global alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    def __init__(self, data=None, encoded=None) -> None:
        self.data = data
        self.encoded = encoded
    
    def encode(self):

        # Convert string to bytes
        if isinstance(self.data, str):
            self.data = self.data.encode()

        # Padding the input string with zero bytes to make its length a multiple of 3
        while len(self.data) % 3 != 0:
            self.data += b'\x00'

        # Encode the data
        result = ''
        for i in range(0, len(self.data), 3):
            chunk = (self.data[i] << 16) + (self.data[i + 1] << 8) + self.data[i + 2]
            result += alphabet[(chunk >> 18) & 63]
            result += alphabet[(chunk >> 12) & 63]
            result += alphabet[(chunk >> 6) & 63]
            result += alphabet[chunk & 63]

        # Add padding if necessary
        padding = len(self.data) % 3
        if padding == 1:
            result = result[:-2] + '=='
        elif padding == 2:
            result = result[:-1] + '='

        return result
    
    def decode(self):
        # Reverse mapping for Base64 alphabet
        base64_dict = {char: i for i, char in enumerate(alphabet)}

        # Remove padding characters
        self.encoded = self.encoded.rstrip('=')

        # Convert encoded string to bytes
        encoded_bytes = bytearray()
        for char in self.encoded:
            encoded_bytes.append(base64_dict[char])

        # Decode the data
        result = bytearray()
        for i in range(0, len(encoded_bytes), 4):
            chunk = (encoded_bytes[i] << 18) + (encoded_bytes[i + 1] << 12) + (encoded_bytes[i + 2] << 6) + encoded_bytes[i + 3]
            result.append((chunk >> 16) & 255)
            result.append((chunk >> 8) & 255)
            result.append(chunk & 255)

        # Remove any zero padding
        result = result.rstrip(b'\x00')

        return bytes(result)