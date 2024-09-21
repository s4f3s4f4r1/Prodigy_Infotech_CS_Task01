print("   ____                            ____ _       _               ")
print("  / ___|___  __ _ ___  ___ _ __   / ___(_)_ __ | |__   ___ _ __ ")
print(" | |   / _ \/ _` / __|/ _ \ '__| | |   | | '_ \| '_ \ / _ \ '__|")
print(" | |__|  __/ (_| \__ \  __/ |    | |___| | |_) | | | |  __/ |   ")
print("  \____\___|\__,_|___/\___|_|     \____|_| .__/|_| |_|\___|_|   ")
print("                                         |_|                    ") 
print("  Create by s4f3s4f4r1 ")
def encrypt_caesar(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_caesar(text):
    print("\nBrute-forcing decryption:")
    for shift in range(1, 51):
        decrypted_text = decrypt_caesar(text, shift)
        print(f"Shift {shift}: {decrypted_text}")

def caesar_cipher():
    choice = input("Choose 1 for encryption or 2 for decryption: ")

    if choice == '1':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = encrypt_caesar(message, shift)
        print(f"Encrypted Message: {encrypted_message}")

    elif choice == '2':
        message = input("Enter the message to decrypt: ")
        decrypt_option = input("Choose option:\n1. Default shift value (23)\n2. Known shift value\n3. Brute force\n")

        if decrypt_option == '1':
            decrypted_message = decrypt_caesar(message, 23)
            print(f"Decrypted Message using default shift value: {decrypted_message}")
        
        elif decrypt_option == '2':
            shift = int(input("Enter the known shift value: "))
            decrypted_message = decrypt_caesar(message, shift)
            print(f"Decrypted Message: {decrypted_message}")
        
        elif decrypt_option == '3':
            brute_force_caesar(message)
        else:
            print("Invalid option selected.")
    else:
        print("Invalid choice selected.")

# Run the Caesar cipher program
caesar_cipher()
print("Thank You for using my Ceasar Chipher tool :)")
