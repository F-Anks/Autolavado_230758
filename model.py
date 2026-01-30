
"""
Modelo de datos para usuarios del sistema AutoLavado.
Define enums de género, roles y el modelo Usuario usando Pydantic.
"""

from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class Genero(str, Enum):
    """Enum que representa el género de un usuario."""
    MASCULINO = "Hombre"
    FEMENINO = "Mujer"
    OTRO = "Otro"


class Role(str, Enum):
    """Enum que representa los roles de un usuario en el sistema."""
    ADMIN = "admin"
    USER = "user"


class Usuario(BaseModel):
    """Modelo Pydantic que representa a un usuario del sistema."""
    id: Optional[UUID] = uuid4()
    primerNombre: str
    apellidos: str
    genero: Genero
    roles: List[Role]
