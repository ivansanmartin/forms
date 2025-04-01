from pydantic import BaseModel
from fastapi.responses import JSONResponse
import aiohttp

class DiscordNotify(BaseModel):
    webhook_url: str
    
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
                        return JSONResponse({"ok": False, "message": "The webhook url is not valid, read the documentation."})
                    
        except aiohttp.ClientError as err:
            return {"ok": False, "message": f"Request error: {err}", "status_code": 500}