from fastapi import FastAPI
from app.api.v1.endpoints.forms import router as forms_router
from app.api.v1.endpoints.fields import router as fields_router
from app.api.v1.endpoints.answers import router as answers_router
from app.db.mongodb_manager import MongoDBManager
from app.broker.rabbitmq_broker import RabbitMQ
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os
import pika

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await MongoDBManager.create_connection(os.getenv("MONGODB_STRING_CONNECTION"), os.getenv("MONGODB_DATABASE"))
    credentials = pika.PlainCredentials(username=os.getenv("RABBITMQ_USERNAME"), password=os.getenv("RABBITMQ_PASSWORD"))
    connection_parameters = pika.ConnectionParameters(host=os.getenv("RABBITMQ_HOST"), port=os.getenv("RABBITMQ_PORT"), virtual_host=os.getenv("RABBITMQ_VIRTUALHOST"), credentials=credentials)
    channel = RabbitMQ.create_connection(connection_parameters)
    channel.queue_declare(os.getenv("RABBITMQ_QUEUE"))
    
    yield
    
    await MongoDBManager.close_connection()

app = FastAPI(lifespan=lifespan)

app.include_router(forms_router, prefix="/api/v1")
app.include_router(fields_router, prefix="/api/v1")
app.include_router(answers_router, prefix="/api/v1")

@app.get("/api/check")
def check_api():
    return True