# Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
from base64 import b64decode
import bitstring

def bits(string):
    return ''.join(bin(c)[2:].zfill(8) for c in string)

def hamming_distance(b1, b2):
    if len(b1) != len(b2):
        raise ValueError("string lengths must be equal")
    try:
        b1 = b1.encode('ascii')
        b2 = b2.encode('ascii')
    except AttributeError:
        pass
    return sum(x[0] != x[1] for x in zip(bits(b1), bits(b2)))

assert hamming_distance("this is a test", "wokka wokka!!!") == 37

contents = b64decode(open('chal6-data.txt').read())

def fitness(keysize):
    return hamming_distance(contents[0:keysize], contents[keysize:2*keysize]) / keysize

KEYSIZE = min(range(2,41), key=fitness)

blocks = [ [] for i in range(KEYSIZE) ]
for i in range(KEYSIZE):
    for blck in range(i, len(contents), KEYSIZE):
        blocks[i].append(contents[blck])



# Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:
# this is a test
# and
# wokka wokka!!!
# is 37. Make sure your code agrees before you proceed.
# For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
# The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.
# Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
# Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
# Solve each block as if it was single-character XOR. You already have code to do this.
# For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.
