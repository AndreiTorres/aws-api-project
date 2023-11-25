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
        response.status_code = status.HTTP_201_CREATED
        response.media_type = "application/json"
        studentSaved = studentService.save_student(student)
        return studentSaved

@student_router.get("/alumnos/{id}")
def getStudentById(id: int, response: Response):
    student = studentService.get_student_by_id(id)
    
    if student:
        response.status_code = status.HTTP_200_OK
        response.media_type = "application/json"
        return student
    
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail = "Student not found")

@student_router.put("/alumnos/{id}")
def updateStudent(id: int, studentUpdated: Annotated[Student, Body()], response: Response):
    student = studentService.update_student(id, studentUpdated)

    if student:
        response.status_code = status.HTTP_200_OK
        response.media_type = "application/json"
        return student
     
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail = "Student not found")

@student_router.delete("/alumnos/{id}")
def deleteStudent(id: int, response: Response):

    wasDeleted = studentService.delete_student(id)

    if not wasDeleted:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = "Student not found")
    
    response.status_code = status.HTTP_200_OK
