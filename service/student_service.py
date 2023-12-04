from fastapi import UploadFile
from config.database import MySQLCon
from model.student_model import Student
from schemas.student_schema import StudentSchema
from config.connection import sns_client, s3_client
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class StudentService:

    def get_all_students(self):
        session = MySQLCon()
        students = session.query(StudentSchema).all()
        session.close()
        return students
    
    def save_student(self, student: Student):

        session = MySQLCon()            
        
        new_student = StudentSchema(
            nombres = student.nombres, 
            apellidos = student.apellidos, 
            matricula = student.matricula,
            fotoPerfilUrl = '',
            promedio = student.promedio, 
            password = student.password
        )

        session.add(new_student)
        session.commit()
        session.refresh(new_student)
        session.close()

        student_dict_clean = {key: value for key, value in new_student.__dict__.items() if not key.startswith('_')}
        return student_dict_clean

    def get_student_by_id(self, id: int):
        session = MySQLCon()
        student = session.query(StudentSchema).filter(StudentSchema.id == id).first()
        session.close()

        if not student:
            return None

        student_dict_clean = {key: value for key, value in student.__dict__.items() if not key.startswith('_')}
        
        return student_dict_clean
    
    def update_student(self, id: int, studentUpdated: Student):

        isStudent = self.get_student_by_id(id)

        if not isStudent:
            return None
        
        session = MySQLCon()
        rows_affected = session.query(StudentSchema).filter(StudentSchema.id == id).update(dict(studentUpdated))
        session.commit()
        session.close()

        if rows_affected > 0:
            return self.get_student_by_id(id)
        
        return None
    
    def delete_student(self, id: int):

        isStudent = self.get_student_by_id(id)

        if not isStudent:
            return None
        
        session = MySQLCon()
        session.query(StudentSchema).filter(StudentSchema.id == id).delete()
        session.commit()
        session.close()
        return True
    
    def send_email(self, id: int):
        student = self.get_student_by_id(id)

        if not student:
            return None
        
        message = f"El promedio del alumno {student['nombres']} {student['apellidos']} es {student['promedio']}."
        
        response = sns_client.publish(
            TopicArn = "arn:aws:sns:us-east-1:581050077128:calificaciones",
            Message = message,
            Subject = "Calificación"
        )

        return True
    
    def uploadPicture(self, id: int, foto: UploadFile):
        student = self.get_student_by_id(id)

        if not student:
            return None

        s3_client.upload_fileobj(foto.file, getenv('AWS_BUCKET'), foto.filename, ExtraArgs = {'ACL': 'public-read', 'ContentType': 'multipart/form-data'})
        
        fotoPerfilUrl = f"https://andreiapibucket.s3.amazonaws.com/{foto.filename}"
        
        student['fotoPerfilUrl'] = fotoPerfilUrl
        response = self.update_student(id, student)
        
        return response

    def login(self, id: int, password: str):
        student = self.get_student_by_id(id)

        if not student or student['password'] !== password:
            return None
        
        

    def verify(self, id: int, sessionString: str):

    def logout(self, id: int, sessionString: str):