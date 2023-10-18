from Sensor_Fault_Detection.entity.config_entity import DataIngetionConfig, TrainingPipelineConfig,DataValidationConfig,DataTransformationConfig
from Sensor_Fault_Detection.entity.aritfacft_entity import DataIngestionArtifact,DataValidationArtifact,DataTransformationArtifact
from Sensor_Fault_Detection.exception import SensorException

import sys, os
from Sensor_Fault_Detection.logger import logging
from Sensor_Fault_Detection.components.data_ingestion import DataIngestion
from Sensor_Fault_Detection.components.data_validation import DataValidation
from Sensor_Fault_Detection.components.data_transformation import DataTransformation

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
        
    def start_data_validation(self, data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                             data_validation_config=data_validation_config
                                             )
            data_validation_artifact = data_validation.initiate_data_validation()

            return data_validation_artifact
        except Exception as e:
            raise SensorException(e, sys)
        
    def start_data_transformation(self,data_validation_artifact:DataValidationArtifact):
        try:
            data_transfomation_config = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact,
                               data_transformation_config=data_transfomation_config)
            data_transfomation_artifact = data_transformation.initiate_data_transformation()

            return data_transfomation_artifact
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

            data_validation_artifact:DataValidationArtifact = self.start_data_validation(
                data_ingestion_artifact=data_ingestion_artifact
                )
            data_transformation_artifact:DataTransformationArtifact = self.start_data_transformation(
                data_validation_artifact=data_validation_artifact)
            

        except Exception as e:
            raise SensorException(e, sys)
        

