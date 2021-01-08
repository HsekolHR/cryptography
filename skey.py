from cryptography.fernet import Fernet
# Generate key
def generate_key(myfile):
    key = Fernet.generate_key()
    with open(myfile,'wb') as mykey:
        mykey.write(key)
    return key
# generate_key()