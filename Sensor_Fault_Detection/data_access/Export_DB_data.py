from Sensor_Fault_Detection.Configration.mongodb_connection import MongoDBClient
from Sensor_Fault_Detection.constants.database import DATABASE_NAME, COLLECTION_NAME
from Sensor_Fault_Detection.exception import SensorException
from Sensor_Fault_Detection.logger import logging


import sys
import pandas as pd
import numpy as np

class ExportData:
    """
    This class helps to export entire MongoDB collection as a Pandas DataFrame.
    """

    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise SensorException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str = COLLECTION_NAME,
                                       database_name: str = DATABASE_NAME) -> pd.DataFrame:
        """
        Export the specified collection as a Pandas DataFrame.

        Args:
            collection_name (str): The name of the collection to export.
            database_name (str): The name of the database containing the collection.

        Returns:
            pd.DataFrame: A Pandas DataFrame containing the collection data.
        """
        try:
            # if database_name is None:
            #     collection = self.mongo_client.database[collection_name]
            # else:
            #     collection = self.mongo_client.client[database_name][collection_name]


            if database_name is None:
                collection = self.mongo_client.client[collection_name]
            else:
                collection = self.mongo_client.client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            logging.info(f"{df}")

            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            df.replace({"na": np.nan}, inplace=True)

            return df

        except Exception as e:
            raise SensorException(e, sys)

