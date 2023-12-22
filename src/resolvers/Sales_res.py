from database.models import Sales
from database.db_manager import base_manager

def get(Sale_ID: int) -> dict:
    res = base_manager.execute(query="""SELECT * FROM Sales WHERE ID = ?""",
                             args=(Sale_ID,))
    return res


def get_all() -> dict:
    res = base_manager.execute(query="""SELECT * FROM Sales""",
                             many=True)
    return res


def new(Sale: Sales) -> dict:
    res = base_manager.execute(query="""INSERT INTO Sales(Application_number, Place_number, Buyer_id, The_amount) 
                                       VALUES(?, ?, ?, ?)
                                       RETURNING ID""",
                             args=(Sale.Application_number, Sale.Place_number, Sale.Buyer_id, Sale.The_amount))
    return res


def update(Sale: Sales) -> dict:
    res = base_manager.execute(query="""UPDATE Sales
                                        SET The_amount = ?
                                        WHERE ID = ?""",
                             args=(Sale.The_amount, Sale.ID))
    return res


def delete(Sale_ID: int) -> dict:
    res = base_manager.execute(query="""DELETE FROM Sales WHERE ID = ?""",
                             args=(Sale_ID,))
    return res