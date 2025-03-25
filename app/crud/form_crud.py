from app.db.mongodb_manager import MongoDBManager


class FormCrud():
    
    @classmethod
    async def get_form(cls):
        collection = MongoDBManager.get_collection("forms")
        
        result = collection.find_one()
        return result




