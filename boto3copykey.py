import boto3

from AWSSecrets import ACCESS_KEY, SECRET_KEY

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

copy_source = {
      'Bucket': 'pk-kapost-tech1',
      'Key': 'pylekitty.jpg'
    }
bucket = s3.Bucket('pk-kapost-tech2')
bucket.copy(copy_source, 'pylekitty.jpg')
