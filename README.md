# Encrypted-and-Unencrypted-Chat-Application

**This project has 3 sections where the security measure taken increases from none to highly secured.**

## 1. Insecure Chat Application
- Conversation between two parties is done in plain text
- No security measure is taken
- Oscar (attackers) can sniff the packet using Wireshark. This will be demonstrated inside the documentation file

## 2. Encrypted with Symmetric Encryption Algorithm (Shift Cipher)
- The conversation between the two parties is somewhat secured
- However, the strength of the encryption is very weak for two reasons:

  **1. It is a shift cipher** — the key space is just 26
  - This is easily broken with brute force attack. The brute force code will be added to the project

  **2. Symmetric keys have a key distribution problem**
  - Even though it is not prone to brute force attack, if the key exchange is done publicly it will be sniffed and used to read the message

## 3. Encrypted with Asymmetric Encryption (RSA)
- This is the most secured and trusted way of communication
- This is the technology used today to secure day-to-day internet browsing
- Used in areas like HTTPS and other highly secured applications
- RSA solves the problem of key distribution by providing the concept of two different keys for encryption and decryption, where data is encrypted using public keys and decrypted only by individuals with the correct private key
- In the modern world, RSA is also used to encrypt the secret key generated for message encryption in the AES algorithm
