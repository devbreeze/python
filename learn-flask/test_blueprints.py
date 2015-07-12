import unittest

from flask import Flask
from blueprints import app


class BlueprintsTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True

    def test_index(self):
        rv = app.test_client().get('/')
        self.assertIn('<h1>Index</h1>', rv.data)

    def test_admin_index(self):
        rv = app.test_client().get('/admin/')
        self.assertIn('<h1>Admin Index</h1>', rv.data)


if __name__ == '__main__':
    unittest.main()
