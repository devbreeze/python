#!/usr/bin/python

import unittest


def main():
    suite = unittest.loader.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    main()
