from fastapi import FastAPI, HTTPException # <--- Agregamos HTTPException
from typing import List
from uuid import UUID
from model import Genero, Role, Usuario

app = FastAPI()

db: List[Usuario] = [
    Usuario(
        primerNombre="Francisco", 
        apellidos="Garcia", 
        genero=Genero.masculino, 
        roles=[Role.admin]),
    
    Usuario(
        primerNombre="Raul", 
        apellidos="Rufino Pazos", 
        genero=Genero.masculino, 
        roles=[Role.user]),
    
    Usuario(
        primerNombre="Edwin", 
        apellidos="Cabrera Tecorralco", 
        genero=Genero.masculino, 
        roles=[Role.user])
]

@app.get("/")
async def read_root():
    return {"mensaje": "Hola pequeños de 8A DSM"}

@app.get("/api/v1/users")
async def get_users():
    return db

@app.get("/api/v1/users/{user_id}")
async def get_user_by_id(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user
    
    raise HTTPException(status_code=404, detail=f"Usuario con id {user_id} no encontrado")

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"mensaje": f"Usuario con id {user_id} eliminado exitosamente"}
            
    raise HTTPException(status_code=404, detail=f"Usuario con id {user_id} no encontrado")

@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, user_update: Usuario):
    for user in db:
        if user.id == user_id:
            # Actualizamos los campos con la información que llega
            if user_update.primerNombre is not None:
                user.primerNombre = user_update.primerNombre
            if user_update.apellidos is not None:
                user.apellidos = user_update.apellidos
            if user_update.genero is not None:
                user.genero = user_update.genero
            if user_update.roles is not None:
                user.roles = user_update.roles
            
            return user
            
    raise HTTPException(status_code=404, detail=f"Usuario con id {user_id} no encontrado")