inputstr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

hex_dict = { '0':0 , '1':1 , '2':2 , '3':3 , '4':4 , '5':5 , '6':6 , '7':7 , '8':8, '9':9 , 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15, }

base64_dict = {
0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D', 4 : 'E', 5 : 'F', 6 : 'G', 7 : 'H', 8 : 'I', 9 : 'J',
10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'a', 27: 'b', 28: 'c', 29: 'd',
30: 'e', 31: 'f', 32: 'g', 33: 'h', 34: 'i', 35: 'j', 36: 'k', 37: 'l', 38: 'm', 39: 'n',
40: 'o', 41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't', 46: 'u', 47: 'v', 48: 'w', 49: 'x',
50: 'y', 51: 'z', 52: '0', 53: '1', 54: '2', 55: '3', 56: '4', 57: '5', 58: '6', 59: '7',
60: '8', 61: '9', 62: '+', 63: '/', }

def from_hex(string):
    """return array of half-bytes from hex"""
    return [ hex_dict[c] for c in string ]

def to_hex(half_bytes):
    inv_map = {v: k for k, v in hex_dict.items()}
    return ''.join([inv_map[i] for i in half_bytes])

def hex_to_b64(inputstr):
    half_bytes = [ hex_dict[c] for c in inputstr ]
    b64_encoded = []
    saved = None
    i = 0
    while i < len(half_bytes):
        if saved is not None:
            assert (saved <= 0x3)
            nextb64 = ( saved << 4 ) | half_bytes[i]
            saved = None
            i += 1
        elif i == len(half_bytes) - 1:
            nextb64 = half_bytes[i]
            i += 1
        else:
            nextb64 = ( half_bytes[i] << 2 ) | ( half_bytes[i+1] >> 2 )
            saved = half_bytes[i+1] & 0x3
            i += 2
        b64_encoded.append(base64_dict[nextb64])
    return ''.join(b64_encoded)


if __name__ == "__main__":
    print(hex_to_b64(inputstr))
