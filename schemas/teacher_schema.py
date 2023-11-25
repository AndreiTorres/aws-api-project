from sqlalchemy import Column, Integer, String
from config.database import Base

class TeacherSchema(Base):
    __tablename__ = "profesores"
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    numeroEmpleado = Column(Integer)
    nombres = Column(String)
    apellidos = Column(String)
    horasClase = Column(Integer)  