class Teacher:
    counter_Teacher_id = 200

    def __init__(self, name ):
        self.teacherId = f"T{str(Teacher.counter_Teacher_id)}"
        Teacher.counter_Teacher_id += 1
        self.name = name
        self.subject_taught = []

    def assignCourse(self ,assignToteacher ):
        self.subject_taught.append(assignToteacher)
        return f"""Your Assigned Courses: {self.subject_taught} """

    def get_information_teacher(self):
        return f"""{self.teacherId} | {self.name} \n courses: {self.subject_taught} """


teacher = Teacher("ali")
print(teacher.get_information_teacher())