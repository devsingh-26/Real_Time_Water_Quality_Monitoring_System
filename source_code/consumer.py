from kafka import KafkaConsumer

import json

from ai_service import analyze_water

consumer = KafkaConsumer(
    'water-quality',

    bootstrap_servers='127.0.0.1:9092',

    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Water Quality Consumer Started...")

for message in consumer:

    data = message.value

    result = analyze_water(data)

    print(result)