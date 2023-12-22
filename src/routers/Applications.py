import fastapi

from database.models import Applications
from resolvers import Applications_res


Applications_router = fastapi.APIRouter(prefix='/Applications', tags=["Applications"])


@Applications_router.get(path='/get/{Applications_ID}', response_model=dict)
def get_Application(Applications_ID: int) -> dict:
    return Applications_res.get(Application_ID = Applications_ID)

@Applications_router.get(path='/get', response_model=dict)
def get_Applications() -> dict:
    return Applications_res.get_all()

@Applications_router.post(path='/new', response_model=dict)
def new_Application(Application: Applications) -> dict:
    return Applications_res.new(Application = Application)

@Applications_router.put(path='/updateNumber_of_tickets/{Applications_ID}', response_model=dict)
def update_Number_of_tickets(Application: Applications) -> dict:
    return Applications_res.update(Application = Application)

@Applications_router.delete(path='/delete/{Applications_ID}', response_model=dict)
def delete_Application(Application_ID: int) -> dict:
     return Applications_res.delete(Application_ID = Application_ID)