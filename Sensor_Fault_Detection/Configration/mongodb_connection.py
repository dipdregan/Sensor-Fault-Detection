import pymongo
from Sensor_Fault_Detection.constants.database import DATABASE_NAME,USER_NAME,PASSWORD
from Sensor_Fault_Detection.constants.env_variable import MONGODB_URL_KEY
from Sensor_Fault_Detection.exception import SensorException
from dotenv import load_dotenv

import certifi
import os,sys

load_dotenv()
ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:

            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                # mongo_db_url = F"mongodb+srv://{USER_NAME}:{PASSWORD}@cluster0.eaymsvp.mongodb.net/?retryWrites=true&w=majority"
                print(mongo_db_url)
                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url) 
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            print("Connection Stablished")
        except Exception as e:
            raise SensorException(e,sys)