""" Unit test cases for vigenere cipher. """

import unittest
from crypto.ciphers import vigenere

class TestVigenere(unittest.TestCase):
  """ Test fixture for Vigenere test cases. """
  def test_identity(self):
    """ Vigenere useless key """
    cipher_text = vigenere.encrypt('AAA', 'a broken clock is right twice a day')
    self.assertEqual(cipher_text, 'ABROKENCLOCKISRIGHTTWICEADAY')

    plain_text = vigenere.decrypt('AAA', cipher_text)
    self.assertEqual(plain_text, 'ABROKENCLOCKISRIGHTTWICEADAY')

  def test_scramble(self):
    """ Vigenere scramble """
    cipher_text = vigenere.encrypt('CAT', 'a broken clock is right twice a day')
    plain_text = vigenere.decrypt('CAT', cipher_text)

    self.assertEqual(plain_text, 'ABROKENCLOCKISRIGHTTWICEADAY')

    cipher_text = vigenere.encrypt('C', 'C')
    self.assertEqual(cipher_text, 'E')
