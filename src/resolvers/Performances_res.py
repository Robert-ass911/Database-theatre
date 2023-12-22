from database.models import Performances
from database.db_manager import base_manager

def get(Performance_ID: int) -> dict:
    res = base_manager.execute(query="""SELECT * FROM Performances WHERE ID = ?""",
                             args=(Performance_ID,))
    return res


def get_all() -> dict:
    res = base_manager.execute(query="""SELECT * FROM Performances""",
                             many=True)
    return res


def new(Performance: Performances) -> dict:
    res = base_manager.execute(query="""INSERT INTO Performances(Name, Date_and_time, The_play, Ticket_price) 
                                       VALUES(?, ?, ?, ?)
                                       RETURNING ID""",
                             args=(Performance.Name, Performance.Date_and_time, Performance.The_play, Performance.Ticket_price))
    return res


def update(Performance: Performances) -> dict:
    res = base_manager.execute(query="""UPDATE Performances
                                        SET Date_and_time = ?
                                        WHERE ID = ?""",
                             args=(Performance.Date_and_time, Performance.ID))
    return res

def delete(Performance_ID: int) -> dict:
    res = base_manager.execute(query="""DELETE FROM Performances WHERE ID = ?""",
                             args=(Performance_ID,))
    return res