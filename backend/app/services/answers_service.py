from app.models.submitted_model import Submitted
from app.broker.rabbitmq_broker import RabbitMQ
from app.crud.forms_crud import FormCrud
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os

load_dotenv()

class AnswerService:
    """
    Class responsible for handling the sending of answer messages 
    through a RabbitMQ communication channel.

    Methods:
    --------
    send_message_worker(submitted: Submitted):
        Sends a message to the consumer with the submitted serialized in JSON format.
    """
    
    @staticmethod
    async def send_message_worker(submitted: Submitted):
        form = await FormCrud.get_form(submitted.form_id)
        
        if not form:
            return JSONResponse({"ok": False, "message": "No form found"})

        await RabbitMQ.send_message(submitted.model_dump_json())
        return submitted
            

