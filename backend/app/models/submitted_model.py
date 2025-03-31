from pydantic import BaseModel
from app.models.answers_model import Answers
from typing import Optional

class Submitted(BaseModel):
    form_id: Optional[str] = None 
    answers: list[Answers]
    
    class Config:
        extra = "allow"
