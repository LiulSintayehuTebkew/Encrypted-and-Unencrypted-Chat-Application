# Encrypted and Unencrypted Chat Application

This project demonstrates three types of chat applications with increasing levels of security.

## Different level of security(Increasing downward)

### 1. Insecure Chat Application(No Encryption at all)
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
