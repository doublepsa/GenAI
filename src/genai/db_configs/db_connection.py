from mongoengine import connect
from dotenv import load_dotenv
import os
# Load the config file
load_dotenv()

class MongoDBConnection:
    @classmethod
    def setup(cls):
        """ Sets up the MongoDB connection using environment variables.
            Returns True if connection is successful, False otherwise.
        """
        # Read DB config from environment variables
        db_name = os.getenv("MONGO_DB_NAME", "GenAi_WS25")
        host = os.getenv("MONGO_HOST", "localhost")
        port = int(os.getenv("MONGO_PORT", 27017))

        # Attempt to connect to MongoDB
        try:
            connect(db=db_name, host=host, port=port)
            print(f"Connected to local DB: {db_name}")
            return True
        except Exception as e:
            print(f"Connection Failed: {e}")
            return False