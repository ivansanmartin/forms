from app.crud.forms_crud import FormCrud
from app.models.form_model import Form
from app.schemas.form_update import FormUpdate


class FormService:
    """
    Service class for managing forms.

    Methods:
        get_form(form_id: str) -> dict | None:
            Retrieves a form by its ID.
        
        create_form(form: Form) -> Form:
            Creates a new form and validates its structure.
        
        patch_form(form_id: str, form_update: FormUpdate) -> dict:
            Partially updates an existing form.
        
        delete_form(form_id: str) -> DeleteResult:
            Deletes a form by its ID.
    """

    @staticmethod
    async def get_form(form_id: str) -> dict | None:
        """
        Retrieve a form by its ID.

        Args:
            form_id (str): The ID of the form to retrieve.

        Returns:
            dict | None: The form data if found, otherwise None.
        """
        form = await FormCrud.get_form(form_id)
        if not form:
            return None
        return Form.model_validate(form).model_dump()

    @staticmethod
    async def create_form(form: Form) -> Form:
        """
        Create a new form.

        Args:
            form (Form): The form object to be created.

        Returns:
            Form: The validated form object.
        """
        await FormCrud.create_form(form)
        return Form.model_validate(form)

    @staticmethod
    async def patch_form(form_id: str, form_update: FormUpdate) -> dict:
        """
        Partially update a form.

        Args:
            form_id (str): The ID of the form to update.
            form_update (FormUpdate): The data to update.

        Returns:
            dict: The updated form data.
        """
        new_form = await FormCrud.patch_form(form_id, form_update.model_dump(exclude_unset=True))
        return new_form

    @staticmethod
    async def delete_form(form_id: str):
        """
        Delete a form by its ID.

        Args:
            form_id (str): The ID of the form to delete.

        Returns:
            DeleteResult: return a DeleteResult class of MotorCollection
        """
        result = await FormCrud.delete_form(form_id)
        return result
