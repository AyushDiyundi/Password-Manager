from cryptography.fernet import Fernet


# Function to generate and save a new encryption key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the encryption key from file
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# Load the encryption key from file
key = load_key()

# Create a Fernet instance with the loaded key
fer = Fernet(key)


# Function to view decrypted passwords from passwords.txt
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            decrypted_password = fer.decrypt(passw.encode()).decode()
            print("User:", user, "| Password:", decrypted_password)


# Function to add an encrypted password to passwords.txt
def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    # Encrypt the password and write to passwords.txt
    with open('passwords.txt', 'a') as f:
        encrypted_password = fer.encrypt(pwd.encode()).decode()
        f.write(name + "|" + encrypted_password + "\n")


# Main loop to interact with the user
while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
