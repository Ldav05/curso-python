from fastapi import FastAPI
from routers import products, users
from typing import Union

app = FastAPI() 

# Routers
app.include_router(products.router)
app.include_router(users.router)

@app.get("/") # Especifica la direción a la cual se hace la petición
async def root():  # Definimos la función como asíncrona
    return "¡Hola FastAPI!"

@app.get("/url") 
async def url():  
    return {"url": "https://lgordon.online"}

# Inicia el server: uvicorn main:app --reload
# Detiene el server : Ctrl + c