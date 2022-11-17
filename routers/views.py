from typing import List

from fastapi import APIRouter, HTTPException
from services.services import UserService, FavoriteService
from services.member_services import MemberService
from schemas.member_schemas import MemberCreateInput

from schemas.schemas import UserCreateInput, StandardOutput, ErrorOutput, UserFavoriteAddInput, UserFavoriteRemove, \
    UserListOutput

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')
member_router = APIRouter(prefix='/member')
events_router = APIRouter(prefix='/events')


@user_router.post('/create', description='Route to add users', response_model=StandardOutput,
                  responses={400: {'model': ErrorOutput}})
async def user_create(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return {'message': 'Ok'}
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.delete('/delete/{user_id}')
async def user_delete(user_id: int):
    try:
        await UserService.delete_user(user_id)
        return {'message': 'Ok'}
    except Exception as error:
        raise HTTPException(400, {'detail': f'{str(error)}'})


@user_router.post('/favorite/add')
async def user_favorite_add(favorite_add: UserFavoriteAddInput):
    try:
        await FavoriteService.create_favorite(user_id=favorite_add.user_id, symbol=favorite_add.symbol)
        return {'message': 'Favorite added'}
    except Exception as error:
        raise HTTPException(400, {'detail': f'{str(error)}'})


@user_router.delete('/favorite/delete')
async def user_favorite_remove(remove_favorite: UserFavoriteRemove):
    try:
        await FavoriteService.delete_favorite(user_id=remove_favorite.user_id, symbol=remove_favorite.symbol)
        return {'message': 'Favorite removed'}
    except Exception as error:
        raise HTTPException(400, {'detail': f'{str(error)}'})


@user_router.get('/list', response_model=List[UserListOutput])
async def user_list():
    try:
        return await UserService.list_user()
    except Exception as error:
        raise HTTPException(400, {'detail': f'{str(error)}'})


@member_router.post('/create', description='Route to add users', response_model=StandardOutput,
                  responses={400: {'model': ErrorOutput}})
async def create_member(user: MemberCreateInput):
    try:
        await MemberService.create_member(
            user)
        return {'message': 'Show!'}
    except Exception as error:
        raise HTTPException(400, {'detail': f'{str(error)}'})

