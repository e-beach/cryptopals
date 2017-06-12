import cryptopals as c


class EncryptionOracle:
    def __init__(self, key=c.RAND_KEY):
        self.key = key

    def sign(self, plaintext):
        plaintext = c.as_bytes(plaintext)
        return c.Sha1Hash().update(self.key + plaintext).digest()

    def verify(self, plaintext, mac):
        return mac == self.sign(plaintext)


if __name__ == "__main__":
    oracle = EncryptionOracle()
    mac = oracle.sign("asdf")
    print('MAC:', mac)
    print(oracle.verify("asdf", mac))