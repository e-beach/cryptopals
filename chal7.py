from base64 import b64decode
from Crypto.Cipher import AES

KEY = b'YELLOW SUBMARINE'

def EBC_decrypt(content, key=KEY):
    return AES.new(key, AES.MODE_ECB).decrypt(content)

def EBC_encrypt(content, key=KEY):
    return AES.new(key, AES.MODE_ECB).encrypt(content)

if __name__ == "__main__":
    content = b64decode(open('data/7.txt').read())
    assert EBC_encrypt(EBC_decrypt(content)) == content
    print(EBC_decrypt(content))
