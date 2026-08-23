class Course():
    counter_course_code = 300   

    def __init__(self, course_name, course_code=None):
        self.course_name = course_name
        if course_code is None:
            prefix = course_name[:3].upper()
            self.course_code = f"{prefix}{Course.counter_course_code}"
            Course.counter_course_code += 1
        else:
            self.course_code = course_code
        self.assigned_teacher = None
        self.enrolled_student_ids = []

    def add_student(self, student_id):
        if student_id in self.enrolled_student_ids:
            return f"Student {student_id} is already enrolled."

        self.enrolled_student_ids.append(student_id)
        return f"Student {student_id} added successfully."
        

    def remove_student(self, student_id):
        if student_id not in self.enrolled_student_ids:
            return f"Student {student_id} is not enrolled."

        self.enrolled_student_ids.remove(student_id)
        return f"Student {student_id} removed successfully."
    
    def assign_teacher(self, teacher_id):
        self.assigned_teacher = teacher_id
        return f"Teacher {teacher_id} assigned to {self.course_name}."
    
    def to_dict(self):
        return {
            "course_name":self.course_name,
            "course_code": self.course_code,
            "assigned_teacher": self.assigned_teacher,
            "enrolled_student_ids":self.enrolled_student_ids
        }

    def __str__(self):
        teacher = self.assigned_teacher if self.assigned_teacher else "None"

        students = (
            ", ".join(self.enrolled_student_ids)
            if self.enrolled_student_ids
            else "None"
        )
        return (
            f"{self.course_code} | {self.course_name} | "
            f"Teacher: {teacher} | Students: {students}"
        )

