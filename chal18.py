import cryptopals as c
from struct import pack

def CTR(text):
    return b''.join(
            c.strxor(
                c.pad_EBC_encrypt(pack("<l", 0) + pack("<l", i)), 
                block) 
            for i, block in enumerate(c.chunks(text)))

if __name__ == "__main__":
    print(CTR(c.b64decode('L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==')))
