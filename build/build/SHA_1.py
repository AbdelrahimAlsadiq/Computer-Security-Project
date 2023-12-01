import struct

class SHA1:
    def __init__(self, message):
        self.message = message

    def left_rotate(self, n, b):
        return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

    def sha1_hash(self):
        h0 = 0x67452301
        h1 = 0xEFCDAB89
        h2 = 0x98BADCFE
        h3 = 0x10325476
        h4 = 0xC3D2E1F0

        data = self.message.encode('utf-8')  # Convert message to bytes

        ml = len(data) * 8
        data += b'\x80'

        while (len(data) * 8) % 512 != 448:
            data += b'\x00'

        data += struct.pack('>Q', ml)

        for i in range(0, len(data), 64):
            chunk = data[i:i + 64]

            words = [0] * 80
            for j in range(0, 64, 4):
                words[j // 4] = struct.unpack('>I', chunk[j:j + 4])[0]

            for j in range(16, 80):
                words[j] = self.left_rotate((words[j - 3] ^ words[j - 8] ^ words[j - 14] ^ words[j - 16]), 1)

            a, b, c, d, e = h0, h1, h2, h3, h4

            for j in range(80):
                if 0 <= j <= 19:
                    f = (b & c) | ((~b) & d)
                    k = 0x5A827999
                elif 20 <= j <= 39:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif 40 <= j <= 59:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                else:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6

                temp = self.left_rotate(a, 5) + f + e + k + words[j] & 0xFFFFFFFF
                e, d, c, b, a = d, c, self.left_rotate(b, 30), a, temp

            h0 = (h0 + a) & 0xFFFFFFFF
            h1 = (h1 + b) & 0xFFFFFFFF
            h2 = (h2 + c) & 0xFFFFFFFF
            h3 = (h3 + d) & 0xFFFFFFFF
            h4 = (h4 + e) & 0xFFFFFFFF

        return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)
