import unittest


class ListTestCase(unittest.TestCase):

    def test_first_item(self):
        a = []
        self.assertIsNone(a[0] if a else None)

        b = [5]
        self.assertEqual(b[0] if b else None, 5)

        c = [4, 6]
        self.assertEqual(c[0] if c else None, 4)


if __name__ == '__main__':
    unittest.main()
