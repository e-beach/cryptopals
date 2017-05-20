from chal11 import rand_bytes
import chal12

def oracle(content, prefix=rand_bytes(0, 100)):
        return chal12.oracle(prefix + content)

def discard_prefix_block(cipher, blocksize=16):
    s1 = cipher(b'a')
    s2 = cipher(b'b')
    i = 0   
    while s1[i] == s2[i]:
        i += 1
    blck = i // blocksize
    def discarded(text):
        return cipher(text)[blck * blocksize:]
    return discarded

def normalize(cipher, blocksize=16):
    cipher = discard_prefix_block(cipher)
    for i in range(blocksize):
        msg1 = b'a' * i + b'b' * blocksize + b'c' * blocksize
        msg2 = b'c' * i + b'b' * blocksize + b'd' * blocksize
        if cipher(msg1)[blocksize:2*blocksize] == cipher(msg2)[blocksize:2*blocksize]:
            def normalized(text):
                return cipher(b'a'* i + text)[blocksize:]
            return normalized

print(chal12.find_secret(normalize(oracle)).decode('utf-8'))
