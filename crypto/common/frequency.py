""" Frequency counting, letters, pairs, and more """

import math

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def count_letters(lines):
  """ Find the histogram of all the letters in lines, by percentage expressed as integer. """

  histogram = {}
  total = 0

  for line in lines:
    line = line.upper()
    for letter in line:
      if letter in ALPHABET:
        current_count = histogram.get(letter, 0)
        histogram[letter] = current_count + 1
        total += 1

  for key in histogram.keys():
    histogram[key] = math.floor((histogram[key] / total) * 100)

  return histogram

def count_letter_pairs(lines):
  """ Find the histogram of all adjacent letters in lines. """

  histogram = {}

  for line in lines:
    line = line.upper()
    for letter in line:
      if letter in ALPHABET:
        current_count = histogram.get(letter, 0)
        histogram[letter] = current_count + 1

  return histogram

