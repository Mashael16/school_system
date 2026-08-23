class Teacher:
    counter_teacher_id = 200   

    def __init__(self, name, subject, teacher_id = None):
        if teacher_id is None:
            self.teacher_id = f"T{Teacher.counter_teacher_id}"
            Teacher.counter_teacher_id += 1
        else:
            self.teacher_id = teacher_id
        self.name = name
        self.subject = subject
        self.assigned_courses = []

    def assignCourse(self ,course_code ):
        if course_code in self.assigned_courses:
            return f"{self.name} is already assigned to {course_code}."
        
        self.assigned_courses.append(course_code)
        return f"{course_code} assigned to {self.name}."

    def remove_course(self, course_code):
        if course_code not in self.assigned_courses:
            return f"{self.name} is not assigned to {course_code}."

        self.assigned_courses.remove(course_code)
        return f"{course_code} removed from {self.name}."


    def to_dict(self):
        return {
            "teacher_id": self.teacher_id,
            "name": self.name,
            "subject": self.subject,
            "assigned_courses": self.assigned_courses
        }

    def __str__(self):
        return f"{self.teacher_id} | {self.name} | Subject: {self.subject} \n courses: {self.assigned_courses}"
