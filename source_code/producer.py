from kafka import KafkaProducer

import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers='127.0.0.1:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:

    data = {

        "temperature": round(random.uniform(20, 35), 2),

        "ph": round(random.uniform(5.5, 9.0), 2),

        "turbidity": random.randint(1, 100),

        "tds": random.randint(100, 1000),

        "water_level": random.randint(20, 100)
    }

    producer.send("water-quality", data)

    print("Produced:", data)

    time.sleep(2)