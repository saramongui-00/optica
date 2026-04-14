from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.appointment_controller import router
from dotenv import load_dotenv
import os
import py_eureka_client.eureka_client as eureka_client
import threading

load_dotenv()

app = FastAPI(title="Servicio de Citas", version="1.0")

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
    port = int(os.getenv("PORT", 8002))
    
    def register_eureka():
        eureka_client.init(
            eureka_server="http://eureka-server:8761/eureka",
            app_name="servicio-citas",
            instance_port=port,
            instance_host="servicio-citas"
        )
        print("✅ Servicio de Citas registrado en Eureka")
    
    thread = threading.Thread(target=register_eureka)
    thread.start()
    
    print(f"🚀 Servicio de Citas iniciado en puerto {port}")

@app.on_event("shutdown")
async def shutdown_event():
    eureka_client.stop()
    print("👋 Servicio de Citas detenido")

@app.get("/health")
async def health():
    return {"status": "Servicio Citas OK"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8002))
    uvicorn.run(app, host="0.0.0.0", port=port)