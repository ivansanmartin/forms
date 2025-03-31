from pydantic import BaseModel
from app.enums.validate_data_types import ValidateTypes
from typing import Union
from fastapi.responses import JSONResponse


class Answer(BaseModel):
    field_id: str
    type: ValidateTypes
    value: Union[str, int, bool, list]
    
    def validate_value_type(self, position):
        expected_type = ValidateTypes[str(self.type.value).upper()].data_type
        
        if not isinstance(self.value, expected_type):
            return JSONResponse({"error": f"Invalid value in position {position}: {self.value} should be of type {expected_type}"})
