freqs = { 'a':8.167, 'b':1.492, 'c':2.782, 'd':4.253, 'e':12.70, 'f':2.228, 'g':2.015, 'h':6.094, 'i':6.966, 'j':0.153, 'k':0.772, 'l':4.025, 'm':2.406, 'n':6.749, 'o':7.507, 'p':1.929, 'q':0.095, 'r':5.987, 's':6.327, 't':9.056, 'u':2.758, 'v':0.978, 'w':2.360, 'x':0.150, 'y':1.974, 'z':0.074, ' ': 19.18 }
import binascii

def fitness(string):
    try:
        string = string.decode('utf-8')
    except UnicodeDecodeError:
        return -1
    except AttributeError:
        pass
    return sum( freqs[c] for c in string.lower() if c in freqs)

def strxor(a, b):
    """ Take the xor of two python bytes objects, outputing another bytes object """
    return bytes([ a^b for (a, b) in zip(a, b)])

def decrypt(content):
    """ decrypt a hex-encoded string that has been xored with a single character.  """
    candidates = [ strxor(content, [b] * len(content)) for b in range(256) ]
    return max(candidates, key=fitness)

if __name__ == "__main__":
    from sys import argv
    print(decrypt(binascii.unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')))
