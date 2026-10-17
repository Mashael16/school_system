from django.shortcuts import render

from django.contrib import messages
from django.shortcuts import render, redirect

from models.student import Student
from .school_service import school, save_all_data

from models.teacher import Teacher
from models.course import Course

from django.views.decorators.http import require_POST

def student_list(request):
    """Show all students, and add a new one when the form is submitted."""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        age = request.POST.get("age", "").strip()

        # Same rules as the console validators, checked on the server.
        if not name.replace(" ", "").isalpha():
            messages.error(request, "Name must contain letters only.")
        elif not age.isdigit() or not 5 <= int(age) <= 100:
            messages.error(request, "Age must be a number between 5 and 100.")
        else:
            student = Student(name.title(), int(age))
            success, message = school.add_student(student)

            if success:
                save_all_data(school)   # no "Save and Exit" on a website
                messages.success(request, f"{message} ID: {student.student_id}")
            else:
                messages.error(request, message)

        # Redirect so refreshing the page doesn't submit the form twice.
        return redirect("student_list")

    return render(request, "portal/students.html", {
        "students": school.get_students(),
    })


def teacher_list(request):
    """Show all teachers, and add a new one when the form is submitted."""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        subject = request.POST.get("subject", "").strip()

        if not name.replace(" ", "").isalpha():
            messages.error(request, "Name must contain letters only.")
        elif not subject:
            messages.error(request, "Subject cannot be blank.")
        else:
            teacher = Teacher(name.title(), subject)
            success, message = school.add_teacher(teacher)

            if success:
                save_all_data(school)
                messages.success(request, f"{message} ID: {teacher.teacher_id}")
            else:
                messages.error(request, message)

        return redirect("teacher_list")

    return render(request, "portal/teachers.html", {
        "teachers": school.get_teachers(),
    })


def course_list(request):
    """Show all courses; add a course or assign a teacher from the forms."""
    if request.method == "POST":
        # A hidden "action" field tells us which of the two forms was sent.
        action = request.POST.get("action")

        if action == "add_course":
            course_name = request.POST.get("course_name", "").strip()

            if not course_name:
                messages.error(request, "Course name cannot be blank.")
            else:
                course = Course(course_name)
                success, message = school.add_course(course)

                if success:
                    save_all_data(school)
                    messages.success(request, f"{message} Code: {course.course_code}")
                else:
                    messages.error(request, message)

        elif action == "assign_teacher":
            teacher_id = request.POST.get("teacher_id", "")
            course_code = request.POST.get("course_code", "")

            message = school.assign_teacher_to_course(teacher_id, course_code)

            # This method returns a plain string, so check how it starts.
            if message.startswith("Success"):
                save_all_data(school)
                messages.success(request, message)
            else:
                messages.error(request, message)

        return redirect("course_list")

    # Pair each course with its teacher object so the page can show the name.
    rows = [
        {"course": course, "teacher": school.get_teacher(course.assigned_teacher)}
        for course in school.get_courses()
    ]

    return render(request, "portal/courses.html", {
        "rows": rows,
        "courses": school.get_courses(),
        "teachers": school.get_teachers(),
    })

def enrollment(request):
    """Enroll or drop students, and show who is in which course."""
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "enroll":
            student_id = request.POST.get("student_id", "")
            course_code = request.POST.get("course_code", "")
            message = school.enroll_student(student_id, course_code)

        elif action == "drop":
            # The drop dropdown sends one value like "S100|PYT300".
            student_id, _, course_code = request.POST.get("enrollment", "").partition("|")
            message = school.drop_student(student_id, course_code)

        else:
            message = "Error: Unknown action."

        if message.startswith("Success"):
            save_all_data(school)
            messages.success(request, message)
        else:
            messages.error(request, message)

        return redirect("enrollment")

    students = school.get_students()
    courses = school.get_courses()

    # Every current (student, course) pair, used for the drop dropdown.
    enrollments = []
    for student in students:
        for code in student.enrolled_course:
            course = school.get_course(code)
            if course:
                enrollments.append({"student": student, "course": course})

    # Each course with its student objects, for the "Course students" table.
    course_rows = [
        {
            "course": course,
            "students": [
                school.get_student(sid)
                for sid in course.enrolled_student_ids
                if school.get_student(sid)
            ],
        }
        for course in courses
    ]

    return render(request, "portal/enrollment.html", {
        "students": students,
        "courses": courses,
        "enrollments": enrollments,
        "course_rows": course_rows,
    })


def home(request):
    """Dashboard with totals for students, teachers, courses, and enrollments."""
    return render(request, "portal/home.html", {
        "student_count": len(school.students),
        "teacher_count": len(school.teachers),
        "course_count": len(school.courses),
        "enrollment_count": sum(len(s.enrolled_course) for s in school.students.values()),
        "school": school,
    })

@require_POST
def delete_student(request, student_id):
    """Delete one student, then go back to the Students page."""
    success, message = school.delete_student(student_id)
    if success:
        save_all_data(school)
        messages.success(request, message)
    else:
        messages.error(request, message)
    return redirect("student_list")


@require_POST
def delete_teacher(request, teacher_id):
    """Delete one teacher, then go back to the Teachers page."""
    success, message = school.delete_teacher(teacher_id)
    if success:
        save_all_data(school)
        messages.success(request, message)
    else:
        messages.error(request, message)
    return redirect("teacher_list")


@require_POST
def delete_course(request, course_code):
    """Delete one course, then go back to the Courses page."""
    success, message = school.delete_course(course_code)
    if success:
        save_all_data(school)
        messages.success(request, message)
    else:
        messages.error(request, message)
    return redirect("course_list")