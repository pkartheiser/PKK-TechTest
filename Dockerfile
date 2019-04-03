FROM python:3.7
RUN pip install boto3
COPY boto3credtest.py /
COPY AWSSecrets.py /
ENTRYPOINT ["python",boto3credtest.py"]
