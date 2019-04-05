import boto3

from AWSSecrets import ACCESS_KEY, SECRET_KEY

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)
bucket = s3.Bucket('pk-kapost-tech1')
for o in bucket.objects.all():
  print(o.key,o.size)
  if o.size > 10000000:
    copy_source = {
        'Bucket': 'pk-kapost-tech1',
        'Key':o.key
      }
    bucket = s3.Bucket('pk-kapost-tech2')
    bucket.copy(copy_source,o.key)
