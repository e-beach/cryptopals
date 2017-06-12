from base64 import b64decode
import chal3

def as_bytes(str_or_byte):
    try:
        return str_or_byte.encode('latin-1')
    except AttributeError:
        return bytes(str_or_byte)

def bitstring(string):
    return ''.join(bin(c)[2:].zfill(8) for c in string)

def hamming_distance(b1, b2):
    if len(b1) != len(b2):
        raise ValueError("string lengths must be equal")
    b1 = as_bytes(b1)
    b2 = as_bytes(b2)
    return sum(x[0] != x[1] for x in zip(bitstring(b1), bitstring(b2)))

def fitness(keysize):
    return hamming_distance(content[0:keysize], content[keysize:2*keysize]) / keysize

def solve_with_best_keysize(content):
    candidates = list(range(2,41))
    candidates.sort(key = lambda x: chal3.fitness(solve(x, content[0:1000])))
    return solve(candidates[-1], content)

def solve(keysize, content):
    blocks = [ [ content[blck] for blck in range(i, len(content), keysize) ] for i in range(keysize) ]
    blocks = [ chal3.decrypt(blck) for blck in blocks ]
    result = ''.join(chr(blocks[i % keysize][i // keysize]) for i in range(len(content)))
    return result

if __name__ == "__main__":
    content = b64decode(open('data/6.txt').read())
    print(solve_with_best_keysize(content))
