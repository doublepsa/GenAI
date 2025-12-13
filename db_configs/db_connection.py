from mongoengine import connect

class MongoDBConnection:
    @classmethod
    def setup(cls, db_name="GenAi_WS25", host="localhost", port=27017):
        try:
            connect(
                db=db_name,
                host=host, 
                port=port
            )
            print(f"Connection successful to DB: '{db_name}' at {host}:{port}")
            return True
        except Exception as e:
            print(f"Connection Failed! Error: {e}")
            return False