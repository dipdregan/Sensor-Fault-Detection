from Sensor_Fault_Detection.constants.Training_pipeline import SCHEMA_FILE_PATH
from Sensor_Fault_Detection.entity.aritfacft_entity import DataIngestionArtifact, DataValidationArtifact
from Sensor_Fault_Detection.entity.config_entity import DataValidationConfig

from Sensor_Fault_Detection.exception import SensorException
from Sensor_Fault_Detection.logger import logging

import os,sys
import pandas as pd

from scipy.stats import ks_2samp
import numpy as np

from Sensor_Fault_Detection.utils.util import read_yaml_file,write_yaml_file

class DataValidation:
    
    def __init__(self, data_ingestion_artifact:DataIngestionArtifact,
                 data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)

        except Exception as e:
            raise SensorException(e, sys)

    def validate_number_of_columns(self, dataframe:pd.DataFrame)->bool:
        try:
            number_of_columns = len(self._schema_config['columns'])
            logging.info(f"Required number of columns :{number_of_columns}")
            logging.info(f"Data frame has a columns: {len(dataframe.columns)}")

            if len(dataframe.columns)== number_of_columns:
                return True
            return False
        
        except Exception as e:
            raise SensorException(e, sys)
        
    def drop_zero_std_columns(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        try:
            # Filter only numeric columns
            numeric_df = dataframe.select_dtypes(include=[np.number])

            std_dev = numeric_df.std()
            non_zero_std_cols = std_dev[std_dev != 0].index.tolist()

            return dataframe[non_zero_std_cols]
        except Exception as e:
            raise SensorException(e, sys)

    def is_numerical_column_exist(self, dataframe:pd.DataFrame)-> bool:
        try:
            numerical_columns = self._schema_config['numerical_columns']
            dataframe_columns = dataframe.columns

            numerical_columns_status = True
            missing_numerical_columns = []
            for num_col in numerical_columns:
                if num_col not in dataframe_columns:
                    numerical_columns_status = False
                    missing_numerical_columns.append(num_col)
            
            logging.info(f"Missing numerical columns : \n\n[{missing_numerical_columns}]")
            return numerical_columns_status
        
        except Exception as e:
            raise SensorException(e, sys)

    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise SensorException(e,sys)


    def detect_dataset_drift(self,base_df, current_df, threshold=0.05) ->bool:
        try:
            status = True
            drift_report={}
            for column in base_df.columns:
                d1 = base_df[column]
                d2 = current_df[column]
                is_same_dist = ks_2samp(d1,d2)
                if threshold<=float(is_same_dist.pvalue):
                    is_found=False

                else:
                    is_found = True
                    status = False
                drift_report.update({column:{
                    "p_value":float(is_same_dist.pvalue),
                    "drift_status":is_found
                    }})
            drift_report_file_path = self.data_validation_config.drift_report_file_path
            #creating dir
            dir_path = os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path, exist_ok= True)
            write_yaml_file(file_path=drift_report_file_path, content=drift_report)
                
            return status
        
        except Exception as e:
            raise SensorException(e, sys)


    def initiate_data_validation(self)-> DataValidationArtifact:
        try:
            error_message = ""
            ## from data ingestion artifact we are taking a path for train and test csv file
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            ## reading data from train and test file
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)

            # validate number of columns
            status = self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message = f"{error_message} Train data frame dose not contain all columns.\n"
            
            status = self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                error_message = f"{error_message} Test data frame dose not contain all columns.\n"

            ## Validate numerical columns
            status = self.is_numerical_column_exist(dataframe=train_dataframe)
            if not status:
                error_message = f"{error_message} Train data frame dose not contain all numerical columns"

            status = self.is_numerical_column_exist(dataframe=test_dataframe)
            if not status:
                error_message = f"{error_message} Test data frame dose not contain all numerical columns"

            if len(error_message)>0:
                raise Exception(error_message)
            
            ## drop_ zero std columns
            train_dataframe = self.drop_zero_std_columns(train_dataframe)
            test_dataframe = self.drop_zero_std_columns(test_dataframe)

            ## Let's Check the data drift
            data_drift_status = self.detect_dataset_drift(base_df=train_dataframe,current_df=test_dataframe)

            data_validation_artifact = DataValidationArtifact(
                validation_status = data_drift_status,

                valid_train_file_path = self.data_validation_config.valid_train_file_path,
                valid_test_file_path  = self.data_validation_config.valid_test_file_path,

                invalid_train_file_path = self.data_validation_config.invalid_train_file_path,
                invalid_test_file_path  = self.data_validation_config.invalid_test_file_path,

                data_drift_report_file_path = self.data_validation_config.drift_report_file_path
            )

            logging.info(f"Data Validation Artifact : {data_validation_artifact}")

        except Exception as e:
            raise SensorException(e,sys)