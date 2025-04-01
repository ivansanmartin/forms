from app.db.mongodb_manager import MongoDBManager
from app.models.form_model import Form
from app.schemas.form_update import FormUpdate
from pymongo.results import DeleteResult
from pymongo import ReturnDocument

class FormCrud:
    """
    CRUD operations for managing forms in the MongoDB database.

    This class provides methods to interact with the "forms" collection,
    including retrieving, creating, updating, and deleting form documents.

    Methods:
        get_form(form_id: str) -> dict | None:
            Retrieves a form document by its ID.

        create_form(form: Form) -> None:
            Inserts a new form document into the database.

        patch_form(form_id: str, form_update: dict) -> dict | None:
            Updates an existing form document based on the provided fields.

        delete_form(form_id: str) -> DeleteResult:
            Deletes a form document by its ID.
    """

    @staticmethod
    async def get_form(form_id: str) -> dict | None:
        """
        Retrieve a form document by its ID.

        Args:
            form_id (str): The unique identifier of the form.

        Returns:
            dict | None: The form document if found, otherwise None.
        """
        collection = MongoDBManager.get_collection("forms")
        result = await collection.find_one({"form_id": form_id}, {"_id": 0})
        return result

    @staticmethod
    async def create_form(form: Form) -> None:
        """
        Insert a new form document into the database.

        Args:
            form (Form): The form object containing the data to be stored.

        Returns:
            None
        """
        collection = MongoDBManager.get_collection("forms")
        await collection.insert_one(form.model_dump(exclude_none=True))

    @staticmethod
    async def patch_form(form_id: str, form_update: dict) -> dict | None:
        """
        Update an existing form document.

        Args:
            form_id (str): The unique identifier of the form.
            form_update (dict): A dictionary containing the fields to update.

        Returns:
            dict | None: The updated form document if successful, otherwise None.
        """
        collection = MongoDBManager.get_collection("forms")
        
        new_form = await collection.find_one_and_update(
            {"$and": [{"form_id": form_id}, {"title": form_update["title"]}]},
            {"$set": form_update}, 
            {"_id": 0},
            return_document=ReturnDocument.AFTER
        )

        return new_form

    @staticmethod
    async def delete_form(form_id: str) -> DeleteResult:
        """
        Delete a form document by its ID.

        Args:
            form_id (str): The unique identifier of the form.

        Returns:
            DeleteResult: The result of the deletion operation.
        """
        collection = MongoDBManager.get_collection("forms")
        result = await collection.delete_one({"form_id": form_id})
        return result
