from app.db.mongodb_manager import MongoDBManager
from app.models.field_model import Fields
from app.schemas.field_update import FieldsUpdate
from pymongo.results import UpdateResult

class FieldCrud:
    """
    CRUD operations for managing form fields in the MongoDB database.

    This class provides methods to interact with the "forms" collection,
    specifically for managing fields within a form document.

    Methods:
        get_fields(form_id: str) -> dict | None:
            Retrieves the fields of a form by its ID.

        create_form_fields(form_id: str, field: Fields) -> UpdateResult:
            Adds a new field to an existing form.

        patch_form_field(form_id: str, field_id: str, fields: FieldsUpdate) -> dict | None:
            Updates a specific field within a form.

        delete_form_field(form_id: str, field_id: str) -> UpdateResult:
            Removes a specific field from a form.
    """

    @staticmethod
    async def get_fields(form_id: str) -> dict | None:
        """
        Retrieve all fields of a form by its ID.

        Args:
            form_id (str): The unique identifier of the form.

        Returns:
            dict | None: A dictionary containing the "fields" array if found, otherwise None.
        """
        collection = MongoDBManager.get_collection("forms")
        fields = await collection.find_one({"form_id": form_id}, projection={"fields": 1, "_id": 0})
        return fields

    @staticmethod
    async def create_form_fields(form_id: str, field: Fields) -> UpdateResult:
        """
        Add a new field to an existing form.

        Args:
            form_id (str): The unique identifier of the form.
            field (Fields): The field object to be added.

        Returns:
            UpdateResult: The result of the update operation.
        """
        collection = MongoDBManager.get_collection("forms")
        result = await collection.update_one({"form_id": form_id}, {"$push": {"fields": field.model_dump()}})
        return result

    @staticmethod
    async def patch_form_field(form_id: str, field_id: str, fields: dict) -> dict | None:
        """
        Update a specific field within a form.

        Args:
            form_id (str): The unique identifier of the form.
            field_id (str): The unique identifier of the field to update.
            fields (FieldsUpdate): The updated field data.

        Returns:
            dict | None: The updated form document if successful, otherwise None.
        """
        collection = MongoDBManager.get_collection("forms")
        result = await collection.find_one_and_update({"form_id": form_id, "fields.field_id": field_id}, {"$set": {f"fields.$.{key}": value for key, value in fields.items()}}, {"_id": 0})
        
        return result
    
    @staticmethod
    async def delete_form_field(form_id: str, field_id: str) -> UpdateResult:
        """
        Remove a specific field from a form.

        Args:
            form_id (str): The unique identifier of the form.
            field_id (str): The unique identifier of the field to remove.

        Returns:
            UpdateResult: The result of the update operation.
        """
        pass
