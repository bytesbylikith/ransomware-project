#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Collect files to decrypt
files = []

for file in os.listdir():
    if file in ("ransomeware.py", "thekey.key", "decrypt.py", "requirements.sh", "encryption_log.txt"):
        continue
    if os.path.isfile(file):
        files.append(file)

# Load the encryption key
try:
    with open("thekey.key", "rb") as key_file:
        secretkey = key_file.read()
    print("[INFO] Encryption key loaded successfully.")
except FileNotFoundError:
    print("[ERROR] Key file 'thekey.key' not found!")
    exit(1)

# Decrypt each file
for file in files:
    try:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
        print(f"[INFO] Decrypted: {file}")
    except Exception as e:
        print(f"[ERROR] Failed to decrypt {file}: {e}")

print("\n[NOTICE] Decryption complete.")
