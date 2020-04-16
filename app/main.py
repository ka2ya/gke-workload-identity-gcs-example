import os

from google.auth.credentials import AnonymousCredentials
from google.cloud import storage
from google.cloud.storage.blob import Blob


BUCKET_NAME = os.environ["BUCKET_NAME"]

data = "OK!!"

credentials = AnonymousCredentials()

client = storage.Client(project="default", credentials=credentials)
bucket = client.bucket(BUCKET_NAME,)
bucket.create()
blob = bucket.blob('test.txt')
blob.upload_from_string(data)
blob2 = bucket.get_blob('test.txt', generation=0)
print(blob2._get_download_url())


# blob2 = Blob(
#     bucket=bucket,
#     name='test.txt',
#     encryption_key=None,
#     generation=0,
# )
# blob2.reload(client=client, timeout=10)
# blob2._properties['Generation'] = 1
# print(bucket.get_blob('TESTFILE').download_as_string())
# bucket = client.get_bucket(BUCKET_NAME)
# blob = bucket.get_blob('TESTFILE')
# resp = blob.upload_from_string(data)
# blob2 = bucket.blob('TESTFILE')
# resp_data = blob2.download_as_string()
# print(resp_data)
