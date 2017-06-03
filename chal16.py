from chal10 import pad_CBC_encrypt, CBC_decrypt
from chal15 import remove_padding
from chal9 import pad16

def dummy_padding(string):
    return "a" * (len(pad16(string)) - len(string))

encrypt = pad_CBC_encrypt
decrypt = lambda text: remove_padding(CBC_decrypt(text))

prefix = "comment1=cooking%20MCs;userdata="
suffix = ";comment2=%20like%20a%20pound%20of%20bacon"

def cookie(text):
    return encrypt(prefix + text.replace(';', '%3B').replace('=', '%3D') + suffix)

def is_admin(cookie):
    return b";admin=true" in remove_padding(decrypt(cookie))

if __name__ == "__main__":
    bits = dummy_padding(prefix) + ":admin<true"
    to_alter1 = len(prefix) + bits.index('<') - 16
    to_alter2 = len(prefix) + bits.index(':') - 16
    c = bytearray(cookie(bits))
    c[to_alter1] ^= 1
    c[to_alter2] ^= 1
    print(CBC_decrypt(bytes(c)))
    print(is_admin(bytes(c)))
