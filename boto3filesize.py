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

bthreshold = 10000000

if o.size > bthreshold:
    print("yes")
  #copy_source = {
        #'Bucket': 'pk-kapost-tech1',
        #'Key':
     # }
  #bucket = s3.Bucket('pk-kapost-tech2')
  #bucket.copy(copy_source, '')
