from cryptography.fernet import Fernet
import os.path
from os import path
import skey

# load key
def load_key():
    if path.exists('mykey.key') == True:
        with open('mykey.key','rb') as mykey:
            key = mykey.read()
            return key
    else:
        key = skey.generate_key('mykey.key')
        return key

# encryption
def encryption(filename):
    # loading key
    key = load_key()
    f= Fernet(key)
    # original files
    with open(filename, 'rb') as myfile:
        orginal = myfile.read()

    encrypt_file= str(filename)
    # saving new file with encrypt
    encrypted = f.encrypt(orginal)
    with open(encrypt_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print("The file is encrypted and saved as "+encrypt_file)

# decryption
def decryption(filename):
    # loading key
    key = load_key()
    f= Fernet(key)
    # open or read the encrypt file
    with open(filename, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    
    decrypt_file = str(filename)
    # decrypt the file and save as new
    decrypted = f.decrypt(encrypted)
    with open(decrypt_file, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    print("File is decrypted and saved as "+ decrypt_file)

if __name__ == "__main__":
    # Inputs for filename
    fname = input("Enter the filename:")
    if path.exists(fname) == True:
        enorde = input("Enter 'en' for (encrypt) or 'de' for (decrypt) :")
        if enorde == 'en':
            encryption(fname)
        elif enorde == 'de':
            decryption(fname)
        else:
            print("The given input is Invalid. It should be 'en' or 'de'")
    else:
        print("No such file found",fname)
    
 