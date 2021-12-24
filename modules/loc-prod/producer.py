# create a simple kafka producer using the kafka-python library
# the message is sent to the topic 'test'
# detect localhost and use the default port
# the message should be sent as gRPC message based on the protobuf specification in the file 'location.proto'
import logging
import os

from kafka import KafkaProducer


# kafka_url = os.environ["KAFKA_URL"]
kafka_url = "location-kafka-0.location-kafka-headless.default.svc.cluster.local:9092"
# kafka_topic = os.environ["KAFKA_TOPIC"]
kafka_topic = "test"
logging.info('connecting to kafka ', kafka_url)
logging.info('connecting to kafka topic ', kafka_topic)
# producer = KafkaProducer(bootstrap_servers=kafka_url)
producer = KafkaProducer(bootstrap_servers='location-kafka-0.location-kafka-headless.default.svc.cluster.local:9092')

# producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

producer.send(kafka_topic, b'Test Message!!!')
producer.flush()