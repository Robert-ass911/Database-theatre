from peewee import Model, CharField, IntegerField, ForeignKeyField
from peewee import *  
import settings


db = SqliteDatabase(database=f'{settings.DATABASE_PATH}/{settings.DATABASE_NAME}')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    position = CharField(default='')
    login = CharField(default='')
    password = CharField(default='')
    power_level = IntegerField(default=0)

class Plays(BaseModel):
    name = CharField(default='')
    price = CharField(default='')
    description = CharField(default='')

class Applications(BaseModel):
    date = CharField(default='')
    play_id = ForeignKeyField(Plays, backref='applications', default=0)
    count_tickets = IntegerField(default=0)

class Performances(BaseModel):
    name = CharField(default='')
    date = CharField(default='')
    play_id = ForeignKeyField(Plays, backref='performances', default=0)
    price = IntegerField(default=0)

class Customers(BaseModel):
    performance_id = ForeignKeyField(Performances, backref='applications', default=0)
    fio = CharField(default='')
    email = CharField(default='')

class Seats(BaseModel):
    place_num = IntegerField(default=0)
    order_num = IntegerField(default=0)

class Sales(BaseModel):
    Application_number = ForeignKeyField(Applications, backref='Applications', default=0)
    Place_number = ForeignKeyField(Seats, backref='Seats', default=0)
    Buyer_id = ForeignKeyField(Customers, backref='Customers', default=0)
    The_amount = CharField(default='')

db.create_tables([User, Customers, Seats, Applications, Performances, Plays, Sales])