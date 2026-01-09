from fastapi import FastAPI
from app.database.database import engine
from app.database import models
from app.route import sales  # Importe o router

app = FastAPI(title="SmartMart API")

models.Base.metadata.create_all(bind=engine)

# Registre o router
app.include_router(sales.router)

@app.get("/")
def root():
    return {"status": "API rodando com banco"}