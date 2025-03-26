from app.crud.form_crud import FormCrud
from app.models.form_model import Form

class FormService():
    @staticmethod
    async def get_form():
        form = await FormCrud.get_form()
        return form

    @staticmethod
    async def create_form(form: Form):
        if len(form.fields) > 0:
            print(form.form_id)
            print("fields of forms is not empty")
            print(form.fields)
        await FormCrud.create_form(form)
    
    @staticmethod
    async def update_form():
        pass
    
    @staticmethod
    async def patch_form():
        pass
    
    @staticmethod
    async def delete_form():
        pass