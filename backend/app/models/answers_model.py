from pydantic import BaseModel, Field
from datetime import datetime
from app.models.answer_model import Answer


class Answers(BaseModel):
    submitted_at: datetime = Field(default_factory=datetime.now)
    answers: list[Answer]
    class Config:
        extra = "allow"
    