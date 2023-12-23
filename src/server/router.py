from src.server.database import pydantic_models, database_models
from src.server.service import RouterManager


routers = (
    RouterManager(pydantic_model=pydantic_models.Performances, database_model=database_models.Performances, prefix='/performances', tags=['Performances']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Plays, database_model=database_models.Plays, prefix='/plays', tags=['Plays']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Customers, database_model=database_models.Customers, prefix='/customers', tags=['Customers']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Seats, database_model=database_models.Seats, prefix='/seats', tags=['Seats']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.User, database_model=database_models.User, prefix='/users', tags=['Users']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Applications, database_model=database_models.Applications, prefix='/applications', tags=['Applications']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Sales, database_model=database_models.Sales, prefix='/sales', tags=['Sales']).fastapi_router
)
