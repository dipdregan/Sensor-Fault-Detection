from Sensor_Fault_Detection.utils.util import load_numpy_array_data, load_object,\
      save_object
from Sensor_Fault_Detection.exception import SensorException
from Sensor_Fault_Detection.logger import logging

from Sensor_Fault_Detection.entity.aritfacft_entity import DataTransformationArtifact,\
      ModelTrainerArtifact
from Sensor_Fault_Detection.entity.config_entity import ModelTranierConfig

from Sensor_Fault_Detection.ml.metric.classification_matrics import \
    get_classification_score
from Sensor_Fault_Detection.ml.model.estimator import SensorModel

from xgboost import XGBClassifier

import os, sys

class ModelTrainer:
    def __init__(self, model_trainer_config:ModelTranierConfig,
                 data_transformation_artifact:DataTransformationArtifact):
        try:
            self.data_transformation_artifact = data_transformation_artifact
            self.model_tranier_config = model_trainer_config
        except Exception as e:
            raise SensorException(e, sys)
        
    def train_model(self,x_train,y_train):
        try:
            xgb_clf = XGBClassifier()
            xgb_clf.fit(x_train,y_train)
            return xgb_clf
        except Exception as e:
            raise SensorException(e, sys)
        
    def initiate_model_trainer(self)-> ModelTrainerArtifact:
        try:
            logging.info("<<===================Model Traning Started.......=================>>")
            train_file_path = self.data_transformation_artifact.transformed_train_file_path
            test_file_path = self.data_transformation_artifact.transformed_test_file_path
            
            logging.info("loading the train and test data set..............")
            train_arr = load_numpy_array_data(train_file_path)
            test_arr = load_numpy_array_data(test_file_path)

            logging.info(f"Spliting the data into features and lables..........")
            x_train, y_train, x_test, y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:, -1]
            )

            logging.info(f"Start model training............")
            model = self.train_model(x_train=x_train,y_train=y_train)

            y_train_pred = model.predict(x_train)
            classification_train_matrics = get_classification_score(y_true=y_train,y_pred=y_train_pred)
            
            if classification_train_matrics.f1_score <= self.model_tranier_config.expected_accuarcy:
                raise Exception('Train model is not good to  expected accuracy ..!')

            y_test_pred = model.predict(x_test)
            classification_test_matrics = get_classification_score(y_true=y_test,y_pred=y_test_pred)

            logging.info("Checking the Overfittiong or Under Fitting...............")
            ## Let's Check the Overfittiong or Under Fitting
            diff = classification_train_matrics.f1_score - classification_test_matrics.f1_score

            if diff > self.model_tranier_config.overfitting_underfitting_threshold :
                raise Exception('Model is not good you have to try with more expriments..!')
            
            preprocessor = load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)
            
            model_dir_path = os.path.dirname(self.model_tranier_config.trained_model_file_path)
            os.makedirs(model_dir_path, exist_ok= True)

            sensor_model = SensorModel(preprocessor=preprocessor, model= model)
            save_object(file_path=self.model_tranier_config.trained_model_file_path, obj=sensor_model)

            # model trainer artifact

            model_trainer_artifact = ModelTrainerArtifact(trained_model_file_path=self.model_tranier_config.trained_model_file_path,
                                 train_metric_artifact=classification_train_matrics,
                                 test_metric_artifact=classification_test_matrics
                                 )
            
            logging.info(f"Model Trainer artifact : {model_trainer_artifact}")
            logging.info(f"{30*'==='}")
            logging.info(f"{10*'=='} Model Training Stage Completed {10*'=='}")
            logging.info(f"{30*'==='}")

        except Exception as e:
            raise SensorException(sys, e)