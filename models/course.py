"""
Course model.

Represents one course, its assigned teacher, and its enrolled students.
"""


class Course():
    """A course with an auto-generated code (e.g. MAT300, PHY301).

    Class attributes:
        counter_course_code (int): the number used for the next new code.
            Shared by all Course objects so codes are never repeated.
    """

    counter_course_code = 300   

    def __init__(self, course_name, course_code=None):
        """Create a course.

        Args:
            course_name (str): the course name.
            course_code (str, optional): an existing code when loading
                from file. If not given, a new code is generated from the
                first three letters of the name plus the counter.
        """
        self.course_name = course_name
        if course_code is None:
            prefix = course_name[:3].upper()
            self.course_code = f"{prefix}{Course.counter_course_code}"
            Course.counter_course_code += 1
        else:
            self.course_code = course_code
        self.assigned_teacher = None       # teacher ID, or None if unassigned
        self.enrolled_student_ids = []     # list of student IDs

    def add_student(self, student_id):
        """Add a student ID to this course, if not already enrolled."""
        if student_id in self.enrolled_student_ids:
            return f"Student {student_id} is already enrolled."

        self.enrolled_student_ids.append(student_id)
        return f"Student {student_id} added successfully."

    def remove_student(self, student_id):
        """Remove a student ID from this course, if enrolled."""
        if student_id not in self.enrolled_student_ids:
            return f"Student {student_id} is not enrolled."

        self.enrolled_student_ids.remove(student_id)
        return f"Student {student_id} removed successfully."
    
    def assign_teacher(self, teacher_id):
        """Set the teacher for this course, replacing any previous one."""
        self.assigned_teacher = teacher_id
        return f"Teacher {teacher_id} assigned to {self.course_name}."
    
    def to_dict(self):
        """Convert the course to a dictionary for saving to JSON."""
        return {
            "course_name":self.course_name,
            "course_code": self.course_code,
            "assigned_teacher": self.assigned_teacher,
            "enrolled_student_ids":self.enrolled_student_ids
        }

    def __str__(self):
        """Readable one-course summary used by print()."""
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