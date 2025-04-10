from fastapi import FastAPI
from app.api.v1.endpoints.forms import router as forms_router
from app.api.v1.endpoints.fields import router as fields_router
from app.api.v1.endpoints.answers import router as answers_router
from app.api.v1.endpoints.metrics import router as metrics_router
from app.db.mongodb_manager import MongoDBManager
from app.broker.rabbitmq_broker import RabbitMQ
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await MongoDBManager.create_connection(os.getenv("MONGODB_STRING_CONNECTION"), os.getenv("MONGODB_DATABASE"))
    
    rabbitmq = RabbitMQ()
    await rabbitmq.connect()

    yield

    await MongoDBManager.close_connection()

app = FastAPI(lifespan=lifespan)

app.include_router(forms_router, prefix="/api/v1")
app.include_router(fields_router, prefix="/api/v1")
app.include_router(answers_router, prefix="/api/v1")
app.include_router(metrics_router, prefix="/api/v1")

@app.get("/api/check")
def check_api():
    return True