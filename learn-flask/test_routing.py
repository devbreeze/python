import unittest

from flask import Flask, url_for
from routing import app


class RoutingTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

    def test_helloworld(self):
        rv = app.test_client().get('/helloworld')
        self.assertIn('Hello, World!', rv.data)

    def test_hellovariable(self):
        rv = app.test_client().get('/hellovariable/Flask')
        self.assertIn('Hello, Flask!', rv.data)

    def test_hellotemplate(self):
        rv = app.test_client().get('/hellotemplate')
        self.assertIn('<title>Message</title>', rv.data)
        self.assertIn('<p>Lorem ipsum dolor sit amet', rv.data)

    def test_hellopost(self):
        rv = app.test_client().post('/hellopost', data=dict(name='Flask'))
        self.assertIn('Hello, Flask!', rv.data)

    def test_helloform(self):
        rv = app.test_client().get('/helloform')
        self.assertIn('<form ', rv.data)
        self.assertIn(' action="/helloform"', rv.data)
        rv = app.test_client().post('/helloform')
        self.assertIn('This field is required.', rv.data)
        rv = app.test_client().post('/helloform', data=dict(name='Flask'))
        self.assertIn('Hello, Flask!', rv.data)

    def test_url_for(self):
        with app.test_request_context('/'):
            self.assertEqual(url_for('helloworld'), '/helloworld')
            self.assertEqual(url_for('hellovariable', name='Flask'), '/hellovariable/Flask')
            self.assertEqual(url_for('static', filename='style.css'), '/static/style.css')

    def test_status_codes(self):
        rv = app.test_client().get('/helloworld')
        self.assertEqual(rv.status_code, 200)
        rv = app.test_client().post('/hellopost')
        self.assertEqual(rv.status_code, 400)
        rv = app.test_client().get('/HelloWorld')
        self.assertEqual(rv.status_code, 404)
        rv = app.test_client().post('/helloworld')
        self.assertEqual(rv.status_code, 405)


if __name__ == '__main__':
    unittest.main()
