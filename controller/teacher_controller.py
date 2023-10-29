from fastapi import APIRouter, Body, Response, status, HTTPException
from typing import Annotated
from service.teacher_service import TeacherService
from model.teacher_model import Teacher

teacher_router = APIRouter()
teacherService = TeacherService()

@teacher_router.get("/profesores")
def getAllStudents(response: Response):
    response.status_code = status.HTTP_200_OK
    response.media_type = "application/json"
    return teacherService.get_all_teachers()

@teacher_router.post("/profesores")
def saveStudent(teacher: Annotated[Teacher, Body()], response: Response):
        response.status_code = status.HTTP_201_CREATED
        response.media_type = "application/json"
        teacherService.save_teacher(teacher)
        return teacher

@teacher_router.get("/profesores/{id}")
def getStudentById(id: int, response: Response):
    teacher = teacherService.get_teacher_by_id(id)
    if teacher:
        response.status_code = status.HTTP_200_OK
        response.media_type = "application/json"
        return teacher
    
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail = "Teacher not found")

@teacher_router.put("/profesores/{id}")
def updateStudent(id: int, teacherUpdated: Annotated[Teacher, Body()], response: Response):
    student = teacherService.update_teacher(id, teacherUpdated)

    if student:
        response.status_code = status.HTTP_200_OK
        response.media_type = "application/json"
        return teacherUpdated
     
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail = "Teacher not found")

@teacher_router.delete("/profesores/{id}")
def deleteStudent(id: int, response: Response):

    wasDeleted = teacherService.delete_teacher(id)

    if not wasDeleted:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = "Teacher not found")
    
    response.status_code = status.HTTP_200_OK