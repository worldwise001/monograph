import unittest
from unittest import mock
from monograph.database import database
from playhouse.db_url import connect

# Create a mock database in memory
@mock.patch('monograph.database.database.db', new=connect("sqlite:///:memory:"))
class BasicDatabaseTests(unittest.TestCase):
    def setUp(self):
        # Currently unneeded
        self.base = database.BaseModel()
        self.user_table = database.User()

    def tearDown(self):
        pass

    def test_basic_db(self):
        database.db.connect() # Should pass
