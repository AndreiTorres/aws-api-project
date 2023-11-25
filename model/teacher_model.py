from pydantic import BaseModel, Field

class Teacher(BaseModel):

    numeroEmpleado: int = Field(ge = 1)
    nombres: str = Field(min_length = 1)
    apellidos: str = Field(min_length = 1)
    horasClase: int = Field(min = 0)  

    class Config:
        orm_mode = True