import boto3

from AWSSecrets import ACCESS_KEY, SECRET_KEY #imports keyresource

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)
bucket = s3.Bucket('pk-kapost-tech1') #source bucket
for o in bucket.objects.all():
  print(o.key,o.size)
  if o.size > 10000000: #size listed in Bytes = 10Mb
    copy_source = {
        'Bucket': 'pk-kapost-tech1', #source bucket
        'Key':o.key
      }
    bucket = s3.Bucket('pk-kapost-tech2') #destination bucket
    bucket.copy(copy_source,o.key)
