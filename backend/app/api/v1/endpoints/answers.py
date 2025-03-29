from fastapi import APIRouter, status
from app.models.answers_model import Answers
from app.models.answer_model import Answer
from app.broker.rabbitmq_broker import RabbitMQ
import ast

router = APIRouter()

@router.post("/forms/{form_id}/fields/answers", status_code=status.HTTP_201_CREATED)
async def create_fields_answers(form_id, answers: Answers):
    answers.form_id = form_id
    
    for answer in answers.answers:
        answer_model = Answer(**dict(answer))
        result = answer_model.validate_value_type()
        
        if not result:
            continue
         
        return result
    
    channel = RabbitMQ.get_channel()
    
    channel.basic_publish(
        exchange="",
        routing_key="answers",
        body=str(answers.model_dump())
    )
    
    print("[x] Sent result to consumer")
    
    return answers
        