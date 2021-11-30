# from kafka import KafkaProducer


# TOPIC_NAME = 'location'
# KAFKA_SERVER = 'localhost:9093'

# producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

# producer.send(TOPIC_NAME, b'Teste de mensagem!!!')
# producer.flush()

import json

from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092', max_request_size=1048576, compression_type=None)

for i in range(10):
    data = { 'tag ': 'blah',
        'name' : 'sam',
        'index' : i,
        'score': 
            {'row1': 100,
             'row2': 200
        }
    }   
    producer.send('sample', json.dumps(data).encode('utf-8'))
    time.sleep(10)
