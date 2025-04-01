from pydantic import BaseModel
from fastapi.responses import JSONResponse
import requests


class DiscordNotify(BaseModel):
    webhook_url: str
    
    def validate_webhook(self, form_name):
        try:
            response = requests.post(self.webhook_url, json={
                "username": "Form Notification",
                "embeds": [
                    {
                        "title": "Webhook validation",
                        "description": f"Webhook validated: now receiving notifications from the **{form_name}**",
                        "color": 5763719
                    }
                ]
            })
            
            if not response.ok:
                return JSONResponse({"ok": False, "message": "The webhook url is not valid, read the documentation."})
            
        except requests.exceptions.HTTPError as errh:
            return JSONResponse({"ok": False, "message": f"HTTP error: {errh}"}, status_code=response.status_code if response else 400)
        except requests.exceptions.ConnectionError as errc:
            return JSONResponse({"ok": False, "message": f"Connection error: {errc}"}, status_code=503)
        except requests.exceptions.Timeout as errt:
            return JSONResponse({"ok": False, "message": f"Timeout error: {errt}"}, status_code=504)
        except requests.exceptions.RequestException as err:
            return JSONResponse({"ok": False, "message": f"Unexpected error: {err}"}, status_code=500)
