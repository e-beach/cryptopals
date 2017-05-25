from base64 import b64decode, b64encode

KEY = b'YELLOW SUBMARINE'

from chal3 import strxor
from chal6 import as_bytes
from chal7 import EBC_encrypt, EBC_decrypt
from chal8 import chunks
from chal9 import pad16
from chal10 import CBC_encrypt, CBC_decrypt, pad_EBC_encrypt, IV
from chal11 import really_randint as randint
from chal11 import RANDKEY
from chal12 import byte
from chal15 import remove_padding
