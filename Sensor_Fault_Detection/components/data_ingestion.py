from Sensor_Fault_Detection.exception import SensorException
from Sensor_Fault_Detection.logger import logging

from Sensor_Fault_Detection.entity.config_entity import DataIngetionConfig
from Sensor_Fault_Detection.entity.aritfacft_entity import DataIngestionArtifact

from sklearn.model_selection import train_test_split
from Sensor_Fault_Detection.data_access.Export_DB_data import ExportData
from Sensor_Fault_Detection.utils.util import read_yaml_file
from Sensor_Fault_Detection.constants.Training_pipeline import SCHEMA_FILE_PATH

from pandas import DataFrame
import pandas as pd
import os, sys

class DataIngestion:

    def __init__(self, data_ingestion_config:DataIngetionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise SensorException(e,sys)

    def export_data_into_feature_store(self) -> DataFrame:
        """
        Bring the data from Mongo DB record as data frame into feature store
        """

        try:
            logging.info(f"Grabbing data from mongo db to feature store......>>>>>>>>>>")
            sensor_data = ExportData()
            datafame = sensor_data.export_collection_as_dataframe()
 
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            ## Creating a folder
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok= True)

            ## saving  the data
            datafame.to_csv(feature_store_file_path, index=False, header= None)

            logging.info(f"Data store in this folder :{feature_store_file_path}")

            return datafame

        except Exception as e:
            raise SensorException(e, sys)
    
    def split_data_as_train_test(self, dataframe:DataFrame) ->None:
        
        """
        Feature store data set will be split in trian and test file
        """
        
        try:
            logging.info(f"Performing train test and split on the raw dataset..........>>>>>")

            train_set, test_set =train_test_split(dataframe,
                                                  test_size=self.data_ingestion_config.train_test_split_ratio)
            
            dir_path = os.path.join(self.data_ingestion_config.train_test_ingested_folder)
            os.makedirs(dir_path, exist_ok= True)

            train_set.to_csv(self.data_ingestion_config.training_file_path, index = False, header = True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False,header = True)

            logging.info(f"train and test file splited and saved on this location :{dir_path} ")
        except Exception as e:
            raise SensorException(e, sys)
    
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_data_into_feature_store()
            drop_columns = self._schema_config["drop_columns"]
            dataframe = dataframe.drop(drop_columns,axis=1)
            logging.info(f"Drop columns: {drop_columns}")

            self.split_data_as_train_test(dataframe = dataframe)
            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                  test_file_path= self.data_ingestion_config.testing_file_path)
            
            logging.info(f"{30*'===='}")
            logging.info(f"{10*'=='}Data Ingestion Completed...{10*'=='}")
            logging.info(f"{30*'===='}")
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e,sys)
        
    