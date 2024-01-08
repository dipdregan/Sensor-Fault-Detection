from Sensor_Fault_Detection.entity.aritfacft_entity import DataValidationArtifact,\
     ModelEvaluationArtifact,ModelTrainerArtifact
from Sensor_Fault_Detection.entity.config_entity import ModelEvaluationConfig

import os, sys

from Sensor_Fault_Detection.ml.metric.classification_matrics import get_classification_score
from Sensor_Fault_Detection.ml.model.estimator import SensorModel, ModelResolver

from Sensor_Fault_Detection.exception import SensorException
from Sensor_Fault_Detection.logger import logging
from Sensor_Fault_Detection.utils.util import save_object, load_object, write_yaml_file
import pandas as pd
from Sensor_Fault_Detection.constants.Training_pipeline import TARGET_COLUMN

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

            df = pd.concat([train_df,test_df])

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
            
            latest_model_path = ModelResolver.get_best_model_path()
            latest_model = load_object(file_path=latest_model_path)
            train_model = load_object(file_path=train_model_file_path)

            y_true = df[TARGET_COLUMN]
            y_train_pred = train_model.predict(df)
            y_latest_pred = latest_model.predict(df)

            train_metrix = get_classification_score(y_true, y_train_pred)
            latest_metrix = get_classification_score(y_true, y_latest_pred)

            improved_accuarcy = train_metrix-latest_metrix 
            if  self.model_eval_config.change_thresold < improved_accuarcy:
                ## 0.02<0.03
                is_model_accepted = True
            else:
                is_model_accepted =False

            model_evaluation_artifact = ModelEvaluationArtifact(
                        is_model_accepted=is_model_accepted,
                        improved_accuarcy=improved_accuarcy,
                        best_model_path=latest_model_path,
                        trained_model_path = train_model_file_path,
                        train_model_metric_artifact = train_metrix,
                        best_model_metric_artifact=latest_metrix)
            model_evaluation_report = model_evaluation_artifact.__dict__()
            write_yaml_file(self.model_eval_config.report_file_path,
                            model_evaluation_report)
            logging.info(f"Model evaluation artifact:{model_evaluation_artifact}")
            return model_evaluation_artifact

        except Exception as e:
            raise SensorException(e, sys)

        

        