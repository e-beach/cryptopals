from chal7 import EBC_decrypt
from chal9 import pad16
from chal10 import pad_EBC_encrypt
from chal11 import RAND_KEY

uid = -1

def encrypt(data):
    """encrypt data under random key, with padding"""
    return pad_EBC_encrypt(data, RAND_KEY)

def decrypt(data):
    return EBC_decrypt(data, RAND_KEY)

def parse_qstring(qstring):
    return  { kv[0]:kv[1] for kv in [ term.split('=') for term in qstring.split('&') ] }

def profile_for(email):
    global uid
    uid += 1
    email = email.replace('&', '').replace('=', '')
    return "email={0}&uid={1}&role={2}".format(email, uid, 'user')

def cookie(email):
    return encrypt(profile_for(email))

def data(cookie):
    decrypted = decrypt(cookie)

    # remove padding
    padcount = decrypted[-1]
    if padcount < 16:
        decrypted = decrypted[0 : -1 * padcount]

    return parse_qstring(decrypted.decode('utf-8'))

email1 = 'a' * ( 32 - len(profile_for('')[:-4]))
email2 = 'a' * (16 - len('email=')) + pad16('admin')

email_uid = cookie(email1)[0:32]
role = cookie(email2)[16:32]

admin_auth = email_uid + role
print(data(admin_auth))
