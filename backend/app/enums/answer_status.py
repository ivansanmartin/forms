from enum import Enum

class AnswerStatus(str, Enum):
    COMPLETED = "completed"
    PARTIAL = "partial"
    ABANDONED = "abandoned"