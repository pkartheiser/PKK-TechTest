# PKK-TechTest
Kapost Tech Test
Boto3filesize.py script searches a designated s3 bucket and copies any files larger than 10mb to a destination bucket. 

Script assumes user is using a resource to feed AWS access key and secret key into boto3filesize.py
Example of aws key resource file is in this repo named AWSSecretsexample.py.
Boto3filesize.py is using AWSSecrets.py which is not listed in this repo

Dockerfile: loads a python3.7 base image, installs boto3, copies boto3filesize.py,AWSSecrets.py, then starts python and executes boto3filesize.py.

AWS Credentials are sourced from IAM service account with s3 access only.
