from fastapi import APIRouter, HTTPException
from typing import Union
from pydantic import BaseModel

router = APIRouter(prefix= "/users", tags=["users"], responses={404: {"message": "No encontrado"}})

# Inicia el server: uvicorn users:app --reload

# Entidad user


class User(BaseModel): # Indispensabe crear la clase con BaseModel
    id: int
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(id = 1, name = "Luis",surname = "Gordon", url = "https://lgordon.online", age = 22),
        User(id = 2, name = "David",surname = "Rodriguez", url = "https://drodriguez.online", age = 22)]


@router.get("/json")
async def usersjson():
    return [{"name": "Luis", "surname": "Gordon", "url": "https://lgordon.online", "age": 22},
            {"name": "David", "surname": "Rodriguez", "url": "https://drodriguez.online", "age": 22},
            {"name": "prueba", "surname": "prueba", "url": "https://prueba.online", "age": 22}]

@router.get("/")
async def get_all_users():
    return users_list

# Path

@router.get("/{id}", response_model= User)
async def get_user_by_id(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
    
    # Querys
    
@router.get("/query") # Ejemplo de query:http://127.0.0.1:8000/userquery/?id=1
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    return search_user(id)
    
# POST (Insertar)
    
@router.post("/", response_model= User, status_code=201) # Se cambia la respuesta del status code
async def insert_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe") # Se hace uso de excepciones HTTP
    else:
        users_list.routeend(user) # Agregar el nuevo usuario a la lista
    
# PUT (Actualizar)

@router.put("/")  
async def update_user(user: User):
    
    found = False
    
    for index,saved_user in enumerate(users_list): # Enumera la lista y guarda el valor en la variable index
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"Error": "No se ha actualizado el usuario"}
    else:
        return {"OK": "Se ha actualizado el usuario"}
    
    
@router.delete("/{id}")  # Cuando es obligatorio usamos la forma path
async def delete_user(id: int):
    
    found = False
    
    for index,saved_user in enumerate(users_list): # Enumera la lista y guarda el valor en la variable index
        if saved_user.id == id:
            del users_list[index]  
            found = True
            
    if not found:
        return {"Error": "No se ha eliminado el usuario"}
    else:
        return {"OK": "Se ha eliminado el usuario"}    

    
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
    
    
