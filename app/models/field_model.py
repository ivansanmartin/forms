from pydantic import BaseModel, Field
from enums.types import Types
import uuid
from uuid import UUID
from typing import Optional

class Fields(BaseModel):
    field_id: UUID = uuid.uuid4
    form_id: UUID
    question: str = Field(min_length=2, max_length=100)
    description: Optional[str] = Field(min_length=2, max_length=100)
    type: Types
    options: Optional[list[str]]
    file: Optional[str]
    placeholder: Optional[str]
    required: bool = Field(default=False)