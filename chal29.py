import cryptopals as c
from chal28 import EncryptionOracle

KEY = c.SUBMARINE_KEY
oracle = EncryptionOracle(key=KEY)

def glue_padding(message):

    message_byte_length = len(message)

    message += b'\x80'
    l = (56 - len(message)) % 64
    message += b'\x00' * l

    message_bit_length = message_byte_length * 8
    message += c.pack('>Q', message_bit_length)

    return message

def forge_mac(original_mac, payload):
    hashObj = c.Sha1Hash()
    # duplicate the state of the secret hash with the MAC

    hashObj._h = [ c.unpack('>I', num)[0] for num in c.blocks(original_mac, 4) ] # 32-bit blocks
    print(hashObj._h)
    return hashObj.update(payload).digest() # this is SHA-1(key || msg || glue || payload),
                                            # so forged_msg must be (msg || glue || payload)

def test():
    # In the future, you REALLY should check everything bit by bit each step of the way.

    plaintext = KEY + b'asdf'

    mac = oracle.sign(plaintext)
    print('forging, relying on original glue padding')
    mac2 = forge_mac(mac, b'')
    print('authenticating, relying on bootlegged glue padding')
    mac3 = oracle.sign(b'asdf' + glue_padding(KEY + plaintext))
    print('mac2', mac2)
    print('mac3', mac3)

    # print(c.Sha1Hash().update(message).digest()) # padded once
    # print(c.Sha1Hash().update(message + glue_padding(message)).digest()) # padded twice


def breakit(mac, plaintext, payload):
    # key length should be 0-255 bytes
    #  for length in range(255):
    length = 16
    glue = glue_padding(b'A' * length + plaintext)
    forged_plaintext = plaintext + glue + payload # that was def an error
    forged_mac = forge_mac(mac, payload)
    if oracle.verify(forged_plaintext, forged_mac):
        return forged_mac, forged_plaintext
    raise ValueError("Couldn't break it")

if __name__ == "__main__":

    # server
    plaintext = b"comment1=cooking%20MCs;userdata=foo;comment2=%20like%20a%20pound%20of%20bacon"
    mac = oracle.sign(plaintext)

    # attacker
    breakit(mac, plaintext, payload=b";admin=true")

    # plaintext = c.RAND_KEY + b'asdf'

    # print('forged-glue:', glue_padding(plaintext))
    # print(c.Sha1Hash().update(plaintext).digest())
    # assert glue_padding(plaintext) == sha1.gluedUp
    # test()