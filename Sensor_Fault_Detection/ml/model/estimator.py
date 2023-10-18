class TargetValueMapping:
    def __init__(self):
        self.negative = 0
        self.positive = 1

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
