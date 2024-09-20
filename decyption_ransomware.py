import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import time
import shutil
import sys

# Create ASCII art for the header
def print_header():
    header = """
-----------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------
.-.  .  . ..-..-..  ..  .  .  .-..--      .-..--.-.-.. ..-.----.-.-.. .      ---.-..-..
|-' /_\ |\|`-.| ||\/||/\| /_\ |-'|-       | :|-(  |-' Y |-' |  | | ||\|       | | || ||
'`-'   '' '`-'`-''  ''  ''   ''`-'--      '-''--`-'`- ' '   ' -'-`-'' '       ' `-'`-''-'
-----------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------
    """
    print(header)

# Function to show a simple loading bar
def print_progress_bar(iteration, total, length=50):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\rDecryption Progress: |{bar}| {percent}% Complete')
    sys.stdout.flush()

# Decrypt the files and store them in DecryptedFiles directory
def decrypt_cbc_file(input_file, output_file, key, iv, file_size):
    with open(input_file, 'rb') as f_in:
        data = f_in.read()

    with open(output_file, 'wb') as f_out:
        iteration = int(len(data) / 1028)
        for i in range(iteration):
            cipher = AES.new(key, AES.MODE_CBC, iv)
            bytes_to_write = int.from_bytes(data[16:20], byteorder="little")
            chunk = data[20:1028]
            decrypted_chunk = cipher.decrypt(chunk)
            if i == iteration - 1:
                f_out.write(decrypted_chunk[:bytes_to_write])
            else:
                f_out.write(decrypted_chunk)
            data = data[1028:]

            # Update the progress bar
            print_progress_bar(i + 1, iteration)

    print("\nDecryption complete.")

# Example usage
if __name__ == "__main__":
    print_header()

    dir_path = "./HanksBackup"
    decrypted_folder = os.path.join(dir_path, "DecryptedFiles")

    # Create the DecryptedFiles directory if it doesn't exist
    if not os.path.exists(decrypted_folder):
        os.makedirs(decrypted_folder)
        print(f"Created folder: {decrypted_folder}")

    key = b'\x8d\x02\xe6\x5e\x50\x83\x08\xdd\x74\x3f\x0d\xd4\xd3\x1e\x48\x4d'
    iv = b'\x0a\x0b\x0c\x0d\x0e\x0f\xa0\xb0\xc0\xd0\xe0\xf0\xaa\xbb\xcc\xdd'

    # Iterate over files in the HanksBackup directory
    for filename in os.listdir(dir_path):
        input_file = os.path.join(dir_path, filename)

        # Skip the DecryptedFiles directory itself
        if os.path.isdir(input_file):
            continue

        output_file = os.path.join(decrypted_folder, "decrypted_" + filename)
        file_size = os.path.getsize(input_file)

        # Decrypt the file
        print(f"\nDecrypting {filename}...")
        decrypt_cbc_file(input_file, output_file, key, iv, file_size)
