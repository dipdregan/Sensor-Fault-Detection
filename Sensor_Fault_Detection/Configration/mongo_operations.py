import pandas as pd
from Sensor_Fault_Detection.Configration.mongodb_connection import MongoDBClient
from Sensor_Fault_Detection.constants.database import DATABASE_NAME, COLLECTION_NAME, CSV_DATA_PATH
from Sensor_Fault_Detection.logger import logging
from Sensor_Fault_Detection.exception import SensorException
import os, sys


class MongoOperations:

    """
    A class for performing MongoDB operations, including creating databases, collections,
    uploading data from CSV files, listing databases and collections, and deleting databases and collections.

    Attributes:
        None

    Methods:
        - __init__(): Initializes the MongoDB client connection.
        - create_database(database_name=DATABASE_NAME): Creates a MongoDB database if it doesn't exist.
        - create_collection(database_name=DATABASE_NAME, collection_name=COLLECTION_NAME): Creates a MongoDB collection
          within a database if it doesn't exist.
        - upload_csv_to_collection(database_name=DATABASE_NAME, collection_name=COLLECTION_NAME, csv_file_path=CSV_DATA_PATH):
          Uploads data from a CSV file to a specified collection within a database.

    Usage:
        # Example usage of the class:
        db_client = MongoOperations()
        db_client.create_database(database_name)
        db_client.create_collection(database_name, collection_name)
        db_client.upload_csv_to_collection(database_name, collection_name, csv_file_path)
    """


    def __init__(self):
        logging.info(f"Making a connection...>>>> Dipendra G wait ,.....")
        self.mongo_client = MongoDBClient()
        logging.info(f"Connection Established ......>>>>>")


    def create_database(self, database_name=DATABASE_NAME):
        try:

            if database_name not in self.mongo_client.client.list_database_names():
                logging.info("creating a data base.....>>>>>>>")
                self.mongo_client.client[database_name]
                logging.info(f"Database created successfully :'{database_name}'........>>>>>>>>>  sir")
            else:
                logging.info(f"Database '{database_name}' already exists....>>>>>>> sir")
        except Exception as e:
            raise SensorException(e, sys)

    def create_collection(self, database_name=DATABASE_NAME, collection_name=COLLECTION_NAME):
        try:
            db = self.mongo_client.client[database_name]
            if collection_name not in db.list_collection_names():
                logging.info(f"Creating the collection....>>>>>")
                db.create_collection(collection_name)
                logging.info(f"Created collection '{collection_name}' in database '{database_name}'.")
            else:
                logging.info(f"Collection '{collection_name}' already exists in database '{database_name}'.")
        except Exception as e:
            raise SensorException(e, sys)

    def upload_csv_to_collection(self, database_name=DATABASE_NAME, collection_name=COLLECTION_NAME, csv_file_path=CSV_DATA_PATH):
        try:
            logging.info(f"Uploading the CSV dataset in mongoDB .......>>>>>>>>")
            db = self.mongo_client.client[database_name]
            collection = db[collection_name]
            df = pd.read_csv(csv_file_path)
            data = df.to_dict(orient='records')
            result = collection.insert_many(data)
            logging.info(f"Inserted {len(result.inserted_ids)} documents into the collection '{collection_name}' in database '{database_name}'.")
        except Exception as e:
            raise e

# if __name__ == "__main__":
#     db_client = MongoOperations()
#     database_name = "sensor"
#     collection_name = "sensor_data"  
#     csv_file_path = r"sensor_csv_file.csv"

#     db_client.create_database(database_name)
#     db_client.create_collection(database_name, collection_name)
#     db_client.upload_csv_to_collection(database_name, collection_name, csv_file_path)
