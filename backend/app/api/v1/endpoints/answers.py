from fastapi import APIRouter, status
from app.models.answer_model import Answer
from app.models.submitted_model import Submitted
from app.broker.rabbitmq_broker import RabbitMQ
from app.services.answers_service import AnswerService

router = APIRouter()

@router.post("/forms/{form_id}/fields/answers", status_code=status.HTTP_201_CREATED)
async def create_fields_answers(form_id, submitted: Submitted):
    submitted.form_id = form_id
    
    print(submitted)
    
    for index in range(0, len(submitted.answers)):
        for answer in submitted.answers[index].response:
            answer_model = Answer(**dict(answer))
            result = answer_model.validate_value_type(index)
            
            if not result:
                continue
            
            return result
        

    
    channel = RabbitMQ.get_channel()
    
    print(submitted)
    
    AnswerService.send_message_worker(channel, submitted)

    
    return submitted
        