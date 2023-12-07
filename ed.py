from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename="secret.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_key(filename="secret.key"):
    return open(filename, "rb").read()

def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

if __name__ == "__main__":
    key = generate_key()
    save_key(key)

    message_to_encrypt = input("Enter the message to encrypt: ")
    encrypted_message = encrypt_message(message_to_encrypt, key)

    print(f"\nOriginal Message: {message_to_encrypt}")
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = decrypt_message(encrypted_message, key)
    print(f"Decrypted Message: {decrypted_message}")
