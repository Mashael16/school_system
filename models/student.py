class Students:

    counter_student_id= 100
    
    def __init__(self ,  name , age ):
        self.student_id = f"S{str(Students.counter_student_id)}"
        Students.counter_student_id +=1
        self.name=name
        self.age = age
        self.enrolled_course=[]

    def add_course(self,course):

        return f""" Success! You are now enrolled in
          {self.enrolled_course.append(course)}
        """


    def drop_course(self,course):
        return f"""Course successfully deleted.
          {self.enrolled_course.remove(course)}
        """


    def get_course(self):
        return f"""Success! Here are your courses:
        { self.enrolled_course}
        """
        
    
    def get_inforamtion_student(self):
        return f"""{self.student_id} | {self.name} | {self.age} |
courses: {self.enrolled_course}
        """

    # def enrolled_course(self):
    #     self.enrolled_course=self.enrolled_course
student = Students("mashael",23)


student.add_course("python")
student.add_course("java")

print(student.get_course())
print(student.get_inforamtion_student())

student2 = Students("omar",23)
student2.add_course("java")
print(student2.get_inforamtion_student())
