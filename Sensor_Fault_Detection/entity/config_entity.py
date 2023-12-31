from datetime import datetime
from Sensor_Fault_Detection.constants.Training_pipeline import *
import os


class TrainingPipelineConfig:

    def __init__(self, timestamp = datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")

        self.pipeline_name: str = PIPELINE_NAME
        self.artifact_dir: str = os.path.join(ARTIFACT_DIR,timestamp)
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
                                                    DATA_INGETION_DIR_NAME,
                                                    )
        
        self.feature_store_file_path: str = os.path.join(self.data_ingestion_dir,
                                                         DATA_INGETION_FEATURE_STORE_DIR,
                                                         FILE_NAME
                                                         )
        
        self.train_test_ingested_folder: str = os.path.join(self.data_ingestion_dir,
                                                    DATA_INGETION_INGESTED_DIR,
                                                    )
        
        self.training_file_path: str = os.path.join(self.data_ingestion_dir,
                                                    DATA_INGETION_INGESTED_DIR,
                                                    TRAINING_FILE_NAME
                                                    )
        
        self.testing_file_path: str = os.path.join(self.data_ingestion_dir,
                                                   DATA_INGETION_INGESTED_DIR,
                                                   TESTING_FILE_NAME
                                                   )
        
        self.train_test_split_ratio:float = DATA_INGETION_TRAIN_TEST_SPLIT_RATION 

        self.collection_name:str = DATA_INGESTION_COLLECTION_NAME



class DataValidationConfig:

    """
    Configuration class for data validation in the training pipeline.

    Args:
        training_pipeline_config (TrainingPipelineConfig): Configuration object for the training pipeline.

    Attributes:
        data_validation_dir (str): Directory path for data validation artifacts.
        valid_data_dir (str): Directory path for validated data.
        invalid_data_dir (str): Directory path for invalid data.
        valid_train_file_path (str): File path for the validated training data.
        valid_test_file_path (str): File path for the validated testing data.
        invalid_train_file_path (str): File path for the invalid training data.
        invalid_test_file_path (str): File path for the invalid testing data.
        drift_report_file_path (str): File path for the data drift report.

    """
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir,
                                                DATA_VALIDATION_DIR_NAME)
        
        self.valid_data_dir:str = os.path.join(self.data_validation_dir,
                                               DATA_VALIDATION_VALID_DIR)
        
        self.invalid_data_dir: str = os.path.join(self.data_validation_dir,
                                                  DATA_VALIDATION_INVALID_DIR)
        
        self.valid_train_file_path: str = os.path.join(self.valid_data_dir,
                                                       TRAINING_FILE_NAME)
        
        self.valid_test_file_path: str = os.path.join(self.valid_data_dir,
                                                       TESTING_FILE_NAME)
        
        self.invalid_train_file_path: str = os.path.join(self.invalid_data_dir,
                                                         TRAINING_FILE_NAME)
        
        self.invalid_test_file_path: str = os.path.join(self.invalid_data_dir,
                                                         TESTING_FILE_NAME)
        
        self.drift_report_file_path: str = os.path.join(self.data_validation_dir,
                                                        DATA_VALIDATION_DRIFT_REPORT_DIR,
                                                        DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)
        

        
class DataTransformationConfig:
    """
    Configuration class for data transformation in the training pipeline.

    Args:
        training_pipeline_config (TrainingPipelineConfig): Configuration object for the training pipeline.

    Attributes:
        data_transformation_dir (str): Directory path for data transformation artifacts.
        transformed_train_file_path (str): File path for the transformed training data in NumPy format.
        transformed_test_file_path (str): File path for the transformed testing data in NumPy format.
        transformed_object_file_path (str): File path for the saved data transformation object.

    """
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir,
                                                         DATA_TRANSFORMATION_DIR_NAME
                                                         )
        self.transformed_train_file_path: str = os.path.join(self.data_transformation_dir,
                                                             DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                             TRAINING_FILE_NAME.replace("csv", "npy"))
                                                         
        self.transformed_test_file_path: str = os.path.join(self.data_transformation_dir,
                                                             DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                             TESTING_FILE_NAME.replace("csv", "npy"))
        
        self.transformed_object_file_path: str = os.path.join(self.data_transformation_dir,
                                                              DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
                                                              PREPROCESS_OBJECT_FILE_NAME)
        
class ModelTranierConfig:

    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.model_trainer_dir:str = os.path.join(training_pipeline_config.artifact_dir,
                                                  MODEL_TRAINER_DIR_NAME)
        
        self.trained_model_file_path:str = os.path.join(self.model_trainer_dir,
                                                        MODEL_TRAINER_TRAINED_MODEL_DIR,
                                                        MODEL_FILE_NAME)
        
        self.expected_accuarcy: float = MODEL_TRAINER_EXPECTED_SCORE
        self.overfitting_underfitting_threshold = MODEL_TRAINER_OVER_FITTING_UNDER_FITTING

class ModelEvaluationConfig:

    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.model_evaluation_dir:str = os.path.join(training_pipeline_config.artifact_dir,
                                                      MODEL_EVALUATION_DIR_NAME)
        
        self.report_file_path = os.path.join(self.model_evaluation_dir,
                                             MODEL_EVALUATION_REPORT_FILE_PATH)
        
        self.change_thresold = MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE
