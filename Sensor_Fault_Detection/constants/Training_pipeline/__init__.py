import os
from Sensor_Fault_Detection.constants.s3_bucket import TRAINING_BUCKET_NAME

"""
Defining common constnat for training pipeline
"""
TARGET_COLUMN = 'class'
PIPELINE_NAME: str = "Sensor-Fault-Detection"
ARTIFACT_DIR: str = "artifact"
FILE_NAME: str = "sensor.csv"

TRAINING_FILE_NAME = "train.csv"
TESTING_FILE_NAME = "test.csv"

PREPROCESS_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = 'model.pkl'

SCHEMA_FILE_PATH = os.path.join("configs",'schema.yaml')
SCHEMA_DROP_COLS = 'drop_columns'

"""
Defining Data Ingetion related constant 
"""
DATA_INGESTION_COLLECTION_NAME: str = "sensor"
DATA_INGETION_DIR_NAME: str = "data_ingetion"
DATA_INGETION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGETION_INGESTED_DIR: str = "ingested"
DATA_INGETION_TRAIN_TEST_SPLIT_RATION: float = 0.20

"""
Data validation realted constant
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"


"""
Data Transformation ralated constant
"""

DATA_TRANSFORMATION_DIR_NAME = 'data_transformation'
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR = "transformed_object"

"""
Model Tranier related Constant
"""
MODEL_TRAINER_DIR_NAME:str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR:str = "traned_model"
MODEL_FILE_NAME:str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float =0.71
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING: float =0.5