""" The app-runner for the crypto module. """

import sys
from crypto.common import commando
from crypto.ciphers import caesar
from crypto.ciphers import vigenere

def format_block_text(text):
  """ Print text in block format. """
  i = 0
  out = ''

  while i < len(text):
    if i > 0 and i % 24 == 0:
      print(out)
      out = ''

    out += text[i] + ' '
    i += 1

  if len(out) > 0:
    print(out)

def run():
  """ Drive the ciphers from command line input. """
  (err, value) = commando.parse('cipher [key] (decrypt)', sys.argv[1:])

  if err:
    print(value)
    return

  data = sys.stdin.readlines()
  cipher = None

  if value['cipher'] == 'caesar':
    cipher = caesar
  elif value['cipher'] == 'vigenere':
    cipher = vigenere

  output_text = ''
  for line in data:
    if value['decrypt']:
      output_text += cipher.decrypt(value['key'], line)
    else:
      output_text += cipher.encrypt(value['key'], line)

  format_block_text(output_text)
