from base64 import b64decode
from Crypto.Cipher import AES

key = b'YELLOW SUBMARINE'

def decrypt_yellow(content):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(content)

if __name__ == "__main__":
    content = b64decode(open('chal7-data.txt').read())
    print(decrypt_yellow(content))
