from fastapi import FastAPI
from controllers.patient_controller import router
from services.patient_service import PatientService
from events.consumer import PatientEventConsumer
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Servicio de Pacientes", version="1.0")

app.include_router(router)

service = PatientService()
consumer = PatientEventConsumer(service)

@app.on_event("startup")
async def startup_event():
    consumer.start_listening()
    print("Servicio de Pacientes iniciado en puerto 8001")

@app.get("/health")
async def health():
    return {"status": "Servicio Pacientes OK"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)