from sqlalchemy.ext.asyncio.session import async_session

from database.models import Events
from database.connection import async_session
from schemas.event_schemas import EventCreateInput


class EventService:
    async def create_event(event: EventCreateInput):
        async with async_session() as session:
            session.add(Events(
                member_id=event.member_id,
                type=event.type,
                date=event.date,
                start_time=event.start_time,
                end_time=event.end_time,
                warned_peers=event.warned_peers,
                warned_team=event.warned_team,
                warned_leader=event.warned_leader,
                defined_substitute=event.defined_substitute,
                substitute=event.substitute,
                pending_task=event.pending_task,
                document=event.document,
                created_at=event.created_at,
                status=event.status
            ))
            await session.commit()
