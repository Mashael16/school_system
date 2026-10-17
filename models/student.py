"""
Student model.

Represents one student and the list of course codes they are enrolled in.
"""


class Student:
    """A student with an auto-generated ID (S100, S101, ...).

    Class attributes:
        counter_student_id (int): the number used for the next new ID.
            Shared by all Student objects so IDs are never repeated.
    """

    counter_student_id= 100
    
    def __init__(self ,  name , age , student_id = None):
        """Create a student.

        Args:
            name (str): the student's name.
            age (int): the student's age.
            student_id (str, optional): an existing ID when loading from
                file. If not given, a new ID is generated.
        """
        if student_id is None:
            self.student_id = f"S{str(Student.counter_student_id)}"
            Student.counter_student_id +=1
        else:
            self.student_id = student_id
        
        self.name=name
        self.age = age
        self.enrolled_course=[]   # list of course codes, e.g. ["MAT300"]

    def enroll_in_course(self,course_code):
        """Add a course code to this student's list, if not already there."""
        if course_code in self.enrolled_course:
            return f"{self.name} is already enrolled in {course_code}."
        
        self.enrolled_course.append(course_code)
        return f""" Success!{self.name} You are now enrolled in
          {course_code}
        """

    def drop_course(self, course_code):
        """Remove a course code from this student's list, if present."""
        if course_code not in self.enrolled_course:
            return f"{self.name} is not enrolled in {course_code}."
        self.enrolled_course.remove(course_code)
        return f"Course successfully deleted. {course_code}"

    def get_course(self):
        """Return a message listing this student's course codes."""
        return f"""Success! Here are your courses:
        { self.enrolled_course}
        """
    
    def to_dict(self):
        """Convert the student to a dictionary for saving to JSON."""
        return {
            "student_id":self.student_id,
            "student_name":self.name,
            "student_age":self.age,
            "enrolled_course":self.enrolled_course
            }

    def __str__(self):
        """Readable one-student summary used by print()."""
        return f"""{self.student_id} | {self.name} | {self.age} |
courses: {self.enrolled_course}
        """