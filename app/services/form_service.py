from app.crud.form_crud import FormCrud

class FormService():
    @staticmethod
    async def get_form():
        form = await FormCrud.get_form()
        return form