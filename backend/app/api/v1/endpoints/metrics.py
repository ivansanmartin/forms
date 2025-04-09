from fastapi import APIRouter, status
from app.services.forms_metrics_service import FormMetricService
from pprint import pprint

router = APIRouter();

@router.get("/forms/metrics/{public_code}", status_code=status.HTTP_200_OK)
async def get_form_metrics(public_code):
    result = await FormMetricService.get_form_metrics(public_code)
    
    return {"ok": result}