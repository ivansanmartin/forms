from fastapi import APIRouter, status
from app.services.form_service import FormService
from app.models.form_model import Form

router = APIRouter()

@router.get('/forms/{form_id}', status_code=status.HTTP_200_OK)
async def get_form(form_id):
    test = await FormService.get_form()
    
    return test

@router.post('/forms', status_code=status.HTTP_200_OK)
async def create_form(form: Form):
    await FormService.create_form(form)
    return {"data": form}

@router.put('/forms', status_code=status.HTTP_200_OK)
async def update_form():
    return {}

@router.patch("/forms", status_code=status.HTTP_200_OK)
async def patch_form():
    return {}

@router.delete('/forms', status_code=status.HTTP_200_OK)
async def delete_form():
    return {}