from pydantic import BaseModel, Field
from datetime import datetime
import uuid
from uuid import UUID
from models.answers_model import Answer

class Response(BaseModel):
    form_id: UUID = uuid.uuid4
    submitted_at: datetime = Field(default_factory=datetime.now)
    anwers: list[Answer]