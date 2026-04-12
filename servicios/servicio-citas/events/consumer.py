import json
import os
import asyncio
from aiokafka import AIOKafkaConsumer

class AppointmentEventConsumer:
    def __init__(self):
        self.consumer = None
        self.bootstrap_servers = os.getenv("KAFKA_URL", "localhost:9092")
        self.topic = "appointment-events"
        self.group_id = "appointment-service-group"
        self._consumer_task = None

    async def start(self):
        if not self.consumer:
            self.consumer = AIOKafkaConsumer(
                self.topic,
                bootstrap_servers=self.bootstrap_servers,
                group_id=self.group_id,
                value_deserializer=lambda v: json.loads(v.decode('utf-8')),
                auto_offset_reset='earliest'
            )
            await self.consumer.start()
            print(f"✅ Kafka Consumer conectado a {self.bootstrap_servers}")
            self._consumer_task = asyncio.create_task(self._consume_loop())

    async def stop(self):
        if self._consumer_task:
            self._consumer_task.cancel()
        if self.consumer:
            await self.consumer.stop()
            self.consumer = None
            print("✅ Kafka Consumer detenido")

    async def _consume_loop(self):
        try:
            async for msg in self.consumer:
                event = msg.value
                event_type = event.get("event_type")
                
                if event_type == "APPOINTMENT_CREATED":
                    print(f"📥 Evento recibido: Cita {event.get('appointment_id')} creada para paciente {event.get('patient_document')}")
                elif event_type == "APPOINTMENT_CANCELLED":
                    print(f"📥 Evento recibido: Cita {event.get('appointment_id')} cancelada")
                elif event_type == "APPOINTMENT_UPDATED":
                    print(f"📥 Evento recibido: Cita {event.get('appointment_id')} actualizada")
        except asyncio.CancelledError:
            print("Consumer loop cancelado")
        except Exception as e:
            print(f"❌ Error en consumer: {e}")