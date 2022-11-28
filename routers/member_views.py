from typing import List

from fastapi import APIRouter, HTTPException
from schemas.member_schemas import MemberCreateInput, MemberListOutput
from schemas.schemas import ErrorOutput, StandardOutput
from services.member_services import MemberService

member_router = APIRouter(prefix='/member')


@member_router.post('/create', description='Route to add users', response_model=StandardOutput,
                  responses={400: {'model': ErrorOutput}})
async def create_member(user: MemberCreateInput):
    try:
        await MemberService.create_member(
            user)
        return {'message': 'Show!'}
    except Exception as error:
        raise HTTPException(400, {'detail': f'{str(error)}'})


@member_router.get('/list', response_model=List[MemberListOutput])
async def member_list():
    try:
        return await MemberService.list_member()
    except Exception as error:
        raise HTTPException(400, {'detail': f'{str(error)}'})
