from pydantic import BaseModel, UrlConstraints, field_validator
from pydantic_core import Url
from fastapi.responses import JSONResponse
from typing_extensions import Annotated
import aiohttp

class SlackNotify(BaseModel):
    webhook_url: Annotated[Url, UrlConstraints(allowed_schemes=["https"])]
    
    @field_validator("webhook_url")
    def convert_url_to_str(cls, value):
        return str(value)
    
    async def validate_webhook(self, form_name):
        try:
            async with aiohttp.ClientSession() as session:
                payload = {
                    "text": f"Webhook validated: now receiving notifications from the *{form_name}*",
                }
                async with session.post(self.webhook_url, json=payload) as response:
                    if not response.ok:
                        return JSONResponse({"ok": False, "message": "The slack webhook url is not valid, read the documentation."})

        except aiohttp.ClientError as err:
            return {"ok": False, "message": f"Request error: {err}", "status_code": 500}