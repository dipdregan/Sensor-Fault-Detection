class TargetValueMapping:
    def __init__(self):
        self.negative = 0
        self.positive = 1

    def to_dict(self):
        return self.__dict__
    
    def reverse_mapping(self):
        mapping_responce = self.to_dict()
        return dict(zip(mapping_responce.values(),mapping_responce.keys()))