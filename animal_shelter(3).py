

from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, _password, _username = 'aacUser'):
        # Connection variables
        USER = "aacuser"
        PASS = "your_secure_password"
        HOST = "nv-desktop-services.apporto.com"
        PORT = 32967
        DB = "AAC"
        COL = "animals"

        # Initialize connection to MongoDB
        self.client = MongoClient(f"mongodb://{USER}:{PASS}@{HOST}:{PORT}")
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """
        Insert a new document into the collection.
        Args:
            data (dict): The data to be inserted.
        Returns:
            bool: True if the insert was successful, False otherwise.
        """
        try:
            if data and isinstance(data, dict):
                self.collection.insert_one(data)
                return True
            else:
                raise ValueError("Provided data must be a non-empty dictionary.")
        except PyMongoError as e:
            print(f"Error inserting document: {e}")
            return False

    def read(self, query):
        """
        Query the collection for documents.
        Args:
            query (dict): The query to execute.
        Returns:
            list: A list of documents matching the query, or an empty list.
        """
        try:
            if isinstance(query, dict):
                cursor = self.collection.find(query)
                return list(cursor)
            else:
                raise ValueError("Query must be a valid dictionary.")
        except PyMongoError as e:
            print(f"Error querying documents: {e}")
            return []

  

    def delete(self, query):
        """
        Delete documents from the collection.
        Args:
            query (dict): The query to find documents to delete.
        Returns:
            int: The number of documents deleted.
        """
        try:
            if query and isinstance(query, dict):
                result = self.collection.delete_many(query)
                return result.deleted_count
            else:
                raise ValueError("Query must be a valid dictionary.")
        except PyMongoError as e:
            print(f"Error deleting documents: {e}")
            return 0

    def update(self, query, update_data):
        """
        Update documents in the collection.
        Args:
            query (dict): The query to find documents.
            update_data (dict): The data to update in matching documents.
        Returns:
            int: The number of documents updated.
        """
        try:
            if query and isinstance(query, dict) and update_data and isinstance(update_data, dict):
                result = self.collection.update_many(query, {"$set": update_data})
                return result.modified_count
            else:
                raise ValueError("Both query and update_data must be valid dictionaries.")
        except PyMongoError as e:
            print(f"Error updating documents: {e}")
            return 0