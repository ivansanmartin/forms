from app.db.mongodb_manager import MongoDBManager
from app.models.form_model import Form
from app.models.field_model import Field
import bson

class FormCrud():
    
    @staticmethod
    async def get_form(form_id):
        collection = MongoDBManager.get_collection("forms")
        result = await collection.find_one({ "form_id": form_id}, {"_id": 0 })
        
        return result
    
    @staticmethod
    async def create_form(form: Form):
        collection = MongoDBManager.get_collection("forms")
        await collection.insert_one(form.model_dump())
        






