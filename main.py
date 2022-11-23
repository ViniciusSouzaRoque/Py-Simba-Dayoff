from fastapi import FastAPI, APIRouter
from routers.views import user_router, assets_router, member_router
from routers.event_views import events_router
app = FastAPI()
router = APIRouter()

@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(prefix='/first', router=router)
app.include_router(user_router)
app.include_router(assets_router)
app.include_router(events_router)
app.include_router(member_router)
