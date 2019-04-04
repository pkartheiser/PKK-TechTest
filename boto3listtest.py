import boto3

from AWSSecrets import ACCESS_KEY, SECRET_KEY

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)
my_bucket = s3.Bucket('pk-kapost-tech1')

for file in my_bucket.objects.all():
    print(file.key)
