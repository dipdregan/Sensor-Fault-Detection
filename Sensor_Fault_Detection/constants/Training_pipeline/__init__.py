import os
from Sensor_Fault_Detection.constants.s3_bucket import TRAINING_BUCKET_NAME

"""
Defining common constnat for training pipeline
"""
TARGET_COLUMN = 'class'
PIPELINE_NAME: str = "sensor"
ARTIFACT_DIR: str = "artifact"
FILE_NAME: str = "sensor.csv"

TRAINING_FILE_NAME = "train.csv"
TESTING_FILE_NAME = "test.csv"

PREPROCESS_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = 'model.pkl'

SCHEMA_FILE_PATH = os.path.join("config",'schema.yaml')
SCHEMA_DROP_COLS = 'drop_columns'

"""
Defining Data Ingetion related constant 
"""
DATA_INGESTION_COLLECTION_NAME: str = "sensor"
DATA_INGETION_DIR_NAME: str = "data_ingetion"
DATA_INGETION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGETION_INGESTED_DIR: str = "ingested"
DATA_INGETION_TRAIN_TEST_SPLIT_RATION: float = 0.25