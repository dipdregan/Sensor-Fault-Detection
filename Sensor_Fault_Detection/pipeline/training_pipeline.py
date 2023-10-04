from Sensor_Fault_Detection.entity.config_entity import DataIngetionConfig, TrainingPipelineConfig
from Sensor_Fault_Detection.entity.aritfacft_entity import DataIngestionArtifact
from Sensor_Fault_Detection.exception import SensorException

import sys, os
from Sensor_Fault_Detection.logger import logging
from Sensor_Fault_Detection.components.data_ingestion import DataIngestion

class TrainingPipeline:

    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
        

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            self.data_ingestion_config = DataIngetionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting Data Ingestion---------->>>>>>>>>>>>")
            data_ingetion = DataIngestion(data_ingestion_config=self.data_ingestion_config)

            data_ingetion_artifact = data_ingetion.initiate_data_ingestion()
            logging.info(f"<<<<<<<<<<<<<<<<---------Data Ingestion Completed  and artifact : {data_ingetion_artifact}---------->>>>>>>>>>>>")
            return data_ingetion_artifact
        except Exception as e:
            raise SensorException(e, sys)
        
    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)
        
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)
        
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)
        
    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)
        
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)
        
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
        except Exception as e:
            raise SensorException(e, sys)
        

