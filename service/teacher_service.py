from config.database import MySQLCon
from model.teacher_model import Teacher
from schemas.teacher_schema import TeacherSchema


class TeacherService:

    def get_all_teachers(self):
        session = MySQLCon()
        teachers = session.query(TeacherSchema).all()
        session.close()
        
        return teachers
    
    def save_teacher(self, teacher: Teacher):
        session = MySQLCon()

        new_teacher = TeacherSchema(
            numeroEmpleado = teacher.numeroEmpleado,
            nombres = teacher.nombres,
            apellidos = teacher.apellidos,
            horasClase = teacher.horasClase
        )

        session.add(new_teacher)
        session.commit()
        session.refresh(new_teacher)
        session.close()

        new_teacher_clean = {key: value for key, value in new_teacher.__dict__.items() if not key.startswith('_')}
        return new_teacher_clean

    def get_teacher_by_id(self, id: int):

        session = MySQLCon()

        teacher = session.query(TeacherSchema).filter(TeacherSchema.id == id).first()
        session.close()
        
        if not teacher:
            return None

        teacher_clean = {key: value for key, value in teacher.__dict__.items() if not key.startswith('_')}
        
        return teacher_clean

    
    def update_teacher(self, id: int, teacherUpdated: Teacher):
        isTeacher = self.get_teacher_by_id(id)

        if not isTeacher:
            return None
        
        session = MySQLCon()
        rows_affected = session.query(TeacherSchema).filter(TeacherSchema.id == id).update(dict(teacherUpdated))
        session.commit()
        session.close()

        if rows_affected > 0:
            return self.get_teacher_by_id(id)
        
        return None
    
    def delete_teacher(self, id: int):
        isTeacher = self.get_teacher_by_id(id)

        if not isTeacher:
            return None
        
        session = MySQLCon()
        session.query(TeacherSchema).filter(TeacherSchema.id == id).delete()
        session.commit()
        session.close()
        return True