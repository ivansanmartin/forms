from fastapi import APIRouter, status

router = APIRouter()

@router.get('/forms/{form_id}', status_code=status.HTTP_200_OK)
async def get_form(form_id):
    return {form_id}

@router.post('/forms', status_code=status.HTTP_200_OK)
async def get_form():
    return {}

@router.patch('/forms', status_code=status.HTTP_200_OK)
async def get_form():
    return {}

@router.delete('/forms', status_code=status.HTTP_200_OK)
async def get_form():
    return {}