from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.appointment_controller import router
from dotenv import load_dotenv
import os

load_dotenv()

# Kafka solo si la URL está configurada
KAFKA_URL = os.getenv("KAFKA_URL", "")
USE_KAFKA = KAFKA_URL != ""

if USE_KAFKA:
    from events.producer import AppointmentEventProducer
    from events.consumer import AppointmentEventConsumer
    producer = AppointmentEventProducer()
    consumer = AppointmentEventConsumer()

@asynccontextmanager
async def lifespan(app: FastAPI):
    if USE_KAFKA:
        await producer.start()
        await consumer.start()
        print("🚀 Servicio de Citas con Kafka iniciado")
    else:
        print("🚀 Servicio de Citas iniciado (Kafka desactivado)")
    yield
    if USE_KAFKA:
        await producer.stop()
        await consumer.stop()
        print("👋 Servicio de Citas detenido")

app = FastAPI(title="Appointment Service", version="1.0", lifespan=lifespan)

# Configurar CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/health")
async def health():
    return {"status": "Appointment Service OK"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)