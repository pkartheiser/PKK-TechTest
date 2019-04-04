FROM python:3.7
RUN pip install boto3
COPY boto3credtest.py /
COPY boto3filesize.py /
COPY boto3copykey.py /
COPY AWSSecrets.py /
COPY boto3listtest.py /
ENTRYPOINT ["python","boto3filesize.py"]
