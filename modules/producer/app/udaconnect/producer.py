import time
from concurrent import futures
import grpc
import location_pb2
import location_pb2_grpc
import logging
import os
import sys
from kafka import KafkaProducer

# KAFKA_URL = "location-kafka-0.location-kafka-headless.default.svc.cluster.local:9092"
# TOPIC_NAME = "test"
KAFKA_URL = os.environ["KAFKA_URL"]
TOPIC_NAME = os.environ["KAFKA_TOPIC"]

logging.basicConfig(level=logging.INFO)

def main():
    producer = KafkaProducer(bootstrap_servers=KAFKA_URL)
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = location_pb2_grpc.LocationStub(channel)
        response = stub.GetLocation(location_pb2.GetLocationRequest())
        location = response.location
        print(location)
        producer.send(TOPIC_NAME, location.SerializeToString())
        producer.flush()
        time.sleep(1)


if __name__ == '__main__':
    main()