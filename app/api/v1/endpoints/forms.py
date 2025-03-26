from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.services.form_service import FormService
from app.models.form_model import Form

router = APIRouter()

@router.get("/forms/{form_id}", status_code=status.HTTP_200_OK)
async def get_form(form_id):
    form = await FormService.get_form(form_id)
    
    if not form:
        return JSONResponse(
            status_code=404,
            content={"ok": False, "message": "No form found"}
        )
    
    return form
    
@router.post("/forms", status_code=status.HTTP_201_CREATED)
async def create_form(form: Form):
    form = await FormService.create_form(form)
    return form

@router.patch("/forms/{form_id}")
async def patch_form():
    return {}

@router.delete("/forms/{form_id}")
async def delete_form():
    return {}