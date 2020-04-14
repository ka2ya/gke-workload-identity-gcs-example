import os
from google.cloud import storage
from google.auth.credentials import AnonymousCredentials

BUCKET_NAME = os.environ["BUCKET_NAME"]

data = "OK!!"

credentials = AnonymousCredentials()
client = storage.Client(project="default", credentials=credentials)

bucket = client.get_bucket(BUCKET_NAME)
blob = bucket.get_blob('TESTFILE')
resp = blob.upload_from_string(data)
blob2 = bucket.blob('TESTFILE')
resp_data = blob2.download_as_string()

print(resp_data)
