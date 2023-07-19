import random
import string
import base64
import hashlib


def get_code_verifier():
  code_verifier = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128)))
  code_verifier = base64.urlsafe_b64encode(code_verifier.encode('utf-8'))
  return code_verifier


def gen_code_challenge(code_verifier):
  code_challenge = hashlib.sha256(code_verifier).digest()
  code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').replace('=', '')
  return code_challenge



if __name__ == '__main__':
  code_verifier = get_code_verifier()
  code_challenge = gen_code_challenge(code_verifier)

  print('..verifier...')
  print(code_verifier)
  print('..challenge...')
  print(code_challenge)

