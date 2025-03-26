from app.crud.form_crud import FormCrud
from app.models.form_model import Form
import json


class FormService():
    @staticmethod
    async def get_form(form_id):
        form = await FormCrud.get_form(form_id)
        
        if not form:
            return None
            
        return Form.model_validate(form).model_dump()

    @staticmethod
    async def create_form(form: Form):
        await FormCrud.create_form(form)
        return Form.model_validate(form)
        
    @staticmethod
    async def update_form():
        pass
    
    @staticmethod
    async def patch_form():
        pass
    
    @staticmethod
    async def delete_form():
        pass