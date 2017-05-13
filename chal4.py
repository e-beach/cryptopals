import binascii
from chal3 import decrypt, fitness

f = open('data/4.txt').read()
candidates = [ decrypt(binascii.unhexlify(line)) for line in f.split('\n') ]
print(max(candidates, key=fitness))
