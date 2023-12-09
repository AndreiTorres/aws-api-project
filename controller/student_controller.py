from typing import Annotated
from fastapi import APIRouter, Body, File, Response, UploadFile, status, HTTPException
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

@student_router.post("/alumnos/{id}/fotoPerfil")
def uploadPicture(id: int, foto: Annotated[UploadFile, File()], response: Response):
    
    try:
        res = studentService.uploadPicture(id, foto)
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "An error has ocurred on the server")
    
    if not response:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = "Student not found")
    
    response.status_code = status.HTTP_200_OK
    response.media_type = "application/json"
    return res
    
@student_router.post("/alumnos/{id}/session/login")
def login(id: int, body: Annotated[dict, Body()], response: Response):
    try:
        sessionString = studentService.login(id, body['password']   )
    except Exception as e:
        print(e)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "An error has ocurred on the server")

    if not sessionString:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail = "Bad request")
    
    response.status_code = status.HTTP_200_OK
    
    return {'sessionString': sessionString}

@student_router.post("/alumnos/{id}/session/verify")
def verify(id: int, body: Annotated[dict, Body()], response: Response):
    try:
        res = studentService.verify(id, body['sessionString'])
    except Exception as e:
        print(e)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "An error has ocurred on the server")
    
    if not res:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail = "Bad request")
    
    response.status_code = status.HTTP_200_OK

    return {'message': 'Sesion valida'}

@student_router.post("/alumnos/{id}/session/logout")
def logout(id: int, body: Annotated[dict, Body()], response: Response):
    try:
        res =studentService.logout(id, body['sessionString'])
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "An error has ocurred on the server")
    
    if not res:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail = "Bad request")
    
    response.status_code = status.HTTP_200_OK

    return {'message': 'Sesion cerrada'}