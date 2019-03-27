from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode
from datetime import datetime


password = '<$3JOH22A$>'


def id2token(id):
    ciphertext = encrypt(password, id)
    return b64encode(ciphertext).decode('utf-8')


def token2id(token):
    cipherbytestring = b64decode(token)
    return str(int(decrypt(password, cipherbytestring)))


def generate_id():
    timestamp = int(datetime.now().timestamp())
    return str(timestamp)


def generate_token():
    id = generate_id()
    return id2token(id)

# Example code:
# import SessionToken
# tk=SessionToken.generate_token()
# print(tk)
# => c2MAArDDsorX9REFcB5Mo/fXCY2HZubq/81PUVkUdVBQ7/OyKFEgQplU51NkvYVYEzFthsZP3FHDbcYRHcutCcGo47EtTKepu/Ylegve
# id=SessionToken.token2id(tk)
# print(id)
# => 1552422033