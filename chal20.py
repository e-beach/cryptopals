import cryptopals as c
from chal6 import solve
import chal19

text = open('data/20.txt').read()
lines = [ c.CTR_Encrypt(c.b64decode(s)) for s in text.split('\n') ]
c.pprint(lines)
c.RAND_KEY = '\x00' # cryptopals ate the key

key_size = min(map(len, lines))
total = b''.join(line[:key_size] for line in lines)
print(solve(key_size, total))

# chal19.solve(lines, chal19.solve_keystream(lines))



