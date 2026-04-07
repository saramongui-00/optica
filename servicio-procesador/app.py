from fastapi import FastAPI

app = FastAPI(title="Servicio Procesador")

@app.get("/health")
def health():
    return {"status": "Servicio Procesador OK"}

@app.get("/")
def root():
    return {"message": "Hola desde Python/FastAPI"}
