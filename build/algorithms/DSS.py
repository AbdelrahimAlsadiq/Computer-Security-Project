from ecdsa import SigningKey, VerifyingKey, BadSignatureError
import base64

class DSS:
    def __init__(self, msg):
        self.msg = msg
        self.pk = None
    
    def sign(self):
        bin_msg = self.msg.encode()
        private_key = SigningKey.generate()
        signature = private_key.sign(bin_msg)
        self.pk = private_key.get_verifying_key()

        # Encode the signature and public key to base64 for string representation
        signature_b64 = base64.b64encode(signature).decode('utf-8')
        public_key_b64 = base64.b64encode(self.pk.to_string()).decode('utf-8')

        return signature_b64, public_key_b64
    
    def set_public_key(self, public_key):
        try:
            # Decode the base64 public key string to bytes
            public_key_bytes = base64.b64decode(public_key)
            self.pk = VerifyingKey.from_string(public_key_bytes)
            return True
        except Exception as e:
            print("Error setting public key:", e)
            return False
    
    def verify(self, signature, public_key, original_msg):
        # Decode the base64 signature and public key strings to bytes
        signature_bytes = base64.b64decode(signature)
        public_key_bytes = base64.b64decode(public_key)

        # Set the provided public key
        self.set_public_key(public_key)

        # Verify the signature against the provided message
        verification = self.pk.verify(signature_bytes, original_msg.encode())

        # If the verification result is True:
        if verification:
            return True
        else:
            return False


