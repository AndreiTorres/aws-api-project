from model.student_model import Student

class StudentService:

    STUDENTS_DATA = []

    def get_all_students(self):
        return self.STUDENTS_DATA
    
    def save_student(self, student: Student):
        self.STUDENTS_DATA.append(student)

    def get_student_by_id(self, id: int):
        for student in self.STUDENTS_DATA:
            if student.id == id:
                return student
        return None
    
    def update_student(self, id: int, studentUpdated: Student):
        for index, student in enumerate(self.STUDENTS_DATA):
            if student.id == id:
                self.STUDENTS_DATA[index] = studentUpdated
                return studentUpdated
        return None
    
    def delete_student(self, id: int):
        for student in self.STUDENTS_DATA:
            if student.id == id:
                self.STUDENTS_DATA.remove(student)
                return True
        return None