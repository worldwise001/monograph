from monograph.database import database as orm
from peewee import SqliteDatabase
import unittest


class DatabaseUserTests(unittest.TestCase):
    def setUp(self) -> None:
        mock_db = SqliteDatabase(':memory:')
        orm.db.initialize(mock_db)
        orm.db.connect()
        orm.db.create_tables([orm.User])

    def tearDown(self) -> None:
        pass

    # Helper function to add a user whose username is "Joe"
    def add_joe(self) -> orm.User:
        joe = orm.User(username="Joe", password="123", email="joe@test.test")
        joe.save()  # Should pass
        return joe

    def test_basic_db(self) -> None:
        self.assertIsNot(orm.db, None)

    def test_add_user(self) -> None:
        self.add_joe()
        self.assertEqual(len(orm.User.select()), 1)  # There is now 1 user

    def test_delete_user(self) -> None:
        self.add_joe()
        joe = orm.User.get(orm.User.username == "Joe")
        joe.delete_instance()
        self.assertEqual(len(orm.User.select()), 0)  # db should be empty

    def test_email_change(self) -> None:
        joe = self.add_joe()
        old_email = joe.email
        new_email = "joe@test1.test1"
        joe.change_email(new_email)
        self.assertEqual(joe.email, new_email)  # email should have changed
        self.assertNotEqual(joe.email, old_email)
