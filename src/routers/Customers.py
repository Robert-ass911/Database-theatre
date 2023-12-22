import fastapi

from database.models import Customers
from resolvers import Customers_res


Customers_router = fastapi.APIRouter(prefix='/Customers', tags=["Customers"])


@Customers_router.get(path='/get/{Customers_ID}', response_model=dict)
def get_Customer(Customers_ID: int) -> dict:
    return Customers_res.get(Customer_ID = Customers_ID)

@Customers_router.get(path='/get', response_model=dict)
def get_Customers() -> dict:
    return Customers_res.get_all()

@Customers_router.post(path='/new', response_model=dict)
def new_Customer(Customer: Customers) -> dict:
    return Customers_res.new(Customer = Customer)

@Customers_router.put(path='/updateName/{Customers_ID}', response_model=dict)
def update_Name(Customer: Customers) -> dict:
    return Customers_res.update(Customer = Customer)

@Customers_router.delete(path='/delete/{Customers_ID}', response_model=dict)
def delete_Customer(Customer_ID: int) -> dict:
     return Customers_res.delete(Customer_ID = Customer_ID)