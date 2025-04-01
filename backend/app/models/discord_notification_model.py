from pydantic import BaseModel, UrlConstraints, field_validator
from pydantic_core import Url
from typing_extensions import Annotated
from fastapi.responses import JSONResponse
import aiohttp

class DiscordNotify(BaseModel):
    webhook_url: Annotated[Url, UrlConstraints(allowed_schemes=["https"])]
    
    @field_validator("webhook_url")
    def convert_url_to_str(cls, value):
        return str(value)
    
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