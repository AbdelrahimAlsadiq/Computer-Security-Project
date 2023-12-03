>Note: Each title can be found in the source code with ```###``` comment
## 1. How is the Secure Hash Algorithm 1 (SHA-1) Works:
1. **Padding:** 
    - The input message is padded so that its length is congruent to 448 modulo 512 bits. 
    - Padding ensures that the length of the message is a multiple of 512 bits (64 bytes).

</br>

2. **Message Length:** 
    - The original length of the message in bits is appended to the end of the padded message. 
    - The length is represented as a 64-bit integer, making the final message a multiple of 512 bits.

</br>

3. **Initialize Variables:** 
    - Starts with five 32-bit integers (h0, h1, h2, h3, h4) representing the initial hash values. 
    - These values are based on the first 32 bits of the fractional parts of the square roots of the first five prime numbers.

</br>

4. **Process the Message:**
    - The message is divided into blocks of 512 bits each.
    - Each block is further divided into 16 words of 32 bits each, forming the message schedule.

</br>

5. **Extend the Message Schedule:**
    - From the 16 words obtained in step 4, extend the message schedule to create 80 words in total.
    - The additional words are created using a recursive formula that involves applying bitwise operations (AND, XOR, OR) and left rotations.

</br>

6. **Initialize Temporary Variables:**
    - Initialize five temporary variables (a, b, c, d, e) with the values of the initial hash values (h0, h1, h2, h3, h4).

</br>

7. **Compression Function:** 
    - Perform 80 rounds of operations using a compression function that operates on these temporary variables and the extended message schedule.
    - Each round involves various bitwise operations (AND, XOR, OR), addition modulo 2^32, and circular left shifts.

</br>

8. **Update Hash Values:**
    - After 80 rounds of processing, update the hash values (h0, h1, h2, h3, h4) using the temporary variables (a, b, c, d, e) calculated in the compression function.

</br>

9. **Final Hash Value:**
    - Concatenate the updated hash values (h0, h1, h2, h3, h4) to obtain a 160-bit hash value, which represents the SHA-1 output or message digest.
---
## 2. How is the Data Encryption Standard (DES) Works:
1. **Key Generation:**
    - Generate a 56-bit key from an input key of 64 bits by removing every eighth bit and ignoring parity bits. The resulting key is divided into sixteen 48-bit subkeys, one for each round of encryption.

</br>

2. **Initial Permutation (IP):**
    - Permute the 64-bit plaintext block according to an initial permutation table (IP). This step rearranges the bits of the plaintext.

</br>

3. **Splitting and Expansion:**
    - Divide the permuted plaintext block into two halves, each containing 32 bits.
    - Expand the right half of 32 bits to 48 bits using an expansion permutation table.

</br>

4. **Key Mixing (XOR with Subkey):**
    - Perform an XOR operation between the expanded 48-bit right half and the first 48-bit subkey derived from the main key.

5. **Substitution (S-boxes):**
    - Divide the result of the XOR operation into eight 6-bit blocks.
    - Substitute each 6-bit block using eight substitution boxes (S-boxes), each providing a 4-bit output based on a 6-bit input. The S-boxes provide a nonlinear transformation.

</br>

6. **Permutation (P-box):**
    - Permute the outputs of the S-boxes using a permutation table (P-box) to obtain a new 32-bit block.

</br>

7. **Feistel Network:**
    - Use a Feistel network structure by swapping the left and right halves, and repeating steps 3 to 6 for a total of 16 rounds (iterations) with different subkeys.

8. **Final Permutation (FP):**
    - After the 16 rounds of the Feistel structure, perform a final permutation (FP) on the swapped halves of the data.

</br>

9. **Output:**
    - The final permutation produces the encrypted 64-bit ciphertext block, which is the result of encrypting the original plaintext using DES.

</br>

10. **Decryption:**
    - Decryption in DES is the same as encryption but with the subkeys used in reverse order.
    - The ciphertext block undergoes an initial permutation (IP) similar to encryption, then goes through 16 rounds using the subkeys in reverse order.
    - Finally, a final permutation (FP) is applied to obtain the decrypted plaintext block.

---
## 3. How is the Digital Signature Standard (DSS) Works:
1. **Key Generation:**
    - Generate a pair of keys: a private key and a corresponding public key. The private key is kept secret, while the public key is shared with others.

</br>

2. **Signing the Message:**
    - The signer computes a digital signature using their private key and the hash value of the message.
    - The signing operation involves performing mathematical operations using the private key and the hash value to create the digital signature.
    - The exact signature generation process in DSS involves modular arithmetic and other mathematical operations.

</br>

3. **Verification Process:**
    - The verifier receives the message, the digital signature, and the signer's public key.
    - The verifier calculates the hash value of the received message using the same hashing algorithm used by the signer.
    - Using the public key provided by the signer, the verifier performs mathematical operations to verify the authenticity of the signature.
    - The verification process checks whether the computed hash matches the hash value extracted from the signature using the public key. If they match, the signature is considered valid; otherwise, it is invalid