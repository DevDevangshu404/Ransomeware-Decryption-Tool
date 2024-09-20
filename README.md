# Ransomware Decryption Tool - Devangshu Mazumder

This project is a Python-based decryption tool designed to decrypt files that were encrypted by a ransomware attack. The tool analyzes the ransomware, recovers the key, and decrypts the affected files. It uses the Advanced Encryption Standard (AES) in CBC mode to decrypt the files and stores the decrypted files in a separate directory.

# Download Hank's Backup: https://drive.google.com/file/d/1XR3xHpdBfR8HGXItexhzny9AzzGMWc8i/view?usp=sharing
## Features
- Decrypts files encrypted with AES in CBC mode.
- Displays a progress bar during the decryption process.
- Stores decrypted files in a `DecryptedFiles` folder.
- Provides an ASCII art header for a user-friendly terminal interface.

## Tools Used
- **Python 3**: The core programming language used to implement the decryption tool.
- **PyCryptodome**: A Python library for cryptographic operations, used to handle AES decryption.
- **Ghidra**: A reverse-engineering tool to analyze the ransomware code and extract encryption keys.
- **Virtual Environment**: Used to isolate the Python environment and dependencies for this project.

## Setup Instructions (MacBook Pro 2017 - Intel)
### Prerequisites
Before running the decryption tool, ensure that the following software is installed:
- **Python 3**: If not installed, download and install Python 3 from [python.org](https://www.python.org/downloads/).
- **Ghidra**: To analyze the ransomware code, download Ghidra from [ghidra-sre.org](https://ghidra-sre.org/).

### Step-by-Step Setup
1. **Clone the Repository**: Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/ransomware-decryption-tool.git
   cd

### Create and Activate a Virtual Environment:
1. **Create a virtual environment to isolate the dependencies
   ```bash
   python3 -m venv venv
2. **Activate the virtual environment:
   ```bash
   source venv/bin/activate

### Install Dependencies: Install the required Python libraries, including pycryptodome for cryptographic operations:
   ```bash
pip install pycryptodome
```
### Run the Decryption Tool:

```bash
python decyption_ransomware.py
```
### Deactivate the Virtual Environment: After finishing the session, deactivate the virtual environment:

```bash
deactivate
```
# How It Works
1. ** Ransomware Analysis: Using Ghidra, the AES encryption keys and initialization vector (IV) were extracted
      from the ransomware binary.

2. ** Decryption Algorithm: The AES algorithm in CBC mode is used to decrypt each encrypted file.

3. ** Decrypted Files: The decrypted files are stored in a new folder called DecryptedFiles within the
      HanksBackup directory.

4. ** Progress Bar: While decrypting, a loading bar is displayed to show the progress.

# Notes
1. ** Do Not Run Ransomware: Do not execute the actual ransomware on your machine. The analysis and decryption are performed statically using reverse engineering.
2. ** Compatibility: This script was developed and tested on a MacBook Pro (Intel, 2017) with macOS and Python 3


