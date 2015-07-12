import unittest

from itertools import count


class ItertoolsTestCase(unittest.TestCase):

    def test_count(self):
        a = count(1)

        b = []
        c = b[0] if b else a.next()
        self.assertEqual(c, 1)

        d = [5]
        e = d[0] if d else a.next()
        self.assertEqual(e, 5)

        f = a.next()
        self.assertEqual(f, 2)


if __name__ == '__main__':
    unittest.main()
