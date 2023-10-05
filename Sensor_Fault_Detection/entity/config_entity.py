from datetime import datetime
from Sensor_Fault_Detection.constants import Training_pipeline
import os


class TrainingPipelineConfig:

    def __init__(self, timestamp = datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")

        self.pipeline_name: str = Training_pipeline.PIPELINE_NAME
        self.artifact_dir: str = os.path.join(Training_pipeline.ARTIFACT_DIR,timestamp)
        self.timestamp: str = timestamp

class DataIngetionConfig:
    """
    Configuration class for data ingestion in the training pipeline.

    Args:
        training_pipeline_config (TrainingPipelineConfig): Configuration object for the training pipeline.

    Attributes:
        data_ingestion_dir (str): Directory path for data ingestion artifacts.
        feature_store_file_path (str): File path for the feature store data.
        train_test_ingested_folder (str): Folder path for ingested training and testing data.
        training_file_path (str): File path for the ingested training data.
        testing_file_path (str): File path for the ingested testing data.
        train_test_split_ratio (float): Ratio for splitting data into training and testing sets.
        collection_name (str): Name of the collection for data ingestion.

    """

    def __init__(self, training_pipeline_config:TrainingPipelineConfig):

        self.data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir,
                                                    Training_pipeline.DATA_INGETION_DIR_NAME,
                                                    )
        
        self.feature_store_file_path: str = os.path.join(self.data_ingestion_dir,
                                                         Training_pipeline.DATA_INGETION_FEATURE_STORE_DIR,
                                                         Training_pipeline.FILE_NAME
                                                         )
        
        self.train_test_ingested_folder: str = os.path.join(self.data_ingestion_dir,
                                                    Training_pipeline.DATA_INGETION_INGESTED_DIR,
                                                    )
        
        self.training_file_path: str = os.path.join(self.data_ingestion_dir,
                                                    Training_pipeline.DATA_INGETION_INGESTED_DIR,
                                                    Training_pipeline.TRAINING_FILE_NAME
                                                    )
        
        self.testing_file_path: str = os.path.join(self.data_ingestion_dir,
                                                   Training_pipeline.DATA_INGETION_INGESTED_DIR,
                                                   Training_pipeline.TESTING_FILE_NAME
                                                   )
        
        self.train_test_split_ratio:float = Training_pipeline.DATA_INGETION_TRAIN_TEST_SPLIT_RATION 

        self.collection_name:str = Training_pipeline.DATA_INGESTION_COLLECTION_NAME



class DataValidationConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir,
                                                Training_pipeline.DATA_VALIDATION_DIR_NAME)
        
        self.valid_data_dir:str = os.path.join(self.data_validation_dir,
                                               Training_pipeline.DATA_VALIDATION_VALID_DIR)
        
        self.invalid_data_dir: str = os.path.join(self.data_validation_dir,
                                                  Training_pipeline.DATA_VALIDATION_INVALID_DIR)
        
        self.valid_train_file_path: str = os.path.join(self.valid_data_dir,
                                                       Training_pipeline.TRAINING_FILE_NAME)
        
        self.valid_test_file_path: str = os.path.join(self.valid_data_dir,
                                                       Training_pipeline.TESTING_FILE_NAME)
        
        self.invalid_train_file_path: str = os.path.join(self.invalid_data_dir,
                                                         Training_pipeline.TRAINING_FILE_NAME)
        
        self.invalid_test_file_path: str = os.path.join(self.invalid_data_dir,
                                                         Training_pipeline.TESTING_FILE_NAME)
        
        self.drift_report_file_path: str = os.path.join(self.data_validation_dir,
                                                        Training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
                                                        Training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)
        

        
        