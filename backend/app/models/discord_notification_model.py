from pydantic import BaseModel, field_validator, HttpUrl
from pydantic_core import Url
from typing_extensions import Annotated
from fastapi.responses import JSONResponse
import aiohttp

class DiscordNotify(BaseModel):
    webhook_url: str

    @field_validator("webhook_url", mode="before")
    @classmethod
    def validate_url(cls, value):
        return str(HttpUrl(value))
    
    async def validate_webhook(self, form_name):        
        try:
            async with aiohttp.ClientSession() as session:
                payload = {
                    "username": "Form Notification",
                    "embeds": [
                        {
                            "title": "Webhook validation",
                            "description": f"Webhook validated: now receiving notifications from the **{form_name}**",
                            "color": 5763719
                        }
                    ]
                }
                async with session.post(self.webhook_url, json=payload) as response:
                    if not response.ok:
                        return JSONResponse({"ok": False, "message": "The discord webhook url is not valid, read the documentation."})
            
        except aiohttp.ClientError as err:
            return {"ok": False, "message": f"Request error: {err}", "status_code": 500}