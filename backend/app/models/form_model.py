from pydantic import BaseModel, Field
from datetime import datetime
from app.enums.form_status import FormStatus
from app.models.field_model import Fields
from app.models.discord_notification_model import DiscordNotify
from app.models.slack_notification_model import SlackNotify
from typing import Optional
import uuid

class Form(BaseModel):
    form_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    public_code: str = Field(default_factory=lambda: str(uuid.uuid4().hex)[:6])
    title: str = Field(description="Form title", min_length=2, max_length=100)
    description: str = Field(description="Form description", min_length=2, max_length=100)
    created_by: str = Field(description="Form creator", min_length=2, max_length=100)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    is_public: bool = Field(default=False)
    requires_auth: bool = Field(default=False)
    discord_notification: Optional[DiscordNotify] = None
    slack_notification: Optional[SlackNotify] = None
    status: FormStatus
    fields: list[Fields] = []