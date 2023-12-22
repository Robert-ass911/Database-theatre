from pydantic import BaseModel, condecimal
from datetime import datetime

class Customers(BaseModel):
    ID : int
    Name : str
    Surname : str
    E_mail : str

class Seats(BaseModel):
    ID : int
    Order_number : int
    Place_number : int

class Plays(BaseModel):
    ID : int
    Name : str
    Author : str

class Performances(BaseModel):
    ID : int
    name : str
    Date_and_time : datetime
    The_play : int
    Ticket_price : condecimal(decimal_places=2)

class Applications(BaseModel):
    ID : int
    Representation_number : int
    Date_and_time_of_the_application : datetime
    Number_of_tickets : int

class Sales(BaseModel):
    ID : int
    Application_number : int
    Place_number : int
    Buyer_id : int
    The_amount : condecimal(decimal_places=2)