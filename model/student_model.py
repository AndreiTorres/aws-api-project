from pydantic import BaseModel, Field

class Student(BaseModel):
    id: int = Field(gt = 0)
    nombres: str = Field(min_length = 1)
    apellidos: str = Field(min_length = 1)
    matricula: str = Field(min_length = 1)
    promedio: float = Field(min = 0)