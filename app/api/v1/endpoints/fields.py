from fastapi import APIRouter, status
from app.models.field_model import Fields
from app.schemas.field_update import FieldsUpdate
from app.services.fields_service import FieldService
from fastapi.responses import JSONResponse
import json

router = APIRouter()

@router.get("/forms/{form_id}/fields", status_code=status.HTTP_200_OK)
async def get_form_fields(form_id):
    fields = await FieldService.get_fields(form_id)
    return fields

@router.post("/forms/{form_id}/fields", status_code=status.HTTP_201_CREATED)
async def create_form_fields(form_id, field: Fields):
    result = await FieldService.create_form_fields(form_id, field)
    
    if result.modified_count > 0:
        return field.model_dump()
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"ok": False, "message": "No form found"}
        )
    
@router.patch("/forms/{form_id}/fields/{field_id}")
async def update_form_field(form_id, field_id, fields: FieldsUpdate):
    result = await FieldService.patch_form_field(form_id, field_id, fields)
    
    if result:
        return result
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"ok": False, "message": "No form or field found"}
        )

@router.delete("/forms/{form_id}/fields/{field_id}")
async def delete_form_field(form_id, field_id):
    result = await FieldService.delete_form_field(form_id, field_id)
    
    if result:
        return result
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"ok": False, "message": "No form or field found"}
        )