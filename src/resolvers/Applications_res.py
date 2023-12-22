from database.models import Applications
from database.db_manager import base_manager

def get(Application_ID: int) -> dict:
    res = base_manager.execute(query="""SELECT * FROM Applications WHERE ID = ?""",
                             args=(Application_ID,))
    return res


def get_all() -> dict:
    res = base_manager.execute(query="""SELECT * FROM Applications""",
                             many=True)
    return res


def new(Application: Applications) -> dict:
    res = base_manager.execute(query="""INSERT INTO Applications(Representation_number, Date_and_time_of_the_application, Number_of_tickets) 
                                       VALUES(?, ?, ?)
                                       RETURNING ID""",
                             args=(Application.Representation_number, Application.Date_and_time_of_the_application, Application.Number_of_tickets))
    return res


def update_Number_of_tickets(Application: Applications) -> dict:
    res = base_manager.execute(query="""UPDATE Applications
                                        SET Number_of_tickets = ?
                                        WHERE ID = ?""",
                             args=(Application.Number_of_tickets, Application.ID))
    return res


def delete(Application_ID: int) -> dict:
    res = base_manager.execute(query="""DELETE FROM Applications WHERE ID = ?""",
                             args=(Application_ID,))
    return res