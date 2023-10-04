from Sensor_Fault_Detection.Configration.mongodb_connection import MongoDBClient
from Sensor_Fault_Detection.exception import SensorException
import os, sys
from Sensor_Fault_Detection.logger import logging
from Sensor_Fault_Detection.Configration.mongo_operations import MongoOperations
from Sensor_Fault_Detection.entity.config_entity import TrainingPipelineConfig, DataIngetionConfig
from Sensor_Fault_Detection.pipeline.training_pipeline import TrainingPipeline
from Sensor_Fault_Detection.data_access.Export_DB_data import ExportData
from Sensor_Fault_Detection.pipeline.training_pipeline import TrainingPipeline



if __name__ == "__main__":
    training_pipeline = TrainingPipeline()
    training_pipeline.run_pipeline()

# # Example usage:
# if __name__ == "__main__":
#     exporter = ExportData()
#     df = exporter.export_collection_as_dataframe()
#     print(df.head())  
#     print(df.shape)



# if __name__ == "__main__":
#     training_pipeline = TrainingPipeline()
#     training_pipeline.run_pipeline()



# if __name__ == "__main__":
#     config = TrainingPipelineConfig()
#     data_ingetion_config = DataIngetionConfig(config)
#     print(data_ingetion_config.__dict__)

# if __name__ == "__main__":
#     db_client = MongoOperations()
#     db_client.create_database()
#     db_client.create_collection()
#     # db_client.upload_csv_to_collection()

# # if __name__ == "__main__":
# #     db_client = MongoOperations()
# #     database_name = "sensor"  # Change this to your desired database name
# #     collection_name = "sensor_data"  # Change this to your desired collection name
# #     csv_file_path = r"F:\End_To_End_project\Sensor-Fault-Detection\Data\aps_failure_training_set1.csv"  # Change this to the path of your CSV file

# #     db_client.create_database(database_name)
# #     db_client.create_collection(database_name, collection_name)
# #     db_client.upload_csv_to_collection(database_name, collection_name, csv_file_path)
# # def test():
# #     logging.info("we are dividing  by zero/....")
# #     try:
# #         x =1/0
# #         return x
# #     except Exception as e:
# #         raise SensorException(e, sys)

# if __name__ == "__main__":
#     # # pass
#     # try:
#     #     test()
#     # except Exception as e
#     #     logging.error(e)

#     # step:1 checking mongo connecction
#     mongo_db = MongoDBClient()
#     print(f"Collection name : {mongo_db.database.list_collection_names()}")