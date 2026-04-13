from kafka import KafkaConsumer
import json
import os
import threading

class PatientEventConsumer:
    def __init__(self, patient_service):
        self.consumer = KafkaConsumer(
            "patient-events",
            bootstrap_servers=os.getenv("KAFKA_URL", "localhost:9092"),
            value_deserializer=lambda v: json.loads(v.decode('utf-8')),
            auto_offset_reset='earliest',
            group_id='patient-service-group'
        )
        self.service = patient_service

    def start_listening(self):
        def consume():
            for message in self.consumer:
                event = message.value
                print(f"Evento recibido: {event}")
                if event.get("event_type") == "APPOINTMENT_CREATED":
                    print(f"Cita creada para paciente: {event.get('patient_id')}")
        
        thread = threading.Thread(target=consume, daemon=True)
        thread.start()