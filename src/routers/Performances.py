import fastapi

from database.models import Performances
from resolvers import Performances_res


Performances_router = fastapi.APIRouter(prefix='/Performances', tags=["Performances"])


@Performances_router.get(path='/get/{Performances_ID}', response_model=dict)
def get_Performance(Performances_ID: int) -> dict:
    return Performances_res.get(Performance_ID = Performances_ID)

@Performances_router.get(path='/get', response_model=dict)
def get_Performances() -> dict:
    return Performances_res.get_all()

@Performances_router.post(path='/new', response_model=dict)
def new_Performance(Performance: Performances) -> dict:
    return Performances_res.new(Performance = Performance)

@Performances_router.put(path='/updateDate_and_time/{Performances_ID}', response_model=dict)
def update_Date_and_time(Performance: Performances) -> dict:
    return Performances_res.update(Performance = Performance)

@Performances_router.delete(path='/delete/{Performances_ID}', response_model=dict)
def delete_Performance(Performance_ID: int) -> dict:
     return Performances_res.delete(Performance_ID = Performance_ID)