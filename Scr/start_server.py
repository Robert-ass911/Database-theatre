from database.db_manager import base_manager
import settings
import uvicorn
from fastapi import FastAPI
from routers import Customers, Seats, Plays, Performances, Applications, Sales
from fastapi.responses import RedirectResponse

app = FastAPI(title='teator')

app.include_router(Customers.Customers_router)
app.include_router(Seats.Seats_router)
app.include_router(Plays.Plays_router)
app.include_router(Performances.Performances_router)
app.include_router(Applications.Applications_router)
app.include_router(Sales.Sales_router)

@app.router.get('/')
def start_page() -> RedirectResponse:
    return RedirectResponse('/docs')

if __name__ == "__main__":
    uvicorn.run(app='start_server:app', reload=True, host=settings.HOST, port=settings.PORT)