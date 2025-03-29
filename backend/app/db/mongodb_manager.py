from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional, Any

class MongoDBManager():
    """MongoDB manager.

    This class is used for create connections and get collections for mongodb

    """
    client: Optional[AsyncIOMotorClient] = None
    database: Optional[Any] = None 

    @classmethod
    async def create_connection(cls, url: str, database: str):
        """Create connection with MongoDB
        
        Args:
            url (str): MongoDB connection string 
            Example: (mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl)
            database (str): name of database.
        """
        cls.client = AsyncIOMotorClient(url)
        
        if cls.client:
            cls.database = cls.client[database]
            print("[MongoDB] connection init succesfully.")
        else:
            print("[MongoDB] error getting database, the connection is wrong.")
        
    @classmethod
    def get_collection(cls, collection_name: str):
        """Get a collection of database after initialize

        Args:
            collection_name (str): collection name.

        Returns:
            MotorCollection
        """
        try:
            if cls.database is None:
                raise ValueError("Database connection is not initialized. Call `create_connection` first.")
            
            return cls.database[collection_name]
        except Exception as e:
            print(e)
            
    @classmethod
    async def close_connection(cls):
        """Close connection in mongodb database
        """
        try:
            if cls.client:
                cls.client.close()
                print("[MongoDB] closed connection.")
        except Exception as e:
            print(e)
        
        