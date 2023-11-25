
from sqlalchemy import Column, Float, Integer, String
from config.database import Base

class StudentSchema(Base):
    __tablename__ = "alumnos"

    id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    nombres = Column(String)
    apellidos = Column(String)
    matricula = Column(String)
    promedio = Column(Float)
    fotoPerfilUrl = Column(String)
    password = Column(String)