from peewee import SqliteDatabase, Model, CharField, ForeignKeyField, TextField, DateTimeField, BooleanField
import datetime


db = SqliteDatabase('artifacts.db')

class BaseModel(Model):
    class Meta:
        database = db

# class User(BaseModel):
#     username = CharField(unique=True)

# class Tweet(BaseModel):
#     user = ForeignKeyField(User, backref='tweets')
#     message = TextField()
#     created_date = DateTimeField(default=datetime.datetime.now)
#     is_published = BooleanField(default=True)

class Artifact(BaseModel):
    prompt = TextField(null=False)
    output = TextField(null=True)
    feedback = TextField(null=True)
    from_artifact = ForeignKeyField('self', backref='artifacts', null=True)

