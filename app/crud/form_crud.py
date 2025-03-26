from app.db.mongodb_manager import MongoDBManager
from app.models.form_model import Form
from app.models.field_model import Field
import bson

class FormCrud():
    
    @staticmethod
    async def get_form():
        collection = MongoDBManager.get_collection("forms")
        
        result = collection.find_one()
        return result
    
    @staticmethod
    async def create_form(form: Form):
        collection = MongoDBManager.get_collection("forms")
        
        print(form)
        await collection.insert_one(form.model_dump())






