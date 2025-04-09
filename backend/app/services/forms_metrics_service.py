from app.schemas.forms_metrics import FormMetrics
from app.db.mongodb_manager import MongoDBManager
from pymongoexplain import ExplainableCollection

class FormMetricService:
    
    @staticmethod
    async def get_form_metrics(public_code: str) -> FormMetrics:
        collection = MongoDBManager.get_collection("metrics")
        result = await collection.find_one({ "public_code": public_code })
        return result