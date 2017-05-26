import cryptopals as c
from struct import pack

def CTR(text):
    # limit to 2 ** 32 bytes transfereed
    return b''.join(
            c.strxor(
                c.EBC_encrypt(b'\x00' * 8 + pack("<l", i) + b'\x00' * 4), 
                block) 
            for i, block in enumerate(c.chunks(text)))

if __name__ == "__main__":
    print(CTR(c.b64decode('L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==')))
