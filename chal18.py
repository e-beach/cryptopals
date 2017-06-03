import cryptopals as c
from struct import pack

def CTR_Encrypt(text, key=c.RAND_KEY, offset=0):
    text = c.as_bytes(text)
    start_block = offset // 16
    # limit to 2 ** 32 bytes transfereed
    return b''.join(
            c.strxor(
                c.ECB_encrypt(
                    b'\x00' * 8 + pack("<l", i + start_block) + b'\x00' * 4,
                    key=key),
                block)
            for i, block in enumerate(c.chunks(text)))

if __name__ == "__main__":
    print(CTR_Encrypt(c.b64decode('L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=='), key=c.SUBMARINE_KEY))
