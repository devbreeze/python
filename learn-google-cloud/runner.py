#!/usr/bin/python
import os
import sys
import unittest


def main():
    sys.path.insert(0, os.environ.get('GAE_SDK'))
    import dev_appserver
    dev_appserver.fix_sys_path()

    suite = unittest.loader.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    main()
