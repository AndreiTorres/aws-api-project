from fastapi import APIRouter, Body, Response, status, HTTPException
from typing import Annotated
from service.teacher_service import TeacherService
from model.teacher_model import Teacher

teacher_router = APIRouter()
teacherService = TeacherService()

@teacher_router.get("/profesores")
def getAllTeachers(response: Response):
    response.status_code = status.HTTP_200_OK
    response.media_type = "application/json"
    return teacherService.get_all_teachers()

@teacher_router.post("/profesores")
def saveTeacher(teacher: Annotated[Teacher, Body()], response: Response):
        
        try:
            new_teacher = teacherService.save_teacher(teacher)
        except Exception:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "An error has ocurred on the server")
        
        response.status_code = status.HTTP_201_CREATED
        response.media_type = "application/json"

        return new_teacher

@teacher_router.get("/profesores/{id}")
def getTeacherById(id: int, response: Response):
    
    try:
        teacher = teacherService.get_teacher_by_id(id)
    except Exception:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "An error has ocurred on the server")
    
    if teacher:
        response.status_code = status.HTTP_200_OK
        response.media_type = "application/json"
        return teacher
    
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail = "Teacher not found")

@teacher_router.put("/profesores/{id}")
def updateTeacher(id: int, teacherUpdated: Annotated[Teacher, Body()], response: Response):
    
    try:
        teacher = teacherService.update_teacher(id, teacherUpdated)
    except Exception:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "An error has ocurred on the server")
    
    if teacher:
        response.status_code = status.HTTP_200_OK
        response.media_type = "application/json"
        return teacher
     
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail = "Teacher not found")

@teacher_router.delete("/profesores/{id}")
def deleteTeacher(id: int, response: Response):

    try:
        wasDeleted = teacherService.delete_teacher(id)
    except Exception:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "An error has ocurred on the server")
    
    if not wasDeleted:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = "Teacher not found")
    
    response.status_code = status.HTTP_200_OK