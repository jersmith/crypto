""" Caesar cipher is the classic mono-alphabet cipher. The 'key' is the replacement
    alphabet.
"""


ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(key, plain_text):
  """ Using the key as the replacement alphabet, 'encrypt' the plain_text. """
  cipher_text = ''
  for letter in plain_text.upper():
    if letter in ALPHABET:
      cipher_text += key[ALPHABET.index(letter)]

  return cipher_text

def decrypt(key, cipher_text):
  """ Using the key as the replacement alphabet, 'decrypt' the cipher_text. """
  cipher_text = ''.join(cipher_text.strip().split(' '))
  plain_text = ''
  for letter in cipher_text:
    plain_text += ALPHABET[key.index(letter)]

  return plain_text
