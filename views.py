from fastapi import APIRouter


user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')
member_router = APIRouter(prefix='/member')
events_router = APIRouter(prefix='/events')
