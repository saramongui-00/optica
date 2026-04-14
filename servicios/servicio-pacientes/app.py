from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.patient_controller import router
from dotenv import load_dotenv
import os
import py_eureka_client.eureka_client as eureka_client
import threading

load_dotenv()

app = FastAPI(title="Servicio de Pacientes", version="1.0")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    # Obtener el puerto desde variable de entorno (Docker) o usar 8001 por defecto
    port = int(os.getenv("PORT", 8001))
    
    # Función para registrar en Eureka (se ejecuta en otro hilo para no bloquear)
    def register_eureka():
        eureka_client.init(
            eureka_server="http://eureka-server:8761/eureka",
            app_name="servicio-pacientes",
            instance_port=port,
            instance_host="servicio-pacientes"  # Nombre del servicio en Docker
        )
        print("✅ Servicio de Pacientes registrado en Eureka")
    
    # Ejecutar en hilo separado
    thread = threading.Thread(target=register_eureka)
    thread.start()
    
    print(f"🚀 Servicio de Pacientes iniciado en puerto {port}")

@app.on_event("shutdown")
async def shutdown_event():
    eureka_client.stop()
    print("👋 Servicio de Pacientes detenido")

@app.get("/health")
async def health():
    return {"status": "Servicio Pacientes OK"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8001))
    uvicorn.run(app, host="0.0.0.0", port=port)