from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import engine, Base
from app.database.models import CategoryModel, ProductModel, SaleModel
from app.route import sales, category, products, chart_sale

app = FastAPI(title="SmartMart API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(sales.router)
app.include_router(category.router)
app.include_router(products.router)
app.include_router(chart_sale.router)
@app.get("/")
def root():
    return {"status": "API rodando com banco"}
