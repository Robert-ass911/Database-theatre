from pydantic import BaseModel
from typing import Optional


class ModifyBaseModel(BaseModel):
    id: Optional[int] = 0


class ChangePassword(ModifyBaseModel):
    password: str


class LoginData(ModifyBaseModel):
    login: str
    password: str


class User(ModifyBaseModel):
    position: str
    login: str
    password: str
    power_level: int 

class Plays(BaseModel):
    name: str = ''
    price: str = ''
    description: str = ''

class Applications(BaseModel):
    date: str = ''
    play_id: int = 0
    count_tickets: int = 0

class Performances(BaseModel):
    name: str = ''
    date: str = ''
    play_id: int = 0
    price: int = 0

class Customers(BaseModel):
    performance_id: int = 0
    fio: str = ''
    email: str = ''

class Seats(BaseModel):
    place_num: int = 0
    order_num: int = 0

class Sales(BaseModel):
    Application_number: int= 0
    Place_number: int = 0
    Buyer_id: int = 0
    The_amount: str = ''

