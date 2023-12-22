import fastapi

from database.models import Sales
from resolvers import Sales_res


Sales_router = fastapi.APIRouter(prefix='/Sales', tags=["Sales"])


@Sales_router.get(path='/get/{Sales_ID}', response_model=dict)
def get_Sale(Sales_ID: int) -> dict:
    return Sales_res.get(Sale_ID = Sales_ID)

@Sales_router.get(path='/get', response_model=dict)
def get_Sales() -> dict:
    return Sales_res.get_all()

@Sales_router.post(path='/new', response_model=dict)
def new_Sale(Sale: Sales) -> dict:
    return Sales_res.new(Sale = Sale)

@Sales_router.put(path='/updateThe_amount/{Sales_ID}', response_model=dict)
def update_The_amount(Sale: Sales) -> dict:
    return Sales_res.update(Sale = Sale)

@Sales_router.delete(path='/delete/{Sales_ID}', response_model=dict)
def delete_Sale(Sale_ID: int) -> dict:
     return Sales_res.delete(Sale_ID = Sale_ID)