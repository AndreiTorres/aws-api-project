from pydantic import BaseModel, Field
from config.database import Base

class Student(BaseModel):

    nombres: str = Field(min_length = 1)
    apellidos: str = Field(min_length = 1)
    matricula: str = Field(min_length = 1)
    promedio: float = Field(min = 0)
    fotoPerfilUrl: str = ''
    password: str   

    class Config:
        orm_mode = True