# Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
from base64 import b64decode
from chal3 import decrypt
from chal3 import fitness as chal3fitness
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


def show_candidates():
    candidates = list(range(2,41))
    candidates.sort(key=fitness)
    for x in candidates:
        print(x, solve(x)[0:20])

def solve_candidates():
    candidates = list(range(2,41))
    candidates.sort(key = lambda x: chal3fitness(solve(x, contents[0:1000])))
    print(solve(candidates[-1]))

def solve(KEYSIZE, contents=contents):
    blocks = [ [] for i in range(KEYSIZE) ]
    for i in range(KEYSIZE):
        for blck in range(i, len(contents), KEYSIZE):
            # append a single byte to the block
            blocks[i].append(contents[blck])
    blocks = [ decrypt(x) for x in blocks ]
    result = ''.join(blocks[x % KEYSIZE][x // KEYSIZE] for x in range(len(contents)))
    return result

solve_candidates()
