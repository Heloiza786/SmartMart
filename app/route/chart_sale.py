from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from datetime import date
from pydantic import BaseModel

from app.database.database import SessionLocal
from app.database.models import SaleModel

router = APIRouter(prefix="/charts", tags=["chartsSale"])



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class SalesChartResponse(BaseModel):
    date: date
    total_quantity: int
    total_revenue: float

    class Config:
        from_attributes = True


@router.get("/sales", response_model=List[SalesChartResponse])
def get_sales_chart(db: Session = Depends(get_db)):
    """
    Retorna dados agregados de vendas por dia.
    Ideal para gráficos (linha, barra, etc).
    """
    data = (
        db.query(
            SaleModel.sale_date.label("date"),
            func.sum(SaleModel.quantity).label("total_quantity"),
            func.sum(SaleModel.total_price).label("total_revenue"),
        )
        .group_by(SaleModel.sale_date)
        .order_by(SaleModel.sale_date)
        .all()
    )

    return data
