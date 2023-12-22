import fastapi

from database.models import Seats
from resolvers import Seats_res


Seats_router = fastapi.APIRouter(prefix='/Seats', tags=["Seats"])


@Seats_router.get(path='/get/{Seats_ID}', response_model=dict)
def get_Seat(Seats_ID: int) -> dict:
    return Seats_res.get(Seat_ID = Seats_ID)

@Seats_router.get(path='/get', response_model=dict)
def get_Seats() -> dict:
    return Seats_res.get_all()

@Seats_router.post(path='/new', response_model=dict)
def new_Seat(Seat: Seats) -> dict:
    return Seats_res.new(Seat = Seat)

@Seats_router.put(path='/updatePlace_number/{Seats_ID}', response_model=dict)
def update_Place_number(Seat: Seats) -> dict:
    return Seats_res.update(Seat = Seat)

@Seats_router.delete(path='/delete/{Seats_ID}', response_model=dict)
def delete_Seat(Seat_ID: int) -> dict:
     return Seats_res.delete(Seat_ID = Seat_ID)