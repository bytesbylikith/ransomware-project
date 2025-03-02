# #!/usr/bin/env python3

# import os
# from cryptography.fernet import Fernet

# # Collect files to decrypt
# files = []

# for file in os.listdir():
#     if file in ("ransomeware.py", "thekey.key", "decrypt.py", "requirements.sh", "encryption_log.txt"):
#         continue
#     if os.path.isfile(file):
#         files.append(file)

# # Load the encryption key
# try:
#     with open("thekey.key", "rb") as key_file:
#         secretkey = key_file.read()
#     print("[INFO] Encryption key loaded successfully.")
# except FileNotFoundError:
#     print("[ERROR] Key file 'thekey.key' not found!")
#     exit(1)

# # Decrypt each file
# for file in files:
#     try:
#         with open(file, "rb") as thefile:
#             contents = thefile.read()
#         contents_decrypted = Fernet(secretkey).decrypt(contents)
#         with open(file, "wb") as thefile:
#             thefile.write(contents_decrypted)
#         print(f"[INFO] Decrypted: {file}")
#     except Exception as e:
#         print(f"[ERROR] Failed to decrypt {file}: {e}")

# print("\n[NOTICE] Decryption complete.")
#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet
import logging

# Setup logging
logging.basicConfig(filename='decryption_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def collect_files():
    files = []
    for file in os.listdir():
        if file in ("ransomware.py", "thekey.key", "decrypt.py", "requirements.sh", "encryption_log.txt", "RANSOM_NOTE.txt"):
            continue
        if os.path.isfile(file):
            files.append(file)
    return files

def load_key():
    try:
        with open("thekey.key", "rb") as key_file:
            key = key_file.read()
        logging.info("Encryption key loaded successfully.")
        return key
    except FileNotFoundError:
        logging.error("Key file 'thekey.key' not found!")
        exit(1)

def decrypt_files(files, key):
    for file in files:
        try:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(key).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
            logging.info(f"Decrypted: {file}")
        except Exception as e:
            logging.error(f"Failed to decrypt {file}: {e}")

if __name__ == "__main__":
    files_to_decrypt = collect_files()
    decryption_key = load_key()
    decrypt_files(files_to_decrypt, decryption_key)
    print("[NOTICE] Decryption complete.")
