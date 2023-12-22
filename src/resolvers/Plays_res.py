from database.models import Plays
from database.db_manager import base_manager

def get(Play_ID: int) -> dict:
    res = base_manager.execute(query="""SELECT * FROM Plays WHERE ID = ?""",
                             args=(Play_ID,))
    return res


def get_all() -> dict:
    res = base_manager.execute(query="""SELECT * FROM Plays""",
                             many=True)
    return res


def new(Play: Plays) -> dict:
    res = base_manager.execute(query="""INSERT INTO Plays(Name, Author) 
                                       VALUES(?, ?)
                                       RETURNING ID""",
                             args=(Play.Name, Play.Author))
    return res


def update(Play: Plays) -> dict:
    res = base_manager.execute(query="""UPDATE Plays
                                        SET Name = ?
                                        WHERE ID = ?""",
                             args=(Play.Name, Play.ID))
    return res


def delete(Play_ID: int) -> dict:
    res = base_manager.execute(query="""DELETE FROM Plays WHERE ID = ?""",
                             args=(Play_ID,))
    return res