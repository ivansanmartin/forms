from fastapi import FastAPI
from app.api.v1.endpoints.forms import router as forms_router
from app.api.v1.endpoints.fields import router as fields_router
from app.db.mongodb_manager import MongoDBManager
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await MongoDBManager.create_connection("mongodb://root:th0sdl2uxvtPPY@local.ivansanmartin.dev:30620/", "forms")
    
    yield
    
    await MongoDBManager.close_connection()

app = FastAPI(lifespan=lifespan)

app.include_router(forms_router, prefix="/api/v1")
app.include_router(fields_router, prefix="/api/v1")

@app.get("/api/check")
def check_api():
    return True