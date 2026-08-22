class School:
    counter_school_id = 400

    def __init__(self,name,address):
        self.schoolId = f"sch{School.counter_school_id}"
        School.counter_school_id +=1
        self.name = name
        self.address = address
        self.allstudents = []
        self.allteachers = []
        self.allcourses=[]

    def addstudent(self,student):
        self.allstudents.append(student)
        return f"""{student.name} added successfully."""


    def addTeacher(self,teacher):
        self.allteachers.append(teacher)
        return f"""{teacher.name} added successfully."""


    def addCourse(self,course):
        self.allcourses.append(course)
        return f"""{course.name} added successfully."""

    def get_information(self):
        return f""" Displaying all registered students, teachers, and courses: \nstudents:{self.allstudents}
                \nteachers:{self.allteachers}\ncourses:{self.allcourses} """
    

