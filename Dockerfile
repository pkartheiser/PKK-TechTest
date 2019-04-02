FROM python:3.7
RUN pip install boto3
COPY helloworld.py /
ENTRYPOINT ["python","helloworld.py"]
