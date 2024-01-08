class TargetValueMapping:
    def __init__(self):
        self.neg = 0
        self.pos = 1

    def to_dict(self):
        return self.__dict__
    
    def reverse_mapping(self):
        mapping_responce = self.to_dict()
        return dict(zip(mapping_responce.values(),mapping_responce.keys()))
    

class SensorModel:

    def __init__(self, preprocessor, model) -> None:
        self.preprocessor = preprocessor
        self.model = model

    def predict(self, x):
        try:
            self.preprocessor.transform(x)
            y_hat = self.model.predict(x)
            return y_hat


        except Exception as e:
            raise e

from Sensor_Fault_Detection.constants.Training_pipeline import SAVE_MODEL_DIR, MODEL_FILE_NAME
import os

class ModelResolver:
    def __init__(self, model_dir=SAVE_MODEL_DIR):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise e
        
    def get_best_model_path(self):
        try:
            timestamp = list(map(int, os.listdir(self.model_dir)))
            latest_timestemp = max(timestamp)
            latest_model_path = os.path.join(self.model_dir,f"{latest_timestemp}",MODEL_FILE_NAME)
            return latest_model_path
        except Exception as e:
            raise e
    
    def is_model_exists(self)->bool:
        try:
            if not os.path.exists(self.model_dir):
                return False
            
            timestamps = os.listdir(self.model_dir)
            if len(timestamps)==0:
                return False
            latest_model_path = self.get_best_model()
            if not os.path.exists(latest_model_path):
                return False
            return True
        except Exception as e:
            raise e
