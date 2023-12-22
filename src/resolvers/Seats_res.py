from database.models import Seats
from database.db_manager import base_manager

def get(Seat_ID: int) -> dict:
    res = base_manager.execute(query="""SELECT * FROM Seats WHERE ID = ?""",
                             args=(Seat_ID,))
    return res


def get_all() -> dict:
    res = base_manager.execute(query="""SELECT * FROM Seats""",
                             many=True)
    return res


def new(Seat: Seats) -> dict:
    res = base_manager.execute(query="""INSERT INTO Seats(Order_number, Place_number) 
                                       VALUES(?, ?)
                                       RETURNING ID""",
                             args=(Seat.Order_number, Seat.Place_number))
    return res


def update(Seat: Seats) -> dict:
    res = base_manager.execute(query="""UPDATE Seats
                                        SET Place_number = ?
                                        WHERE ID = ?""",
                             args=(Seat.Place_number, Seat.ID))
    return res


def delete(Seat_ID: int) -> dict:
    res = base_manager.execute(query="""DELETE FROM Seats WHERE ID = ?""",
                             args=(Seat_ID,))
    return res