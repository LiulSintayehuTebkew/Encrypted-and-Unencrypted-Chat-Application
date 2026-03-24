# Encrypted-and-Unencrypted-Chat-Application
This project has 3 features where the first is insecure chatting application, the 2nd provides simple symmetric encryption but the 3rd provides the strongest asymmetric RSA encryption algorithm.
**This project have 3 sections where the security measure taken increases from none to highly secured**
**1.Insecure Chat Application**
    - here conversation between 2 parties is done in plain text. 
    - No security measure is taken
    - Oscar(attackers can sniff the packet using wireshark. I will demo this inside the decomentation file
**2.Encrypted with Symetric Encryption Algorithm(shift cipher)**
    - the conversation between the 2 parties is some how secured.
    - but the strength of the encryption is very weak for 2 reasons.
      1. it is shift cipher: which means the key space is just 26. 
              - this is easily broken with brute force attack. I will add the bruteforce code to the project.
      2. symmetric keys have key distribution problem.
              - even though it is not prone to brute force attack, if the key is exchange is done publicly it will be sniffed and used to read the message.
**3.Encrypted with Asymmetric Encryption (RSA)**
    - this is the most secured and trusted way of communication
    - this is the technology used to day to secure day to day internet browser
    - used in areas like https and other highly secured application
    - RSA solves the problem of key distribution by providing the concept of 2 different keys for encryption and decryption where data will be encrypted using public       keys and will be decrypted only by individuals with correct private key.
    - in modern world RSA is also used to encrypt the secret key generated for message encryption for AES algorithm.
