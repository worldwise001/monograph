from peewee import Model, CharField, DateTimeField, MySQLDatabase

# NOTE: It may be more conventional to name this file ORM.py

db = None # *existing* db file to connect to [e.g., MySqlDatabase('db.sql')]
# can be remote

# Database model
class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    # Should we have an numerical ID field or just use username as key?
    username = CharField(unique=True)
    password = CharField
    email = CharField
    join_date = DateTimeField
    update_data = DateTimeField # Last time user was updated

    # Other field ideas:
    # - Google scholar ID
    # - Home institution URL
    
    # TODO: Convenience methods go here (e.g., get relationships to other tables)


# TODO other tables