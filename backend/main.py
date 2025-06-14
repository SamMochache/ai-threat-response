from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Threat Detection API",
    description="Receives logs and returns alert data",
    version="1.0.0"
)

app.include_router(router)
