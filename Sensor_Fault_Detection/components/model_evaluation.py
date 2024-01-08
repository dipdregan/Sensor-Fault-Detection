from Sensor_Fault_Detection.entity.aritfacft_entity import DataValidationArtifact, ModelEvaluationArtifact,ModelTrainerArtifact
from Sensor_Fault_Detection.entity.config_entity import ModelEvaluationConfig

import os, sys

from Sensor_Fault_Detection.ml.metric.classification_matrics import get_classification_score
from Sensor_Fault_Detection.ml.model.estimator import SensorModel, ModelResolver

from Sensor_Fault_Detection.exception import SensorException
from Sensor_Fault_Detection.logger import logging
from Sensor_Fault_Detection.utils.util import save_object, load_object
import pandas as pd

class ModelEvaluation:

    def __init__(self, model_eval_config:ModelEvaluationConfig,
                 data_validation_artifact:DataValidationArtifact,
                 model_trainer_artifact:ModelTrainerArtifact):
        
        try:
            self.model_eval_config = model_eval_config
            self.data_validation_artifact = data_validation_artifact
            self.model_trainer_artifact = model_trainer_artifact
        except Exception as e:
            raise SensorException(e,sys)
        

    def initiate_model_evaluation(self)-> ModelEvaluationArtifact:
        try:
            valid_train_file_path = self.data_validation_artifact.valid_train_file_path
            valid_test_file_path = self.data_validation_artifact.valid_test_file_path

            #valid train and test file
            train_df = pd.read_csv(valid_train_file_path)
            test_df = pd.read_csv(valid_test_file_path)

            train_model_file_path = self.model_trainer_artifact.trained_model_file_path
            model_resolver = ModelResolver()

            is_model_accepted = True
            if not model_resolver.is_model_exists():
                model_evaluation_artifact = ModelEvaluationArtifact(is_model_accepted=is_model_accepted,
                                        improved_accuarcy=None,
                                        best_model_path=None,
                                        trained_model_path = train_model_file_path,
                                        train_model_metric_artifact = self.model_trainer_artifact.test_metric_artifact,
                                        best_model_metric_artifact=None)
                
                logging.info(f"Model Evaluation Artifact: {model_evaluation_artifact}")
                return model_evaluation_artifact
            
            

        except Exception as e:
            raise SensorException(e, sys)

        

        