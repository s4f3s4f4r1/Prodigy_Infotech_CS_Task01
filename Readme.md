
# Introduction

This a Python-based command-line application designed to encrypt and decrypt messages using the Caesar cipher technique. The tool allows users to either encrypt or decrypt a message by applying a shift to the characters in the text. In addition, it offers brute-force decryption capabilities to attempt all possible shifts on an encrypted message, making it a versatile tool for beginners in cryptography.




## Features

- Encrypting Messages
- Decrypting Messages: Users can decrypt a message by either:
- Using a known shift value.
- Using a default shift value (23), commonly used for Caesar cipher puzzles.
- Brute-forcing all possible shifts to find the original message.
### Program Workflow
#### Banner Display
      ____                            ____ _       _               
     / ___|___  __ _ ___  ___ _ __   / ___(_)_ __ | |__   ___ _ __ 
    | |   / _ \/ _` / __|/ _ \ '__| | |   | | '_ \| '_ \ / _ \ '__|
    | |__|  __/ (_| \__ \  __/ |    | |___| | |_) | | | |  __/ |   
     \____\___|\__,_|___/\___|_|     \____|_| .__/|_| |_|\___|_|   
                                          |_|                    
    Create by s4f3s4f4r1
 
This adds a professional touch and branding to the tool, indicating that the program is created by the developer s4f3s4f4r1 that is my username/sign name.
    

## Code Structure
The program is modular, with the following key functions:
    
    encrypt_caesar(text, shift) 
Encrypts the input text by shifting the characters by the provided value.

    decrypt_caesar(text, shift)

 Decrypts the text by shifting characters in the opposite direction.

    brute_force_caesar(text)

Tries every shift between 1 and 50 to display all possible decrypted messages.

    caesar_cipher()

The main function that handles user interaction and calls the respective functions based on the user's choices.

## Run 

Download the .py file and then paste this command in terminal to run the program.

```bash
  python3 Task_01_Caesar_Cipher.py
```


               
