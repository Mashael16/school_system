class Course():
    counter_code_course = 300
    def __init__(self , course_name ):
        self.course_name =course_name
        self.course_code = f"{self.course_name[0:3].upper().strip()} {Course.counter_code_course}"
        Course.counter_code_course +=1
        self.assigned_to_teacher = []
        self.enrolled_student_by_id = []

    def add_student(self,studentId):
        self.enrolled_student_by_id.append(studentId)

    def remove_student(self,studentId):
        self.enrolled_student_by_id.remove(studentId)

    def display_information_course(self):
        return f"""Display name Courses : {self.course_name} | course code {self.course_code}
{self.assigned_to_teacher} | {self.enrolled_student_by_id}"""
    

