from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.models.answers_model import Answers
from app.models.answer_model import Answer

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
    
    return answers
        