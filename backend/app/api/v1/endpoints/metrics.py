from fastapi import APIRouter, status

router = APIRouter();

@router.get("/forms/metrics/{public_code}", status_code=status.HTTP_200_OK)
async def get_form_metrics(public_code):
    pass