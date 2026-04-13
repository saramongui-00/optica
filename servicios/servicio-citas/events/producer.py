import json
import os
from aiokafka import AIOKafkaProducer

class AppointmentEventProducer:
    def __init__(self):
        self.producer = None
        self.bootstrap_servers = os.getenv("KAFKA_URL", "localhost:9092")
        self.topic = "appointment-events"

    async def start(self):
        if not self.producer:
            self.producer = AIOKafkaProducer(
                bootstrap_servers=self.bootstrap_servers,
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            await self.producer.start()
            print(f"✅ Kafka Producer conectado a {self.bootstrap_servers}")

    async def stop(self):
        if self.producer:
            await self.producer.stop()
            self.producer = None
            print("✅ Kafka Producer detenido")

    async def send_appointment_created(self, appointment_id: str, appointment_data: dict):
        if self.producer:
            event = {
                "event_type": "APPOINTMENT_CREATED",
                "appointment_id": appointment_id,
                "date": appointment_data.get("date"),
                "time": appointment_data.get("time"),
                "patient_document": appointment_data.get("patient", {}).get("document")
            }
            await self.producer.send_and_wait(self.topic, event)
            print(f"📨 Evento enviado: APPOINTMENT_CREATED")