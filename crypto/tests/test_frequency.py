""" Unit test cases for the frequency distribution utility. """

import unittest
from crypto.common import frequency


class TestFrequency(unittest.TestCase):
  """ Test suite for Frequency test cases. """
  def test_letter_frequency(self):
    """ Count only letters """
    text_lines = 'abcdef\nabc\nab\n34ab ksd a'.split('\n')
    histogram = frequency.count_letters(text_lines)
    self.assertEqual(histogram['A'], 29)
    self.assertFalse('Z' in histogram)
    self.assertEqual(histogram['K'], 5)
