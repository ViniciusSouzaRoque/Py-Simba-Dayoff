from fastapi import APIRouter, HTTPException

from services.event_services import EventService
from schemas.schemas import StandardOutput, ErrorOutput
from schemas.event_schemas import EventCreateInput


events_router = APIRouter(prefix='/events')


@events_router.post('/create', description='Route to add DayOffs', response_model=StandardOutput,responses={400: {'model': ErrorOutput}})
async def create_event(event: EventCreateInput):
    try:
        await EventService.create_event(event)
        return {'message': 'Day Off Adicionado!'}
    except Exception as error:
        raise HTTPException(400, {'detail': f'{str(error)}'})
