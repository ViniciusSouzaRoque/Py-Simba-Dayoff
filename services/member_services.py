from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy import delete
from sqlalchemy.future import select

from database.models import Member
from database.connection import async_session
from schemas.member_schemas import MemberCreateInput
from providers.hash_provider import gerar_hash


class MemberService:
    async def create_member(user: MemberCreateInput):
        async with async_session() as session:
            session.add(Member(
                first_name=user.first_name,
                last_name=user.last_name,
                cpf=user.cpf,
                email=user.email,
                password=gerar_hash(user.password),
                zip=user.zip,
                birthday=user.birthday,
                street=user.street,
                number=user.number,
                district=user.district,
                state=user.state,
                country=user.country,
                has_children=user.has_children,
                children_qty=user.children_qty,
                children_names=user.children_names,
                marital_state=user.marital_state,
                created_at=user.created_at

            ))
            await session.commit()
