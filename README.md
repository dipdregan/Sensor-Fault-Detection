## Sensor project
```
export MONGO_DB_URL="mongodb+srv://dipendra=:dipendra=@cluster0.eaymsvp.mongodb.net/?retryWrites=true&w=majority"
show the url
echo $MONGO_DB_URL

```

```reading url code
import os

mongo_db_url = os.environ.get('MONGO_DB_URL')

if mongo_db_url:
    print(f'MongoDB URL: {mongo_db_url}')
else:
    print('MONGO_DB_URL environment variable is not set.')

```