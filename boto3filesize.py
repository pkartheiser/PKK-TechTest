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

#mbthreshold = 10000000

#if o.size > mbthreshold
  #copy_source = {
        #'Bucket': 'pk-kapost-tech1',
        #'Key':
     # }
  #bucket = s3.Bucket('pk-kapost-tech2')
  #bucket.copy(copy_source, '')





#bucket = s3.Bucket('pk-kapost-tech1')
#size = 0
#for o in bucket.objects.all():
#        print (o), o.size
#        size += o.size
#print ('s3 size = %.3f MB' % (size/1024/1024))
