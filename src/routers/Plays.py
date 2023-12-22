import fastapi

from database.models import Plays
from resolvers import Plays_res


Plays_router = fastapi.APIRouter(prefix='/Plays', tags=["Plays"])


@Plays_router.get(path='/get/{Plays_ID}', response_model=dict)
def get_Play(Plays_ID: int) -> dict:
    return Plays_res.get(Play_ID = Plays_ID)

@Plays_router.get(path='/get', response_model=dict)
def get_Plays() -> dict:
    return Plays_res.get_all()

@Plays_router.post(path='/new', response_model=dict)
def new_Play(Play: Plays) -> dict:
    return Plays_res.new(Play = Play)

@Plays_router.put(path='/updateName/{Plays_ID}', response_model=dict)
def update_Name(Play: Plays) -> dict:
    return Plays_res.update(Play = Play)

@Plays_router.delete(path='/delete/{Plays_ID}', response_model=dict)
def delete_Play(Play_ID: int) -> dict:
     return Plays_res.delete(Play_ID = Play_ID)