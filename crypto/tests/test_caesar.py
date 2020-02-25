""" Unit test cases for caesar cipher. """

import unittest
import random
from crypto.ciphers import caesar


class TestCaesar(unittest.TestCase):
  """ Test fixture for Caesar test cases. """
  def test_rotate(self):
    """ Caesar shift """
    key = ['F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E' ]

    cipher_text = caesar.encrypt(key, 'a broken clock is right twice a day')
    self.assertEqual(cipher_text[0], 'F')
    plain_text = caesar.decrypt(key, cipher_text)

    self.assertEqual(plain_text, 'ABROKENCLOCKISRIGHTTWICEADAY')

  def test_scramble(self):
    """ Caesar scramble """
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    key = ''

    while len(alphabet) > 0:
      key += alphabet.pop(random.randrange(0, len(alphabet)))

    cipher_text = caesar.encrypt(key, 'a broken clock is right twice a day')
    plain_text = caesar.decrypt(key, cipher_text)

    self.assertEqual(plain_text, 'ABROKENCLOCKISRIGHTTWICEADAY')

  

