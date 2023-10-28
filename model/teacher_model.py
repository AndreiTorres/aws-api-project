from pydantic import BaseModel

class Teacher(BaseModel):
    id: int
    employeeNumber: int
    firstname: str
    lastname: str
    classhours: float