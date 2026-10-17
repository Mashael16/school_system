"""
Teacher model.

Represents one teacher, the subject they teach, and their assigned courses.
"""


class Teacher:
    """A teacher with an auto-generated ID (T200, T201, ...).

    Class attributes:
        counter_teacher_id (int): the number used for the next new ID.
            Shared by all Teacher objects so IDs are never repeated.
    """

    counter_teacher_id = 200   

    def __init__(self, name, subject, teacher_id = None):
        """Create a teacher.

        Args:
            name (str): the teacher's name.
            subject (str): the subject they teach.
            teacher_id (str, optional): an existing ID when loading from
                file. If not given, a new ID is generated.
        """
        if teacher_id is None:
            self.teacher_id = f"T{Teacher.counter_teacher_id}"
            Teacher.counter_teacher_id += 1
        else:
            self.teacher_id = teacher_id
        self.name = name
        self.subject = subject
        self.assigned_courses = []   # list of course codes

    def assignCourse(self ,course_code ):
        """Add a course code to this teacher's list, if not already there."""
        if course_code in self.assigned_courses:
            return f"{self.name} is already assigned to {course_code}."
        
        self.assigned_courses.append(course_code)
        return f"{course_code} assigned to {self.name}."

    def remove_course(self, course_code):
        """Remove a course code from this teacher's list, if present."""
        if course_code not in self.assigned_courses:
            return f"{self.name} is not assigned to {course_code}."

        self.assigned_courses.remove(course_code)
        return f"{course_code} removed from {self.name}."

    def to_dict(self):
        """Convert the teacher to a dictionary for saving to JSON."""
        return {
            "teacher_id": self.teacher_id,
            "name": self.name,
            "subject": self.subject,
            "assigned_courses": self.assigned_courses
        }

    def __str__(self):
        """Readable one-teacher summary used by print()."""
        return f"{self.teacher_id} | {self.name} | Subject: {self.subject} \n courses: {self.assigned_courses}"