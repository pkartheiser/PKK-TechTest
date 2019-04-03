FROM python:3.7
RUN pip install boto3
COPY Boto3credtest.py /
ENTRYPOINT ["python","boto3credtest.py"]
