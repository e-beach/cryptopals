from Crypto.Cipher import AES

SUBMARINE_KEY="YELLOW SUBMARINE"

def ECB_decrypt(content, key=SUBMARINE_KEY):
    return AES.new(key, AES.MODE_ECB).decrypt(content)

def ECB_encrypt(content, key=SUBMARINE_KEY):
    return AES.new(key, AES.MODE_ECB).encrypt(content)

if __name__ == "__main__":
    content = c.b64decode(open('data/7.txt').read())
    assert ECB_encrypt(ECB_decrypt(content)) == content
    print(ECB_decrypt(content))
