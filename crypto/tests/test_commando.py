# pylint: disable=no-member
""" Unit test cases for commando command line processor. """

import unittest
from crypto.common import commando


class TestCommando(unittest.TestCase):
  """ Test fixture for Commando test cases. """
  def test_no_positional_parameters(self):
    """ No positional parameters in template and/or in arguments. """
    (err, value) = commando.parse('', [])
    self.assertFalse(err)

    (err, value) = commando.parse('', ['pos1'])
    self.assertTrue(err)
    self.assertEqual(value, 'Too many parameters')

    (err, value) = commando.parse('pos1', [])
    self.assertTrue(err)
    self.assertEqual(value, 'Not enough required parameters')


  def test_positional_parameters(self):
    """ Positional parameter test cases: match, no match, too many, too few. """
    positionals = 'pos1 pos2 pos3'

    (err, value) = commando.parse(positionals, ['alpha'])
    self.assertTrue(err)
    self.assertEqual(value, 'Not enough required parameters')

    (err, value) = commando.parse(positionals, ['alpha', 'z', 't', 's'])
    self.assertTrue(err)
    self.assertEqual(value, 'Too many parameters')

    (err, value) = commando.parse(positionals, ['alpha', 'beta', 'gamma'])
    self.assertFalse(err)
    self.assertEqual(value['pos1'], 'alpha')
    self.assertEqual(value['pos2'], 'beta')
    self.assertEqual(value['pos3'], 'gamma')

  def test_options(self):
    """ Option arguments test cases. """
    (err, value) = commando.parse('[opt]', ['--opt=alpha'])
    self.assertFalse(err)
    self.assertTrue('opt' in value.keys())
    self.assertEqual(value['opt'], 'alpha')

    (err, value) = commando.parse('[opt]', ['-o=alpha'])
    self.assertFalse(err)
    self.assertTrue('opt' in value.keys())
    self.assertEqual(value['opt'], 'alpha')

    (err, value) = commando.parse('[opt1|opt2]', ['--opt1=alpha', '--opt2=beta'])
    self.assertFalse(err)
    self.assertTrue('opt1' in value.keys())
    self.assertEqual(value['opt1'], 'alpha')
    self.assertTrue('opt2' in value.keys())
    self.assertEqual(value['opt2'], 'beta')

    (err, value) = commando.parse('[opt1|opt2]', ['--opt1=alpha'])
    self.assertTrue(err)
    self.assertEqual(value, 'Missing required option: opt2')

    (err, value) = commando.parse('[opt1|<opt2>]', ['--opt1=alpha'])
    self.assertFalse(err)
    self.assertTrue('opt1' in value.keys())
    self.assertEqual(value['opt1'], 'alpha')

  def test_flags(self):
    """ Flag argument test cases. """
    (err, value) = commando.parse('(flag)', ['--flag'])
    self.assertFalse(err)
    self.assertTrue('flag' in value.keys())
    self.assertTrue(value['flag'])

    (err, value) = commando.parse('(flag1|flag2)', ['--flag1'])
    self.assertFalse(err)
    self.assertTrue('flag1' in value.keys())
    self.assertTrue(value['flag1'])
    self.assertTrue('flag2' in value.keys())
    self.assertFalse(value['flag2'])

    (err, value) = commando.parse('(flag)', ['-f'])
    self.assertFalse(err)
    self.assertTrue('flag' in value.keys())
    self.assertTrue(value['flag'])


if __name__ == '__main__':
  unittest.main()
