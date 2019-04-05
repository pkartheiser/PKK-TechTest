FROM python:3.7
RUN pip install boto3
COPY boto3filesize.py /
COPY AWSSecrets.py /
ENTRYPOINT ["python","boto3filesize.py"]
