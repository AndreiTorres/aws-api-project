from pydantic import BaseModel, Field

class Teacher(BaseModel):
    id: int = Field(ge = 0)
    numeroEmpleado: int = Field(ge = 1)
    nombres: str = Field(min_length = 1)
    apellidos: str = Field(min_length = 1)
    horasClase: int = Field(min = 0)  