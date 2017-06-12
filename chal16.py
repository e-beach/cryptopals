import cryptopals as c

def dummy_padding(string):
    return "a" * (len(c.pad16(string)) - len(string))

encrypt = c.pad_CBC_encrypt
decrypt = lambda text: c.remove_padding(c.CBC_decrypt(text), check_padding=False)

prefix = "comment1=cooking%20MCs;userdata="
suffix = ";comment2=%20like%20a%20pound%20of%20bacon"

def cookie(text):
    return encrypt(prefix + text.replace(';', '%3B').replace('=', '%3D') + suffix)

def is_admin(cookie):
    return b";admin=true" in decrypt(cookie)

if __name__ == "__main__":
    bits = dummy_padding(prefix) + ":admin<true"
    to_alter1 = len(prefix) + bits.index('<') - 16
    to_alter2 = len(prefix) + bits.index(':') - 16
    cook= bytearray(cookie(bits))
    cook[to_alter1] ^= 1
    cook[to_alter2] ^= 1
    print(c.CBC_decrypt(cook))
    print(is_admin(cook))
