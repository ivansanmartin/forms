from app.crud.fields_crud import FieldCrud
from app.models.field_model import Fields
from app.schemas.field_update import FieldsUpdate
from pymongo.results import UpdateResult, DeleteResult


class FieldService:
    """
    Service class for managing fields of forms.

    This class provides business logic for handling form fields, acting as an 
    intermediary between the data access layer (CRUD operations) and the application logic.

    Methods:
        get_fields(form_id: str) -> list[dict] | None:
            Retrieves all fields of a form by its ID.
        
        create_form_fields(form_id: str, fields: Fields) -> UpdateResult:
            Creates a new field within a form.
        
        patch_form_field(form_id: str, field_id: str, fields_update: FieldsUpdate) -> dict | None:
            Updates a specific field in a form.
        
        delete_form_field(form_id: str, field_id: str) -> DeleteResult:
            Deletes a specific field from a form.
    """

    @staticmethod
    async def get_fields(form_id: str) -> list[dict] | None:
        """
        Retrieve all fields of a form by its ID.

        Args:
            form_id (str): The ID of the form.

        Returns:
            list[dict] | None: A list of fields if found, otherwise None.
        """
        fields = await FieldCrud.get_fields(form_id)
        return fields if fields else None

    @staticmethod
    async def create_form_fields(form_id: str, fields: Fields) -> UpdateResult:
        """
        Create a new field within a form.

        Args:
            form_id (str): The ID of the form where the field will be added.
            fields (Fields): The field data to be created.

        Returns:
            UpdateResult: The result of the update operation.
        """
        result = await FieldCrud.create_form_fields(form_id, fields)
        return result

    @staticmethod
    async def patch_form_field(form_id: str, field_id: str, fields_update: FieldsUpdate) -> dict | None:
        """
        Update a specific field in a form.

        Args:
            form_id (str): The ID of the form containing the field.
            field_id (str): The ID of the field to update.
            fields_update (FieldsUpdate): The updated field data.

        Returns:
            dict | None: The updated field data if successful, otherwise None.
        """
        new_field = await FieldCrud.patch_form_field(form_id, field_id, fields_update.model_dump(exclude_unset=True))
        return new_field

    @staticmethod
    async def delete_form_field(form_id: str, field_id: str) -> DeleteResult:
        """
        Delete a specific field from a form.

        Args:
            form_id (str): The ID of the form.
            field_id (str): The ID of the field to delete.

        Returns:
            DeleteResult: The result of the delete operation.
        """
        result = await FieldCrud.delete_form_field(form_id, field_id)
        return result
