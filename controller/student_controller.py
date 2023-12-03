from typing import Annotated
from fastapi import APIRouter, Body, Response, status, HTTPException
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from model.student_model import Student
from service.student_service import StudentService

student_router = APIRouter()
studentService = StudentService()

@student_router.get("/alumnos")
def getAllStudents(response: Response):
    response.status_code = status.HTTP_200_OK
    response.media_type = "application/json"
    return studentService.get_all_students()

@student_router.post("/alumnos")
def saveStudent(student: Annotated[Student, Body()], response: Response):
        
        try:
            studentSaved = studentService.save_student(student)
        except Exception:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "An error has ocurred on the server")
        
        response.status_code = status.HTTP_201_CREATED
        response.media_type = "application/json"
        return studentSaved

@student_router.get("/alumnos/{id}")
def getStudentById(id: int, response: Response):
    try:
        student = studentService.get_student_by_id(id)
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "An error has ocurred on the server")
    
    if student:
        response.status_code = status.HTTP_200_OK
        response.media_type = "application/json"
        return student
    
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail = "Student not found")

@student_router.put("/alumnos/{id}")
def updateStudent(id: int, studentUpdated: Annotated[Student, Body()], response: Response):
    
    try:
        student = studentService.update_student(id, studentUpdated)
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "An error has ocurred on the server")
    
    if student:
        response.status_code = status.HTTP_200_OK
        response.media_type = "application/json"
        return student
     
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail = "Student not found")

@student_router.delete("/alumnos/{id}")
def deleteStudent(id: int, response: Response):
    try:
        wasDeleted = studentService.delete_student(id)
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "An error has ocurred on the server")
    
    if not wasDeleted:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = "Student not found")
    
    response.status_code = status.HTTP_200_OK

@student_router.post("/alumnos/{id}/email")
def sendEmail(id: int, response: Response):
    try:
        wasSend = studentService.send_email(id)
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "An error has ocurred on the server")
    
    if not wasSend:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = "Student not found")
    
    response.status_code = status.HTTP_200_OK