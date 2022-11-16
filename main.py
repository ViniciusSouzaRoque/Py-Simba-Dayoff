from fastapi import FastAPI, APIRouter
from views import user_router, assets_router, events_router, member_router

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
