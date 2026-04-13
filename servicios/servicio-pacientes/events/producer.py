from kafka import KafkaProducer
import json
import os

class PatientEventProducer:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=os.getenv("KAFKA_URL", "localhost:9092"),
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    async def send_event(self, topic: str, event: str):
        self.producer.send(topic, value=event)
        self.producer.flush()