from Sensor_Fault_Detection.Configration.mongo_operations import MongoOperations

db_client = MongoOperations()
db_client.create_collection()
db_client.upload_csv_to_collection()