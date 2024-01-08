## Sensor project
```
export MONGO_DB_URL="mongodb+srv://dipendra=:dipendra=@cluster0.eaymsvp.mongodb.net/?retryWrites=true&w=majority"
export MONGO_DB_URL="mongodb+srv://dipendra_123:dipendra_123@cluster0.eaymsvp.mongodb.net/?retryWrites=true&w=majority"
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

## Data Drift Problem and Solution
```
For training pipeline
---------------------

Train adn test dataset must have same distribution
Base dataset: Train
To Compare with : Test
if same distribution : data is not drifted

Solution : If not then do train test split correctly

```
### Instant Prediction
Not possible to detect data drift immediately

#### Why ???
it is not possible to summarize one record in stats we need bunch of record then we can calculate (mean, median ,mode, distribution ) with single data point it is not possible

#### Solution
we can save each request in database,then we can fetch all request by hour by day


example: collected data of one day

we will go for the data drift detetection

In the train dataset, test dataset.
see the data drift report
```
if huge difference: 
     go for retraining 
else:
    we can keep checking data every day
```
#### For Batch prediction How we will detect data drift ->
---------------------------------------------
```
use training dataset as base
use batch data to compare data drift

if drift found
    send alert (data drift detected so retrain using new data set as well )
else:   
    do the prediction

```

### Concept Drift

it's related to model

```
where relation between input feature and target feature is changed

Solution :  Retrain the model
```



