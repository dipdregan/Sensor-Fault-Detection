import os

mongo_db_url = os.environ.get('MONGO_DB_URL')

if mongo_db_url:
    print(f'MongoDB URL: {mongo_db_url}')
else:
    print('MONGO_DB_URL environment variable is not set.')