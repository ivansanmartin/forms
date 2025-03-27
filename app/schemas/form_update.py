from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.enums.form_status import FormStatus
from app.models.field_model import Fields

class FormUpdate(BaseModel):
    title: str = Field(description="Form title", min_length=2, max_length=100)
    description: Optional[str] = Field(description="Form description", min_length=2, max_length=100, default=None)
    is_public: Optional[bool] = None
    requires_auth: Optional[bool] = None
    status: Optional[FormStatus] = None
    fields: list[Fields] = None
