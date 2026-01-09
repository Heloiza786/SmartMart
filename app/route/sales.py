from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from app.database.database import SessionLocal
from app.database.models import SaleModel

router = APIRouter(prefix="/sales", tags=["sales"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schemas
class SaleCreate(BaseModel):
    product_id: int
    month: int
    quantity: int
    total_price: float

class SaleResponse(BaseModel):
    id: int
    product_id: int
    month: int
    quantity: int
    total_price: float

    class Config:
        from_attributes = True

# create sale
@router.post("/", response_model=SaleResponse, status_code=201)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    db_sale = SaleModel(
        product_id=sale.product_id,
        month=sale.month,
        quantity=sale.quantity,
        total_price=sale.total_price
    )
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

# get all sales 
@router.get("/", response_model=List[SaleResponse])
def get_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sales = db.query(SaleModel).offset(skip).limit(limit).all()
    return sales

# get by id sale 
@router.get("/{sale_id}", response_model=SaleResponse)
def get_sale(sale_id: int, db: Session = Depends(get_db)):
    sale = db.query(SaleModel).filter(SaleModel.id == sale_id).first()
    if not sale:
        raise HTTPException(status_code=404, detail="Venda não encontrada")
    return sale

# Delete sale
@router.delete("/{sale_id}")
def delete_sale(sale_id: int, db: Session = Depends(get_db)):
    sale = db.query(SaleModel).filter(SaleModel.id == sale_id).first()
    if not sale:
        raise HTTPException(status_code=404, detail="Venda não encontrada")
    
    db.delete(sale)
    db.commit()
    return {"message": "Venda deletada com sucesso"}