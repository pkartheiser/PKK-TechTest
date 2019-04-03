import boto3

from AWSSecrets import ACCESS_KEY, SECRET_KEY

client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)
