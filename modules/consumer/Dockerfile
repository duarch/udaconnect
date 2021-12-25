FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install grpcio-tools
RUN pip install -r requirements.txt 

EXPOSE 5000

COPY . .
CMD ["python","app/udaconnect/consumer.py"]