from kafka import KafkaConsumer
import os
import json
from sqlalchemy import create_engine

# Setting Constants
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]
KAFKA_URL = os.environ["KAFKA_URL"]
TOPIC_NAME = os.environ["KAFKA_TOPIC"]

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[KAFKA_URL])

# Only to test
for message in consumer:
    print (message)

# # Consuming data 
# def collect_data(location):
#     conn = create_engine(f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)
#     cur = conn.cursor()
#     user_id = int(location["userId"])
#     latitude, longitude = int(location["latitude"]), int(location["longitude"])
#     db_data = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}))" \
#         .format(user_id, latitude, longitude)

#     print(db_data)
#     cur.execute(db_data)


for topic in consumer:
    location_message = json.loads(topic.value.decode('utf-8'))
    print (location_message)