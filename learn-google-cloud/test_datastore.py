import unittest

from google.appengine.ext import ndb
from google.appengine.ext import testbed


class Config(ndb.Model):
    secretKey = ndb.StringProperty()


class DatastoreTestCase(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        ndb.get_context().clear_cache()

    def tearDown(self):
        self.testbed.deactivate()

    def test_config(self):
        query = Config.query()
        results = query.fetch(1)
        self.assertTrue(not results)


if __name__ == '__main__':
    unittest.main()
