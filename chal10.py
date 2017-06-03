import chal3
from chal6 import as_bytes
import chal7
import chal8
import chal9

IV = bytes([0] * 16)

SUBMARINE_KEY = "YELLOW_SUBMARINE"

def decode_bytes(content):
    return b''.join(content).decode('utf-8')

def pad_CBC_encrypt(message, iv=IV, key=SUBMARINE_KEY):
    message = chal9.pad16(message)
    message = as_bytes(message)
    result = []
    last = iv
    for blck in chal8.chunks(message, 16):
        last = chal7.ECB_encrypt(chal3.strxor(blck, last), key)
        result.append(last)
    return b''.join(result)

def CBC_decrypt(message, iv=IV, key=SUBMARINE_KEY):
    result = []
    last = iv
    for blck in chal8.chunks(message, 16):
        result.append(chal3.strxor(chal7.ECB_decrypt(blck, key), last))
        last = blck
    return b''.join(result)

def pad_ECB_encrypt(message, key=SUBMARINE_KEY):
    message = chal9.pad16(message)
    return chal7.ECB_encrypt(message, key)

if __name__ == "__main__":
    import requests
    from base64 import b64decode
    content = b64decode(requests.get('https://cryptopals.com/static/challenge-data/10.txt').text)
    assert pad_CBC_encrypt(CBC_decrypt(content)) == content
    print(CBC_decrypt(content).decode('utf-8'))
