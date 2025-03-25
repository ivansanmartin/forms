from fastapi import FastAPI
from app.api.v1.endpoints.forms import router as forms_router

app = FastAPI()

app.include_router(forms_router, prefix="/api/v1")

@app.get("/api/check")
def check_api():
    return True