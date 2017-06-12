import cryptopals as c

def dummy_padding(string):
    return "a" * (len(c.pad16(string)) - len(string))

class CBC_Cipher:
    def __init__(self, iv, key):
        self.iv = iv
        self.key = key

    def decrypt(self, ciphertext, check_padding=True):
        return c.remove_padding(c.CBC_decrypt(ciphertext, iv=self.iv, key=self.key), check_padding)

    def encrypt(self, content):
        return c.pad_CBC_encrypt(content, iv=self.iv, key=self.key)

cipher = CBC_Cipher(iv=c.RAND_KEY, key=c.RAND_KEY)


prefix = "comment1=cooking%20MCs;userdata="
suffix = ";comment2=%20like%20a%20pound%20of%20bacon"

class AsciiError(ValueError):
    pass

def is_ascii_char(c):
    return c < 128

def verify_ascii(text):
    if not all(is_ascii_char(c) for c in text):
        raise AsciiError( text.decode('latin-1') + " is not ascii compliant" )

def cookie(text):
    return cipher.encrypt(prefix + text.replace(';', '%3B').replace('=', '%3D') + suffix)

def is_admin(cookie):
    return b";admin=true" in cipher.decrypt(cookie)

if __name__ == "__main__":

    # server
    msg = '\xAA' * 16 * 3
    cook = cookie(msg)

    # attacker
    try:
        blocks = c.blocks(cook)
        cooked = blocks[1] + b'\x00' * 16 + blocks[1]

        # receiver
        decrypted = cipher.decrypt(cooked, check_padding=False)
        verify_ascii(decrypted) # This error msg is sent across the wire.

    # attacker
    except AsciiError as e:
        text = e.args[0]
        l = len(" is not ascii compliant")
        decrypted = text[:-l]
        blocks = c.blocks(decrypted)
        key = c.strxor(blocks[0].encode('latin-1'), blocks[2].encode('latin-1'))
        print(key)
        assert key == c.RAND_KEY

