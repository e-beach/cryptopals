from base64 import b64decode, b64encode
from pprint import pprint

SUBMARINE_KEY = b'YELLOW SUBMARINE'

from chal3 import strxor, freqs as character_frequencies
from chal6 import as_bytes
from chal7 import ECB_encrypt, ECB_decrypt
from chal8 import chunks
from chal9 import pad16
from chal10 import pad_CBC_encrypt, CBC_decrypt, pad_ECB_encrypt, IV
from chal11 import really_randint as rand_int, rand_bytes
from chal11 import RAND_KEY
from chal12 import byte
from chal15 import remove_padding
from chal18 import CTR_Encrypt
from chal21 import MT_19937_params, MT19937 as MersenneTwister

def all_chars():
    return map(byte, range(256))
