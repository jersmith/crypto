""" Vigenere cipher is the classic poly-alphabet cipher. The key is used to determine
    the next caesar cipher.

    Remember we're not using ASCII yet; just manipulate indices of alphabets.
"""


ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(key, plain_text):
  """ Use each letter of the key to find the rotation of the current alphabet. """
  cipher_text = ''
  key_index = 0

  shifts = []
  # Do this once, not for every iteration of the key
  for letter in key:
    shifts.append(ALPHABET.index(letter))

  for letter in plain_text.upper():
    if letter in ALPHABET:
      shift_index = shifts[key_index % len(key)]
      letter_index = ALPHABET.index(letter)
      cipher_text += ALPHABET[(letter_index + shift_index) % 26]
      key_index += 1

  return cipher_text

def decrypt(key, cipher_text):
  """ Use each letter of the key to unrotate the current alphabet. """
  cipher_text = ''.join(cipher_text.strip().split(' '))
  plain_text = ''
  key_index = 0

  shifts = []
  # Do this once, not for every iteration of the key
  for letter in key:
    shifts.append(ALPHABET.index(letter))

  for letter in cipher_text:
    shift_index = shifts[key_index % len(key)]
    letter_index = ALPHABET.index(letter)
    plain_text += ALPHABET[(letter_index + (26 - shift_index)) % 26]
    key_index += 1

  return plain_text
