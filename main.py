import json
from models.school import School
from models.teacher import Teacher 
from models.course import Course
from models.student import Student 

from utils.file_handler import read_file , update_file
from utils.validators import validate_text , validate_age , validate_general_text ,validate_menu_choice
from utils.logging import log_error

#load student 

def load_students(school):
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

            number = int(student.student_id[1:])

            if number >= Student.counter_student_id:
                Student.counter_student_id = number + 1

    except FileNotFoundError:
        print("No student data found. Starting fresh.")
        log_error("students.json not found.")

    except json.JSONDecodeError:
        print("Error: students.json is corrupted.")
        log_error("students.json contains invalid JSON.")

    except KeyError as error:
        print(f"Error: Missing student field: {error}")
        log_error(f"Missing student field: {error}")

    except Exception as error:
        print(f"Error loading students: {error}")
        log_error(f"Unexpected student loading error: {error}")


#load teacher

def load_teachers(school):
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



#load courses
def load_courses(school):
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

#save student 
def save_students(school):
    student_data = []

    for student in school.students.values():
        student_data.append(student.to_dict())

    update_file(
        "data/students.json", student_data)



#save teacher 

def save_teachers(school):
    teacher_data = []

    for teacher in school.teachers.values():
        teacher_data.append(teacher.to_dict())

    update_file(
        "data/teachers.json",teacher_data)

#save course
def save_courses(school):
    course_data = []

    for course in school.courses.values():
        course_data.append(course.to_dict())

    update_file(
        "data/courses.json",
        course_data)

#save all 
def save_all_data(school):
    try:
        save_students(school)
        save_teachers(school)
        save_courses(school)

        print("All data saved successfully.")

    except Exception as error:
        print(f"Error while saving data: {error}")
        log_error(f"Saving error: {error}")

#menu

def display_menu():

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

#main
def main():
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

   

    #load
    load_students(my_school)
    load_teachers(my_school)
    load_courses(my_school)

   

   
    #display
    while True:
        display_menu()
        choice = validate_menu_choice(
            "Choose an option: ",
            1,#min mune
            12#max mune
        )
        #add student
        if choice == 1 :
            name = validate_text("Enter student name: ")

            age = validate_age("Enter student age: ")

            student = Student(name,age)

            message = my_school.add_student(student)

            print(message)

        #add course
        elif choice == 2:

            course_name = validate_general_text("Enter course name: ")

            course = Course(course_name)

            message = my_school.add_course(course)

            print(message)
            print(f"Course Code: {course.course_code}")
        #add teacher
        elif choice == 3:

            name = validate_text( "Enter teacher name: ")
            
            subject = validate_general_text("Enter subject taught: ")
            teacher = Teacher(name, subject)

            message = my_school.add_teacher(teacher)

            print(message)
            print(f"Teacher ID: {teacher.teacher_id}")
        #assign teacher
        elif choice == 4:

            teacher_id = validate_general_text("Enter teacher ID: ").upper()

            course_code = validate_general_text("Enter course code: ").upper()

            message = my_school.assign_teacher_to_course(teacher_id,course_code)

            print(message)
        #enroll
        elif choice == 5:

            student_id = validate_general_text("Enter student ID: ").upper()

            course_code = validate_general_text("Enter course code: " ).upper()

            message = my_school.enroll_student(student_id,course_code )

            print(message)


        #drop
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
        #view student
        elif choice == 7:

            print("\n--- STUDENTS ---")

            my_school.display_students()
        #view courses
        elif choice == 8:

            print("\n--- COURSES ---")

            my_school.display_courses()
        #view teachers
        elif choice == 9:
            print("\n--- TEACHERS ---")
            my_school.display_teachers()

        #view stuednt courses
        elif choice == 10:

            student_id = validate_general_text("Enter student ID: ").upper()
            my_school.display_student_courses(student_id)

        #view course students
        elif choice == 11:

            course_code = validate_general_text("Enter course code: ").upper()
            my_school.display_course_students( course_code )

        #  save and exit
        elif choice == 12:

            print("\nSaving data...")

            save_all_data(my_school)

            print("Thank you for using the School Management System.")
            print("Have a great day!")

            break


if __name__ == "__main__":
    main()
 
