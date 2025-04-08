from app.models.answer_model import Answer
from app.enums.answer_status import AnswerStatus
from pydantic import BaseModel, Field
from datetime import datetime


class Answers(BaseModel):
    submitted_at: datetime = Field(default_factory=datetime.now)
    started_at: datetime = None
    fill_time: int = None
    status: AnswerStatus = None
    num_responses: int = None
    user_agent: str = None
    ip_address: str = None
    location: str = None
    referrer: str = None
    response: list[Answer]
    