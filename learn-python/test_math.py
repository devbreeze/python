import math
import unittest


class MathTestCase(unittest.TestCase):

    def test_factorial(self):
        a = 5
        b = math.factorial(a)
        self.assertEqual(b, 120)


if __name__ == '__main__':
    unittest.main()
