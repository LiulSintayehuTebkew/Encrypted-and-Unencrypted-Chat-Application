# Encrypted and Unencrypted Chat Application

This project demonstrates three types of chat applications with increasing levels of security.

## Different Levels of Security (Increasing downward)

### 1. Insecure Chat Application (No Encryption at all)
- Conversations are sent in plain text.
- No security measures are implemented.
- Vulnerable to attackers (e.g., "Oscar") sniffing packets using tools like Wireshark.  
  *Demo of packet sniffing is included in the documentation.*

### 2. Encrypted with Symmetric Encryption (Shift Cipher)
- Messages are encrypted between the two parties.
- **Weaknesses:**
  1. **Shift Cipher:** Key space is only 26, making brute-force attacks trivial.  
     *Brute-force attack code is included in the project.*
  2. **Key Distribution Problem:** If the key is exchanged publicly, it can be intercepted and used to read messages.

### 3. Encrypted with Asymmetric Encryption (RSA)
- Provides the highest level of security and trust.
- Widely used in modern internet applications like HTTPS.
- **Key Advantages:**
  - Solves key distribution issues using separate public and private keys.
  - Public key encrypts the message; private key decrypts it.
- Commonly used to encrypt secret keys for symmetric algorithms like AES.

### 4. Cyber Attacks
- **Unencrypted Chat Attack:** Used Wireshark to capture network traffic and read the conversation in plain text.
- **Shift Cipher Attack:** 
  - Captured the first message for key exchange, then used the key to decrypt ciphertext.
  - Also demonstrated brute-force attack (easy since key space is only 26).  
    *Python brute-force code is attached in the documentation.*
- **RSA Attack:** 
  - Used prime factorization to get `p` and `q`, which are crucial to generate the private key.
  - Works only if prime numbers are small.  
  - In real-world applications, very large primes are used to make brute-forcing computationally infeasible.

### Note
- This project is **only for educational purposes**.
- Demonstrates how to secure data exchange and how to select the best algorithm to maintain security.
