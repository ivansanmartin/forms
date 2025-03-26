from pydantic import BaseModel, Field
from app.enums.types import Types
import uuid
from uuid import UUID
from typing import Optional

class Fields(BaseModel):
    field_id: UUID = Field(default_factory=uuid.uuid4)
    form_id: UUID
    question: str = Field(min_length=2, max_length=100)
    description: Optional[str] = Field(min_length=2, max_length=100)
    type: Types
    options: Optional[list[str]] = []
    file: Optional[str] = None
    placeholder: Optional[str] = None
    required: bool = Field(default=False)