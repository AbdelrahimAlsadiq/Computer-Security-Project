# Computer-Security-Project
The project aims to create a user-friendly Python application with a graphical user interface (GUI) using Tkinter to perform cryptographic operations such as:

1. **DES encryption.**
2. **SHA-1 Hashing.**
3. **Digital Signature Standard (DSS).** 

This application will provide a convenient platform for users to encrypt and decrypt data using the Data Encryption Standard (DES), generate hash values using the SHA-1 algorithm, and sign/verify messages using the Digital Signature Standard.

---
## 1. How is the Data Encryption Standard (DES) Works:

---
## 2. How is the Secure Hash Algorithm 1 (SHA-1) Works:
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

</br>

10. **Output:** 
    - The resulting hash value represents a unique and fixed-size representation of the input message.
---
## 3. How is the Digital Signature Standard (DSS) Works:
---
## Team Members:
- [Sara Abdelraheem Hamed](https://github.com/SaraEldamarany)
- [Abdelrahim Mohamed Alsadiq](https://github.com/AbdelrahimAlsadiq)
