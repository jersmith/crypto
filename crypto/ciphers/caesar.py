
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(key, plain_text):
  cipher_text = ''
  for letter in plain_text.upper():
    if letter in alphabet:
      cipher_text += key[alphabet.index(letter)]

  return cipher_text

def decrypt(key, cipher_text):
  cipher_text = ''.join(cipher_text.strip().split(' '))
  plain_text = ''
  for letter in cipher_text:
    plain_text += alphabet[key.index(letter)]

  return plain_text
