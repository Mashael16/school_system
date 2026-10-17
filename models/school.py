"""
School model.

The School class is the central manager of the system. It stores every
student, teacher, and course, and it keeps both sides of each
relationship in sync (for example, enrolling a student updates the
student's course list AND the course's student list).
"""


class School:
    """Holds all students, teachers, and courses for one school.

    Each collection is a dictionary keyed by ID or course code,
    which gives fast lookups and prevents duplicates.
    """

    def __init__(self,name,address):
        self.name = name
        self.address = address

        self.students = {}   # student_id  -> Student
        self.teachers = {}   # teacher_id  -> Teacher
        self.courses={}      # course_code -> Course

    # -----------------------------------------------------------------------
    # Students
    # -----------------------------------------------------------------------

    def add_student(self, student):
        """Add a student to the school.

        Returns:
            tuple: (True, message) on success,
                   (False, message) if the ID already exists.
        """
        if student.student_id in self.students:
            return False, f"Student ID {student.student_id} already exists."

        self.students[student.student_id] = student
        return True, f"{student.name} added successfully."

    def get_student(self, student_id):
        """Return the student with this ID, or None if not found."""
        return self.students.get(student_id)

    # -----------------------------------------------------------------------
    # Teachers
    # -----------------------------------------------------------------------

    def add_teacher(self, teacher):
        """Add a teacher to the school.

        Returns:
            tuple: (True, message) on success,
                   (False, message) if the ID already exists.
        """
        if teacher.teacher_id in self.teachers:
            return False, f"Teacher ID {teacher.teacher_id} already exists."

        self.teachers[teacher.teacher_id] = teacher
        return True, f"{teacher.name} added successfully."

    def get_teacher(self, teacher_id):
        """Return the teacher with this ID, or None if not found."""
        return self.teachers.get(teacher_id)

    # -----------------------------------------------------------------------
    # Courses
    # -----------------------------------------------------------------------

    def add_course(self, course):
        """Add a course to the school.

        Returns:
            tuple: (True, message) on success,
                   (False, message) if the course code already exists.
        """
        if course.course_code in self.courses:
            return False, f"Course {course.course_code} already exists."

        self.courses[course.course_code] = course
        return True, f"{course.course_name} added successfully."

    def get_course(self, course_code):
        """Return the course with this code, or None if not found."""
        return self.courses.get(course_code)

    # -----------------------------------------------------------------------
    # Enrollment
    # -----------------------------------------------------------------------

    def enroll_student(self, student_id, course_code):
        """Enroll a student in a course.

        Updates both the student's course list and the course's
        student list so the two stay consistent.

        Returns:
            str: a success or error message for the user.
        """
        student = self.get_student(student_id)
        course = self.get_course(course_code)

        if student is None:
            return "Error: Student does not exist."

        if course is None:
            return "Error: Course does not exist."

        if course_code in student.enrolled_course:
            return ( f"Error: {student.name} is already enrolled "
                f"in {course.course_name}.")

        student.enroll_in_course(course_code)
        course.add_student(student_id)

        return (f"Success! {student.name} enrolled in "
            f"{course.course_name}.")

    def drop_student(self, student_id, course_code):
        """Remove a student from a course.

        Updates both the student's course list and the course's
        student list so the two stay consistent.

        Returns:
            str: a success or error message for the user.
        """
        student = self.get_student(student_id)
        course = self.get_course(course_code)

        if student is None:
            return "Error: Student does not exist."

        if course is None:
            return "Error: Course does not exist."

        if course_code not in student.enrolled_course:
            return (
                f"Error: {student.name} is not enrolled "
                f"in {course.course_name}." )
        student.drop_course(course_code)
        course.remove_student(student_id)

        return (
            f"Success! {student.name} dropped "
            f"{course.course_name}.")

            # -----------------------------------------------------------------------
    # Deleting
    # -----------------------------------------------------------------------

    def delete_student(self, student_id):
        """Delete a student and remove them from every course they joined."""
        student = self.get_student(student_id)
        if student is None:
            return False, "Error: Student does not exist."

        for course_code in student.enrolled_course:
            course = self.get_course(course_code)
            if course:
                course.remove_student(student_id)

        del self.students[student_id]
        return True, f"{student.name} was deleted."

    def delete_teacher(self, teacher_id):
        """Delete a teacher and leave their courses without a teacher."""
        teacher = self.get_teacher(teacher_id)
        if teacher is None:
            return False, "Error: Teacher does not exist."

        for course in self.courses.values():
            if course.assigned_teacher == teacher_id:
                course.assigned_teacher = None

        del self.teachers[teacher_id]
        return True, f"{teacher.name} was deleted."

    def delete_course(self, course_code):
        """Delete a course and remove it from its students and teacher."""
        course = self.get_course(course_code)
        if course is None:
            return False, "Error: Course does not exist."

        for student_id in course.enrolled_student_ids:
            student = self.get_student(student_id)
            if student:
                student.drop_course(course_code)

        teacher = self.get_teacher(course.assigned_teacher)
        if teacher:
            teacher.remove_course(course_code)

        del self.courses[course_code]
        return True, f"{course.course_name} was deleted."

    # -----------------------------------------------------------------------
    # Teacher assignment
    # -----------------------------------------------------------------------

    def assign_teacher_to_course(self, teacher_id, course_code):
        """Assign a teacher to a course.

        Updates both the course's assigned teacher and the teacher's
        course list.

        Returns:
            str: a success or error message for the user.
        """
        teacher = self.get_teacher(teacher_id)
        course = self.get_course(course_code)

        if teacher is None:
            return "Error: Teacher does not exist."

        if course is None:
            return "Error: Course does not exist."

        if course.assigned_teacher == teacher_id:
            return "This teacher is already assigned to this course."

        # If another teacher had this course, remove it from their list
        # so only the new teacher shows it.
        old_teacher = self.get_teacher(course.assigned_teacher)
        if old_teacher:
            old_teacher.remove_course(course_code)

        course.assign_teacher(teacher_id)
        teacher.assignCourse(course_code)

        return (f"Success! {teacher.name} assigned to "
        f"{course.course_name}.")



    # -----------------------------------------------------------------------
    # Display
    # -----------------------------------------------------------------------

    def display_students(self):
        """Print every student, or a notice if there are none."""
        if not self.students:
            print("No students found.")
            return

        for student in self.students.values():
            print(student)

    def get_students(self):
        """Return all students as a list (for the web interface)."""
        return list(self.students.values())

    def display_teachers(self):
        """Print every teacher, or a notice if there are none."""
        if not self.teachers:
            print("No teachers found.")
            return

        for teacher in self.teachers.values():
            print(teacher)

    def get_teachers(self):
        """Return all teachers as a list (for the web interface)."""
        return list(self.teachers.values())

    def display_courses(self):
            """Print every course, or a notice if there are none."""
            if not self.courses:
                print("No courses found.")
                return
    
            for course in self.courses.values():
                print(course)

    def get_courses(self):
        """Return all courses as a list (for the web interface)."""
        return list(self.courses.values())
            
    def display_student_courses(self, student_id):
        """Print the courses one student is enrolled in."""
        student = self.get_student(student_id)
        if student is None:
            print("Error: Student does not exist.")
            return

        if not student.enrolled_course:
            print(f"{student.name} is not enrolled in any courses.")
            return

        print(f"\nCourses for {student.name}:")
        for course_code in student.enrolled_course:
            course = self.get_course(course_code)
            # Skip codes that point to a course that no longer exists.
            if course:
                print(f"{course.course_code} | {course.course_name}")
        
    def display_course_students(self, course_code):
        """Print the students enrolled in one course."""
        course = self.get_course(course_code)

        if course is None:
            print("Error: Course does not exist.")
            return
        
        if not course.enrolled_student_ids:
            print("No students are enrolled in this course.")
            return

        print(f"\nStudents enrolled in {course.course_name}:")

        for student_id in course.enrolled_student_ids:
            student = self.get_student(student_id)

            # Skip IDs that point to a student that no longer exists.
            if student:
                print(
                    f"{student.student_id} | "
                    f"{student.name}"
                )