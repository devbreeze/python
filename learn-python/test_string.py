import unittest


class StringTestCase(unittest.TestCase):

    def test_formatting(self):
        a = 5
        b = 120
        c = '%d! = %d.' % (a, b)
        self.assertEqual(c, '5! = 120.')


if __name__ == '__main__':
    unittest.main()
