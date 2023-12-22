from database.models import Customers
from database.db_manager import base_manager

def get(Customer_ID: int) -> dict:
    res = base_manager.execute(query="""SELECT * FROM Customers WHERE ID = ?""",
                             args=(Customer_ID,))
    return res


def get_all() -> dict:
    res = base_manager.execute(query="""SELECT * FROM Customers""",
                             many=True)
    return res


def new(Customer: Customers) -> dict:
    res = base_manager.execute(query="""INSERT INTO Customers(Name, Surname, E_mail, Comments) 
                                       VALUES(?, ?, ?, ?)
                                       RETURNING ID""",
                             args=(Customer.Name, Customer.Surname, Customer.E_mail, Customer.Comments))
    return res


def update(Customer: Customers) -> dict:
    res = base_manager.execute(query="""UPDATE Customers
                                        SET Name = ?
                                        WHERE ID = ?""",
                             args=(Customer.Name, Customer.ID))
    return res


def delete(Customer_ID: int) -> dict:
    res = base_manager.execute(query="""DELETE FROM Customers WHERE ID = ?""",
                             args=(Customer_ID,))
    return res