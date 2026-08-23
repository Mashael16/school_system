class Student:

    counter_student_id= 100
    
    def __init__(self ,  name , age , student_id = None):
        if student_id is None:
            self.student_id = f"S{str(Student.counter_student_id)}"
            Student.counter_student_id +=1
        else:
            self.student_id = student_id
        
        self.name=name
        self.age = age
        self.enrolled_course=[]

    def enroll_in_course(self,course_code):
        if course_code in self.enrolled_course:
            return f"{self.name} is already enrolled in {course_code}."
        
        self.enrolled_course.append(course_code)
        return f""" Success!{self.name} You are now enrolled in
          {course_code}
        """


    def drop_course(self, course_code):
        if course_code not in self.enrolled_course:
            return f"{self.name} is not enrolled in {course_code}."
        self.enrolled_course.remove(course_code)
        return f"Course successfully deleted. {course_code}"

    def get_course(self):
        return f"""Success! Here are your courses:
        { self.enrolled_course}
        """
    
    def to_dict(self):
        return {
            "student_id":self.student_id,
            "student_name":self.name,
            "student_age":self.age,
            "enrolled_course":self.enrolled_course
            }

                 
    
    def __str__(self):
        return f"""{self.student_id} | {self.name} | {self.age} |
courses: {self.enrolled_course}
        """

