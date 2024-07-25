
FROM python:3.12

RUN apt-get update && apt-get install -y protobuf-compiler pipenv kafkacat

RUN mkdir /kafka_ex/

WORKDIR /kafka_ex/

COPY Pipfile.lock /kafka_ex/

RUN pipenv requirements > requirements.txt

RUN pip install -r requirements.txt
