import requests
import binascii
from collections import Counter

def unhex_data(data):
    return [ binascii.unhexlify(l) for l in data.split('\n')[:-1] ]

def chunks(stuff, n=16):
    result = [stuff[i:i+n] for i in range(0, len(stuff), n)]
    # if isinstance(stuff, bytes):
    #     return bytes(result) # this doesn't make any sense
    return result

def countit(line):
    return max(list(Counter(chunks(line)).values()))

if __name__ == "__main__":
    lines = unhex_data(requests.get('https://cryptopals.com/static/challenge-data/8.txt').text)
    best = max(lines, key=countit)
    print(best)
    print(countit(best))
