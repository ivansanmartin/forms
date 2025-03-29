from enum import Enum
from datetime import date
from typing import Any, Type

class ValidateTypes(str, Enum):
    TEXT = "text", str, ""
    TEXT_AREA = "textarea", str, ""
    NUMBER = "number", int, 0
    EMAIL = "email", str, ""
    DATE = "date", date, None
    RADIO = "radio", list, []
    CHECKBOX = "checkbox", list, []
    SELECT = "select", list, []
    SCALE = "scale", int, 0
    FILE = "file", str, ""
    PHONE = "phone", str, ""

    def __new__(cls, value: str, data_type: Type, default_value: Any):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj._data_type = data_type
        obj._default_value = default_value
        return obj

    @property
    def data_type(self) -> Type:
        return self._data_type

    @property
    def default_value(self) -> Any:
        return self._default_value
