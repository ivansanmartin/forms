from fastapi import APIRouter, status
from app.services.form_service import FormService
import json

router = APIRouter()

@router.get('/forms/{form_id}', status_code=status.HTTP_200_OK)
async def get_form(form_id):
    test = await FormService.get_form()
    
    return test

@router.post('/forms', status_code=status.HTTP_200_OK)
async def get_form():
    return {}

@router.patch('/forms', status_code=status.HTTP_200_OK)
async def get_form():
    return {}

@router.delete('/forms', status_code=status.HTTP_200_OK)
async def get_form():
    return {}