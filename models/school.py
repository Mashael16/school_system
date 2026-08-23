class School:

    def __init__(self,name,address):
        self.name = name
        self.address = address

        self.students = {}
        self.teachers = {}
        self.courses={}
#student
    def add_student(self, student):
        if student.student_id in self.students:
            return False, f"Student ID {student.student_id} already exists."

        self.students[student.student_id] = student
        return True, f"{student.name} added successfully."

    def get_student(self, student_id):
        return self.students.get(student_id)

#teacher
    def add_teacher(self, teacher):
        if teacher.teacher_id in self.teachers:
            return False, f"Teacher ID {teacher.teacher_id} already exists."

        self.teachers[teacher.teacher_id] = teacher
        return True, f"{teacher.name} added successfully."

    def get_teacher(self, teacher_id):
        return self.teachers.get(teacher_id)

#courses
    def add_course(self, course):
        if course.course_code in self.courses:
            return False, f"Course {course.course_code} already exists."

        self.courses[course.course_code] = course
        return True, f"{course.course_name} added successfully."

    def get_course(self, course_code):
        return self.courses.get(course_code)


#enrolled
    def enroll_student(self, student_id, course_code):
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


#drop
    def drop_student(self, student_id, course_code):
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



 #teacher assignment
    def assign_teacher_to_course(self, teacher_id, course_code):
        teacher = self.get_teacher(teacher_id)
        course = self.get_course(course_code)

        if teacher is None:
            return "Error: Teacher does not exist."

        if course is None:
            return "Error: Course does not exist."

        if course.assigned_teacher == teacher_id:
            return "This teacher is already assigned to this course."
        
        course.assign_teacher(teacher_id)
        teacher.assignCourse(course_code)
        return (f"Success! {teacher.name} assigned to "
            f"{course.course_name}." )
#dispaly
    def display_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students.values():
            print(student)

    def display_teachers(self):
        if not self.teachers:
            print("No teachers found.")
            return

        for teacher in self.teachers.values():
            print(teacher)

    def display_courses(self):
            if not self.courses:
                print("No courses found.")
                return
    
            for course in self.courses.values():
                print(course)
            
    def display_student_courses(self, student_id):
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
            if course:
                print(f"{course.course_code} | {course.course_name}")
        
    def display_course_students(self, course_code):
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

            if student:
                print(
                    f"{student.student_id} | "
                    f"{student.name}"
                )


