import cryptopals as c
from functools import partial
from chal16 import dummy_padding

encrypt = decrypt = partial(c.CTR_Encrypt, key=c.RAND_KEY)

prefix = "comment1=cooking%20MCs;userdata="
suffix = ";comment2=%20like%20a%20pound%20of%20bacon"

def cookie(text):
    return encrypt(prefix + text.replace(';', '%3B').replace('=', '%3D') + suffix)

def is_admin(cookie):
    return b";admin=true" in decrypt(cookie)

if __name__ == "__main__":
    bits = dummy_padding(prefix) + ":admin<true"
    to_alter1 = len(prefix) + bits.index('<')
    to_alter2 = len(prefix) + bits.index(':')
    c = bytearray(cookie(bits))
    c[to_alter1] ^= 1
    c[to_alter2] ^= 1
    print(decrypt(c))
    print(is_admin(c))