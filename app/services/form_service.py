from app.crud.form_crud import FormCrud
from app.models.form_model import Form
from app.schemas.form_update import FormUpdate


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
    async def patch_form(form_id, form_update: FormUpdate):
        new_form = await FormCrud.patch_form(form_id, form_update.model_dump(exclude_unset=True))
        return new_form
    
    @staticmethod
    async def delete_form(form_id):
        result = await FormCrud.delete_form(form_id)
        return result