import os

from google.auth.credentials import AnonymousCredentials
from google.cloud import storage


BUCKET_NAME = os.environ["BUCKET_NAME"]

data = "OK!!"

credentials = AnonymousCredentials()

client = storage.Client(project="default", credentials=credentials)
bucket = client.bucket(BUCKET_NAME)
blob = bucket.blob('test.txt')
blob.upload_from_string(data)
blob2 = bucket.get_blob('test.txt')
print(blob2)
