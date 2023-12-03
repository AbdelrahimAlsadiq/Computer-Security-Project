# How to Use the Application:
1) Run the ```main.py``` by using.
    - Command Line Interface (CLI):
    ```python
    python3 main.py
    ```
    - IDE application (Visual Studio Code is preferred).
2) Choose from the main menu the algorithm you want to use.

---
### For Secure Hash Algorithm 1 (SHA-1) Form:
- For single input, enter the message you want to get hashed value of it and click on **Sign** button.
- For multiple inputs, click on **Upload File** and select the file that contains the various messages.
    > Note: file MUST have one message per line.
- The output will be stored in `SHA1_output.txt`
---
### For Data Encryption Standard (DES) Form:
- For single input Encryption, enter the message you want to encrypt, the secret key, and click on **Encrypt** button.
- For single input Decryption, enter the message you want to decrypt, the secret key, and click on **Decrypt** button.
- For multiple inputs Encryption, click on **Upload File** and select the file that contains the various messages and secret key for each message.
    > Notes: 
    >- input values MUST be in hexadecimal format. (16 (64-bit) value for each message/key)
    >- file MUST have one message and one key value per line, separated by commas ",".
    >- The application doesn't support file input for multiple decryptions.
- The output will be stored in `DES_output.txt`
---
### For Digital Signature Standard (DSS) Form:
- For single input sign, enter the message you want to sign and click on **Sign** button.
- For single input verify, enter the message you want to verify, the public key, the signature value, and click on **Verify** button.
- For multiple inputs Encryption, click on **Upload File** and select the file that contains the various messages and secret key for each message.
    > Notes: 
    >- The public key and Signature MUST BE in base-64 format.
    >- file MUST have one message, one public key, and one signature value per line, separated by commas ",".
    >- The application doesn't support file input for multiple verifications.
- The output will be stored in `DSS_output.txt`