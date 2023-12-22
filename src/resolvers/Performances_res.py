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

def get_The_number_of_performances_held() -> dict:
    res = base_manager.execute(query="""SELECT COUNT(ID) FROM Performances""",
                             many=True)
    return res

def get_Statistics_by_type_of_plays() -> dict:
    res = base_manager.execute(query="""SELECT The_play, COUNT(ID) FROM Performances GROUP BY The_play""",
                             many=True)
    return res


def new(Performance: Performances) -> dict:
    res = base_manager.execute(query="""INSERT INTO Performances(Name, Date_and_time, The_play, Ticket_price) 
                                       VALUES(?, ?, ?, ?)
                                       RETURNING ID""",
                             args=(Performance.Name, Performance.Date_and_time, Performance.The_play, Performance.Ticket_price))
    return res


def update_Date_and_time(Performance: Performances) -> dict:
    res = base_manager.execute(query="""UPDATE Performances
                                        SET Date_and_time = ?
                                        WHERE ID = ?""",
                             args=(Performance.Date_and_time, Performance.ID))
    return res

def update_Ticket_price(Performance: Performances) -> dict:
    res = base_manager.execute(query="""UPDATE Performances
                                        SET Ticket_price = ?
                                        WHERE ID = ?""",
                             args=(Performance.Ticket_price, Performance.ID))
    return res

def delete(Performance_ID: int) -> dict:
    res = base_manager.execute(query="""DELETE FROM Performances WHERE ID = ?""",
                             args=(Performance_ID,))
    return res