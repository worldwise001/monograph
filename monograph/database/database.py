from peewee import Model, CharField, DateTimeField, DatabaseProxy
from datetime import datetime
from typing import Any

# NOTE: It may be more conventional to name this file ORM.py

db = DatabaseProxy()  # Set to DatabaseProxy() to enable setting db at runtime
# There are other ways to do this
# http://docs.peewee-orm.com/en/latest/peewee/database.html#setting-the-database-at-run-time


# Base Database model, actual models should inherit this
class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    def __init__(self, *args: str, **kwargs: str):  # PLEASE CHECK
        super(User, self).__init__(*args, **kwargs)
        now = datetime.now()
        self.join_date = now
        self.last_changed = now

    # Should we have an numerical ID field or just use username as key?
    username = CharField(unique=True)
    password = CharField
    email = CharField
    join_date = DateTimeField
    last_changed = DateTimeField  # Last time user was updated

    # Other field ideas:
    # - Google scholar ID
    # - Home institution URL

    def update_last_changed(self) -> None:
        self.last_changed = datetime.today()

    # NOT WORKING! DOES NOT DO ANYTHING
    def change_password(self, new_password: str) -> bool:
        if is_good_password(new_password):
            # TODO: hash the passwords
            return True
        else:
            return False

    def change_email(self, new_email: str) -> bool:
        if is_good_email(new_email):
            self.email = new_email
            self.update_last_changed()
            return True
        else:
            return False
    # Should we be using getters as well?

    # TODO: Convenience methods go here (e.g., get relationships to other tables)


def is_good_email(email: str) -> bool:
    # TODO: complete
    return True


def is_good_password(password: str) -> bool:
    # TODO: complete
    return True

# TODO other tables
