"""
School Management System - entry point.

Runs a menu-driven console application for managing students, teachers,
and courses. Data is loaded from JSON files in the data/ folder at startup
and written back when the user chooses "Save and Exit".
"""

import json
from models.school import School
from models.teacher import Teacher 
from models.course import Course
from models.student import Student 

from utils.file_handler import read_file , update_file
from utils.validators import validate_text , validate_age , validate_general_text ,validate_menu_choice
from utils.logging import log_error


# ---------------------------------------------------------------------------
# Loading data
# ---------------------------------------------------------------------------

def load_students(school):
    """Load saved students from data/students.json into the school.

    Also advances Student.counter_student_id past the highest saved ID,
    so new students never reuse an existing ID.
    """
    try:
        loaded_students = read_file("data/students.json")

        for student_data in loaded_students:
            student = Student(
                name=student_data["student_name"],
                age=student_data["student_age"],
                student_id=student_data["student_id"]
            )

            student.enrolled_course = student_data.get(
                "enrolled_course",
                []
            )

            school.add_student(student)

            # IDs look like "S105": skip the prefix letter and keep the number.
            number = int(student.student_id[1:])

            if number >= Student.counter_student_id:
                Student.counter_student_id = number + 1

    except FileNotFoundError:
        # First run: no saved file yet, which is not an error for the user.
        print("No student data found. Starting fresh.")
        log_error("students.json not found.")

    except json.JSONDecodeError:
        print("Error: students.json is corrupted.")
        log_error("students.json contains invalid JSON.")

    except KeyError as error:
        print(f"Error: Missing student field: {error}")
        log_error(f"Missing student field: {error}")

    except Exception as error:
        # Safety net so a bad file never crashes the program at startup.
        print(f"Error loading students: {error}")
        log_error(f"Unexpected student loading error: {error}")


def load_teachers(school):
    """Load saved teachers from data/teachers.json into the school.

    Also advances Teacher.counter_teacher_id past the highest saved ID.
    """
    try:
        loaded_teachers = read_file("data/teachers.json")

        for teacher_data in loaded_teachers:
            teacher = Teacher(
                name=teacher_data["name"],
                subject=teacher_data.get("subject", "Not specified"),
                teacher_id=teacher_data["teacher_id"]
            )

            teacher.assigned_courses = teacher_data.get(
                "assigned_courses", []
            )

            school.add_teacher(teacher)

            # IDs look like "T203": skip the prefix letter and keep the number.
            number = int(teacher.teacher_id[1:])

            if number >= Teacher.counter_teacher_id:
                Teacher.counter_teacher_id = number + 1

    except FileNotFoundError:
        print("No teacher data found. Starting fresh.")
        log_error("teachers.json not found.")

    except json.JSONDecodeError:
        print("Error: teachers.json is corrupted.")
        log_error("teachers.json contains invalid JSON.")

    except KeyError as error:
        print(f"Error: Missing teacher field: {error}")
        log_error(f"Missing teacher field: {error}")

    except Exception as error:
        print(f"Error loading teachers: {error}")
        log_error(f"Unexpected teacher loading error: {error}")


def load_courses(school):
    """Load saved courses from data/courses.json into the school.

    Also advances Course.counter_course_code past the highest saved
    code number, so newly generated codes stay unique.
    """
    try:
        loaded_courses = read_file("data/courses.json")
        for course_data in loaded_courses:
            course = Course(
            course_name=course_data["course_name"],
            course_code=course_data["course_code"])

            course.assigned_teacher = course_data.get(
                "assigned_teacher" )

            course.enrolled_student_ids = course_data.get(
                "enrolled_student_ids",
                []
            )

            school.add_course(course)

            # Course codes have a variable-length prefix (e.g. "MAT301"),
            # so read the trailing digits from the end instead of slicing.
            code = course.course_code

            digits = ""

            for character in reversed(code):
                if character.isdigit():
                    digits = character + digits
                else:
                    break

            if digits:
                number = int(digits)

                if number >= Course.counter_course_code:
                    Course.counter_course_code = number + 1

    except FileNotFoundError:
        print("No course data found. Starting fresh.")
        log_error("courses.json not found.")

    except json.JSONDecodeError:
        print("Error: courses.json is corrupted.")
        log_error("courses.json contains invalid JSON.")

    except KeyError as error:
        print(f"Error: Missing course field: {error}")
        log_error(f"Missing course field: {error}")

    except Exception as error:
        print(f"Error loading courses: {error}")
        log_error(f"Unexpected course loading error: {error}")


# ---------------------------------------------------------------------------
# Saving data
# ---------------------------------------------------------------------------

def save_students(school):
    """Write all students to data/students.json, replacing its contents."""
    student_data = []

    for student in school.students.values():
        student_data.append(student.to_dict())

    update_file(
        "data/students.json", student_data)


