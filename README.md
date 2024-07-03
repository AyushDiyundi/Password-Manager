# Password-Manager

Before running the Password Manager script, you need to generate an encryption key. Uncomment and run the write_key() function in PasswordManager.py once:

python

    from cryptography.fernet import Fernet

    def write_key():
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

    # Uncomment and run write_key() once to generate the key file
    # write_key()

    This will create a key.key file in the script's directory, which is necessary for encrypting and decrypting passwords.

Usage

    Running the Password Manager:

    To use the Password Manager, run the PasswordManager.py script using Python.

    Options:

        Add Password: Enter add to add a new password. You will be prompted to enter an account name and password. The password will be encrypted and stored in passwords.txt.

        View Passwords: Enter view to view existing passwords stored in passwords.txt. Passwords will be decrypted and displayed.

        Quit: Enter q to quit the Password Manager.

Notes

    Encryption Key: Keep the key.key file secure. Losing this file will make it impossible to decrypt passwords stored with the current key.

    Security: This Password Manager encrypts passwords using Fernet symmetric encryption, which is secure as long as the key.key file is kept confidential.
