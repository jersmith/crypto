""" The app-runner for the crypto module. """

import sys
from crypto.common import commando
from crypto.ciphers import caesar

def format(text):
  """ Print text in block format. """
  i = 0
  out = ''
  while i < len(text):
    if i % 24 == 23:
      print(out)
      out = ''
    else:
      out += text[i] + ' '

    i += 1

  if len(out) > 0:
    print(out)

def run():
  """ Drive the ciphers from command line input. """
  (err, value) = commando.parse('cipher [key] (decrypt)', sys.argv[1:])

  if err == True:
    print(value)
    return

  data = sys.stdin.readlines()
  cipher = None

  if value['cipher'] == 'caesar':
    cipher = caesar

  output_text = ''
  for line in data:
    if value['decrypt'] == True:
      output_text += cipher.decrypt(value['key'], line)
    else:
      output_text += cipher.encrypt(value['key'], line)

  format(output_text)
