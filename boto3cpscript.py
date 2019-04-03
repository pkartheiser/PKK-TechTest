import boto3

from AWSSecrets import ACCESS_KEY, SECRET_KEY

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

bucket = s3.Bucket('pk-kapost-tech1')
size = 0

for o in bucket.objects.all():
    if '<your_filter>' in o.key:
        print o, o.size
        size += o.size
print 's3 size = %.3f GB' % (size/1024/1024/1024)
