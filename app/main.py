from fastapi import FastAPI
from app.database.database import engine
from app.database import models

app = FastAPI(title="SmartMart API")

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "API rodando com banco"}
