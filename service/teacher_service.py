from model.teacher_model import Teacher


class TeacherService:

    TEACHER_DATA = []

    def get_all_teachers(self):
        return self.TEACHER_DATA
    
    def save_teacher(self, teacher: Teacher):
        self.TEACHER_DATA.append(teacher)

    def get_teacher_by_id(self, id: int):
        for teacher in self.TEACHER_DATA:
            if teacher.id == id:
                return teacher
        return None
    
    def update_teacher(self, id: int, teacherUpdated: Teacher):
        for index, teacher in enumerate(self.TEACHER_DATA):
            if teacher.id == id:
                self.TEACHER_DATA[index] = teacherUpdated
                return teacherUpdated
        return None
    
    def delete_teacher(self, id: int):
        for teacher in self.TEACHER_DATA:
            if teacher.id == id:
                self.TEACHER_DATA.remove(teacher)
                return True
        return None