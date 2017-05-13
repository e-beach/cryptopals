import chal3
import chal7
import chal8
import chal9

IV = bytes([0] * 16)

def decode_bytes(content):
    return ''.join([b.decode('utf-8') for b in content])

def CBC_encrypt(message, iv=IV, key=chal7.KEY):
    offset = 16 - (len(message) % 16)
    if offset == 16:
        offset = 0
    # message = chal9.pad(message, length=offset)
    result = []
    last = iv
    for blck in chal8.chunks(message, 16):
        last = chal7.EBC_encrypt(chal3.strxor(blck, last), key)
        result.append(last)
    return b''.join(result)

def CBC_decrypt(message, iv=IV, key=chal7.KEY):
    result = []
    last = iv
    for blck in chal8.chunks(message, 16):
        result.append(chal3.strxor(chal7.EBC_decrypt(blck, key), last))
        last = blck
    return decode_bytes(result)

if __name__ == "__main__":
    import requests
    from base64 import b64decode
    content = b64decode(requests.get('https://cryptopals.com/static/challenge-data/10.txt').text)
    assert CBC_encrypt(CBC_decrypt(content).encode('utf-8')) == content
    print(CBC_decrypt(CBC_encrypt(CBC_decrypt(content).encode('utf-8'))))
    print(CBC_decrypt(content))
