import fastapi

from database.models import Performances
from resolvers import Performances_res


Performances_router = fastapi.APIRouter(prefix='/Performances', tags=["Performances"])


@Performances_router.get(path='/get/one', response_model=dict)
def get_Performance(Performances_ID: int) -> dict:
    return Performances_res.get(Performance_ID = Performances_ID)

@Performances_router.get(path='/get/all', response_model=dict)
def get_Performances() -> dict:
    return Performances_res.get_all()

@Performances_router.get(path='/get/Thenumberofperformancesheld', response_model=dict)
def get_The_number_of_performances_held() -> dict:
    return Performances_res.get_The_number_of_performances_held()

@Performances_router.get(path='/get/Statisticsbytypeofplays', response_model=dict)
def get_Statistics_by_type_of_plays() -> dict:
    return Performances_res.get_Statistics_by_type_of_plays()

@Performances_router.post(path='/new', response_model=dict)
def new_Performance(Performance: Performances) -> dict:
    return Performances_res.new(Performance = Performance)

@Performances_router.put(path='/updateDate_and_time/{Performances_ID}', response_model=dict)
def update_Date_and_time(Performance: Performances) -> dict:
    return Performances_res.update_Date_and_time(Performance = Performance)

@Performances_router.put(path='/updateTicket_price/{Performances_ID}', response_model=dict)
def update_Ticket_price(Performance: Performances) -> dict:
    return Performances_res.update_Ticket_price(Performance = Performance)

@Performances_router.delete(path='/delete/{Performances_ID}', response_model=dict)
def delete_Performance(Performance_ID: int) -> dict:
     return Performances_res.delete(Performance_ID = Performance_ID)