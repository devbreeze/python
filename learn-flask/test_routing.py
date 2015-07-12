import unittest

from flask import Flask, url_for
from routing import app


class RoutingTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True

    def test_hello(self):
        rv = app.test_client().get('/hello')
        self.assertIn('Hello, World!', rv.data)

    def test_greet(self):
        rv = app.test_client().get('/greet/Flask')
        self.assertIn('Hello, Flask!', rv.data)

    def test_factorial(self):
        rv = app.test_client().get('/factorial/5')
        self.assertIn('5! = 120.', rv.data)

    def test_message(self):
        rv = app.test_client().get('/message')
        self.assertIn('<title>Message</title>', rv.data)
        self.assertIn('<p>Lorem ipsum dolor sit amet', rv.data)

    def test_vote(self):
        rv = app.test_client().post('/vote', data=dict(rating=10))
        self.assertIn('Thanks for Voting!', rv.data)

    def test_url_for(self):
        with app.test_request_context('/'):
            self.assertEqual(url_for('hello'), '/hello')
            self.assertEqual(url_for('greet', name='Flask'), '/greet/Flask')
            self.assertEqual(url_for('factorial', x=5), '/factorial/5')
            self.assertEqual(url_for('static', filename='style.css'), '/static/style.css')

    def test_status_codes(self):
        rv = app.test_client().get('/hello')
        self.assertEqual(rv.status_code, 200)
        rv = app.test_client().get('/Hello')
        self.assertEqual(rv.status_code, 404)
        rv = app.test_client().post('/vote', data=dict(rating=11))
        self.assertEqual(rv.status_code, 400)


if __name__ == '__main__':
    unittest.main()
