from pydantic import BaseModel
from datetime import datetime


class Seats(BaseModel):
    ID : int
    Order_number : int
    Place_number : int

class Plays(BaseModel):
    ID : int
    Name : str
    Author : str
    Descriptions : str

class Performances(BaseModel):
    ID : int
    Name : str
    Date_and_time : datetime
    The_play : int
    Ticket_price : float

class Applications(BaseModel):
    ID : int
    Representation_number : int
    Date_and_time_of_the_application : datetime
    Number_of_tickets : int

class Customers(BaseModel):
    ID : int
    Name : str
    Surname : str
    E_mail : str
    Comments : str

class Sales(BaseModel):
    ID : int
    Application_number : int
    Place_number : int
    Buyer_id : int
    The_amount : float