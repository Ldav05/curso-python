from fastapi import APIRouter, HTTPException
from typing import Union
from pydantic import BaseModel


router = APIRouter(prefix="/products", tags=["producs"], responses={404: {"messsage": "No encontrado"}})
products_list =["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

@router.get("/")
async def get_all_products():
    return ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

@router.get("/{id}")
async def get_product_by_id(id: int):
    try:
        return products_list[id]
    except:
        raise HTTPException(status_code=404, detail="El producto no existe")
