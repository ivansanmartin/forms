from pydantic import BaseModel, Field
from app.enums.types import Types
from typing import Optional

class FieldsUpdate(BaseModel):
    question: Optional[str] = Field(min_length=2, max_length=100, default=None)
    description: Optional[str] = Field(min_length=2, max_length=100, default=None)
    type: Optional[Types] = None
    options: Optional[list[str]] = []
    file: Optional[str] = None
    placeholder: Optional[str] = None
    required: Optional[bool] = Field(default=False)