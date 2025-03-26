from fastapi import APIRouter, status
from app.models.field_model import Field
from fastapi.responses import JSONResponse
import json

router = APIRouter()

@router.get("/forms/{form_id}/fields")
async def get_form_fields(form_id):
    pass

@router.post("/forms/{form_id}/fields")
async def create_form_fields(form_id):
    pass

@router.patch("/forms/{form_id}/fields/{field_id}")
async def update_form_field(form_id, field_id):
    pass

@router.delete("/forms/{form_id}/fields/{field_id}")
async def delete_form_field(form_id, field_id):
    pass