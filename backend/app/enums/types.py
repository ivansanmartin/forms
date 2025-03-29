from enum import Enum

class Types(str, Enum):
    TEXT = "text"
    TEXT_AREA = "textarea"
    NUMBER = "number"
    EMAIL = "email"
    DATE = "date"
    RADIO = "radio"
    CHECKBOX = "checkbox"
    SELECT = "select"
    SCALE = "scale"
    FILE = "file"
    PHONE = "phone"