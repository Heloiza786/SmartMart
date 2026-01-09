from fastapi import FastAPI
from app.database.database import engine, Base
from app.database.models import CategoryModel, ProductModel, SaleModel
from app.route import sales
from app.route import category
from app.route import products

app = FastAPI(title="SmartMart API")


Base.metadata.create_all(bind=engine)


app.include_router(sales.router)
app.include_router(category.router)
app.include_router(products.router)

@app.get("/")
def root():
    return {"status": "API rodando com banco"}