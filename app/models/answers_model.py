from pydantic import BaseModel, Field
from uuid import UUID
from typing import Union

class Answer(BaseModel):
    field_id: UUID
    answer: Union[str, int, list]