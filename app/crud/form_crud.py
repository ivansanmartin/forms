from app.db.mongodb_manager import MongoDBManager
from app.models.form_model import Form
from app.schemas.form_update import FormUpdate

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
    
    @staticmethod
    async def patch_form(form_id, form_update):
        collection = MongoDBManager.get_collection("forms")
        await collection.update_one({ "$and": [{"form_id": form_id}, {"title": form_update["title"]}] }, { "$set": form_update })
        
        new_form = await collection.find_one({ "form_id": form_id}, {"_id": 0 })
        
        return new_form
    
    @staticmethod
    async def delete_form(form_id):
        collection = MongoDBManager.get_collection("forms")
        result = await collection.delete_one({ "form_id": form_id })
        return result