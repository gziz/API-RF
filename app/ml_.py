import pickle
# import boto3


# BUCKET_NAME = 'serverless-machine-learning'
# MODEL_FILE_NAME = 'model.pkl'
# S3 = boto3.client('s3', region_name='eu-central-1')

def predict_rf(data):
    loaded_rf = pickle.load(open("./random_forest.pkl", 'rb') )
    predictions = loaded_rf.predict(data)
    return list(predictions)
