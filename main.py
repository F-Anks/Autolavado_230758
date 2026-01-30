"""
API REST básica con FastAPI para la gestión de usuarios.

Incluye operaciones CRUD en memoria utilizando UUID como identificador,
roles y género definidos mediante enums.
"""

from typing import List
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException

from model import Genero, Role, Usuario

app = FastAPI()

db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        primerNombre="Jose Francisco",
        apellidos="Flores Amador",
        genero=Genero.MASCULINO,
        roles=[Role.USER]
    ),
    Usuario(
        id=uuid4(),
        primerNombre="Luis Angel",
        apellidos="Flores Amador",
        genero=Genero.MASCULINO,
        roles=[Role.USER]
    )
]


@app.get("/")
async def root():
    """Endpoint raíz que devuelve un mensaje de bienvenida."""
    return {"message": "Hola Mundo"}


@app.get("/api/v1/user")
async def get_user():
    """Obtiene la lista completa de usuarios."""
    return db


@app.get("/api/v1/user/{user_id}", response_model=Usuario)
async def get_user_by_id(user_id: UUID):
    """Obtiene un usuario específico por su ID."""
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.delete("/api/v1/user/{user_id}")
async def delete_user(user_id: UUID):
    """Elimina un usuario por su ID."""
    for index, user in enumerate(db):
        if user.id == user_id:
            db.pop(index)
            return {"message": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.put("/api/v1/user/{user_id}", response_model=Usuario)
async def update_user(user_id: UUID, user_update: Usuario):
    """Actualiza la información de un usuario existente."""
    for index, user in enumerate(db):
        if user.id == user_id:
            user_update.id = user_id
            db[index] = user_update
            return user_update
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