def save_teachers(school):
    """Write all teachers to data/teachers.json, replacing its contents."""
    teacher_data = []

    for teacher in school.teachers.values():
        teacher_data.append(teacher.to_dict())

    update_file(
        "data/teachers.json",teacher_data)


def save_courses(school):
    """Write all courses to data/courses.json, replacing its contents."""
    course_data = []

    for course in school.courses.values():
        course_data.append(course.to_dict())

    update_file(
        "data/courses.json",
        course_data)


def save_all_data(school):
    """Save students, teachers, and courses, reporting any failure."""
    try:
        save_students(school)
        save_teachers(school)
        save_courses(school)

        print("All data saved successfully.")

    except Exception as error:
        print(f"Error while saving data: {error}")
        log_error(f"Saving error: {error}")


# ---------------------------------------------------------------------------
# User interface
# ---------------------------------------------------------------------------

def display_menu():
    """Print the main menu options."""

    print("\n" + "=" * 50)
    print("        SCHOOL MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add student")
    print("2. Add course")
    print("3. Add teacher")
    print("4. Assign teacher to course")
    print("5. Enroll student")
    print("6. Drop student from course")
    print("7. View students")
    print("8. View courses")
    print("9. View teachers")
    print("10. View student courses")
    print("11. View course students")
    print("12. Save and Exit")

    print("=" * 50)


def main():
    """Set up the school, load saved data, and run the menu loop."""
    print("\nSystem Setup")
    print("-" * 30)

    school_name = validate_general_text(
        "Please enter the name of the school: "
    )

    school_address = validate_general_text(
        "Please enter the school's address: "
    )

    my_school = School(
        school_name,
        school_address
    )

    print(
        f"\nWelcome to {my_school.name} "
        f"Management System!"
    )

    # Restore data from the previous session before showing the menu.
    load_students(my_school)
    load_teachers(my_school)
    load_courses(my_school)

    # Main loop: runs until the user chooses "Save and Exit".
    while True:
        display_menu()
        choice = validate_menu_choice(
            "Choose an option: ",
            1,   # first menu option
            12   # last menu option
        )

        # IDs and course codes are upper-cased below so that user input
        # like "s101" still matches the stored "S101".

        # 1. Add student
        if choice == 1 :
            name = validate_text("Enter student name: ")

            age = validate_age("Enter student age: ")

            student = Student(name,age)
            
            success, message = my_school.add_student(student)

            print(message)
            if success:
                print(f"Student ID: {student.student_id}")

        # 2. Add course
        elif choice == 2:

            course_name = validate_general_text("Enter course name: ")

            course = Course(course_name)

            success, message = my_school.add_course(course)

            print(message)
            if success:
                print(f"Course Code: {course.course_code}")

        # 3. Add teacher
        elif choice == 3:

            name = validate_text( "Enter teacher name: ")
            
            subject = validate_general_text("Enter subject taught: ")
            
            teacher = Teacher(name, subject)

            success, message = my_school.add_teacher(teacher)

            print(message)
            if success:
                print(f"Teacher ID: {teacher.teacher_id}")

        # 4. Assign teacher to course
        elif choice == 4:

            teacher_id = validate_general_text("Enter teacher ID: ").upper()

            course_code = validate_general_text("Enter course code: ").upper()

            message = my_school.assign_teacher_to_course(teacher_id,course_code)

            print(message)

        # 5. Enroll student in course
        elif choice == 5:

            student_id = validate_general_text("Enter student ID: ").upper()

            course_code = validate_general_text("Enter course code: " ).upper()

            message = my_school.enroll_student(student_id,course_code )

            print(message)

        # 6. Drop student from course
        elif choice == 6:

            student_id = validate_general_text(
                "Enter student ID: "
            ).upper()

            course_code = validate_general_text(
                "Enter course code: "
            ).upper()

            message = my_school.drop_student(
                student_id,
                course_code
            )

            print(message)

        # 7. View all students
        elif choice == 7:

            print("\n--- STUDENTS ---")

            my_school.display_students()

        # 8. View all courses
        elif choice == 8:

            print("\n--- COURSES ---")

            my_school.display_courses()

        # 9. View all teachers
        elif choice == 9:
            print("\n--- TEACHERS ---")
            my_school.display_teachers()

        # 10. View courses of one student
        elif choice == 10:

            student_id = validate_general_text("Enter student ID: ").upper()
            my_school.display_student_courses(student_id)

        # 11. View students of one course
        elif choice == 11:

            course_code = validate_general_text("Enter course code: ").upper()
            my_school.display_course_students( course_code )

        # 12. Save and exit
        elif choice == 12:

            print("\nSaving data...")

            save_all_data(my_school)

            print("Thank you for using the School Management System.")
            print("Have a great day!")

            break


if __name__ == "__main__":
    main()