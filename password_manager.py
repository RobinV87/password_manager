from cryptography.fernet import Fernet
import json
import os

def generate_key():
    return Fernet.generate_key()

def load_key(file_path):
    return open(file_path, "rb").read()

def save_key(key, file_path):
    with open(file_path, "wb") as key_file:
        key_file.write(key)

def encrypt_password(key, password):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def decrypt_password(key, encrypted_password):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

def save_passwords(passwords, file_path):
    with open(file_path, "w") as password_file:
        json.dump(passwords, password_file)

def load_passwords(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as password_file:
            return json.load(password_file)
    else:
        return {}

def add_password(passwords, site, password, key):
    encrypted_password = encrypt_password(key, password)
    passwords[site] = encrypted_password.decode()
    return passwords

def get_password(passwords, site, key):
    if site in passwords:
        encrypted_password = passwords[site].encode()
        return decrypt_password(key, encrypted_password)
    else:
        return None

def main():
    key_file = "secret.key"
    password_file = "passwords.json"

    if not os.path.exists(key_file):
        key = generate_key()
        save_key(key, key_file)
    else:
        key = load_key(key_file)

    passwords = load_passwords(password_file)

    while True:
        print("*==========================*")
        print("*|  Password Manager 1.0   *")
        print("*==========================*")
        action = input("Do you want to add a new password or retrieve an existing one? (add/retrieve/exit): ").strip().lower()
        if action == "add":
            site = input("Enter the site name: ").strip()
            password = input("Enter the password: ").strip()
            passwords = add_password(passwords, site, password, key)
            save_passwords(passwords, password_file)
            print(f"Password for {site} added.")
        elif action == "retrieve":
            site = input("Enter the site name: ").strip()
            password = get_password(passwords, site, key)
            if password:
                print(f"The password for {site} is: {password}")
            else:
                print(f"No password found for {site}.")
        elif action == "exit":
            break
        else:
            print("Invalid action. Please choose add, retrieve, or exit.")

if __name__ == "__main__":
    main()
