# School Management System

A simple console app for managing a school's students, courses, and teachers. Built in Python for the Unit 2 project — everything runs from a text menu, and all data is saved to JSON so it's still there next time you run it.

## Features

- Add students, courses, and teachers (IDs and course codes are generated automatically)
- Enroll or drop a student from a course
- Assign a teacher to a course
- View everything: all students, all courses, all teachers, or drill into one student's courses / one course's students
- Input validation on every prompt, so you can't enter a blank name, a bad age, or a duplicate ID
- Saves everything to JSON on exit, loads it back automatically next time
- Bad or missing data files won't crash the program — errors get logged to `logs.txt` instead

## Project structure

```
school_system/
├── main.py                # menu loop, load/save
├── models/
│   ├── student.py
│   ├── course.py
│   ├── teacher.py
│   └── school.py          # the class that ties everything together
├── utils/
│   ├── file_handler.py    # read/write JSON
│   ├── validators.py      # input checks
│   └── logging.py
├── data/
│   ├── students.json
│   ├── courses.json
│   └── teachers.json
├── logs.txt
└── diagrams/
    ├── avtivitydiagramschool.jpg
    ├── classdiagramSchool.png
    └── useCsediagram.jpg
```

## Running it

Needs Python 3.8+, no extra packages.

```bash
python3 main.py
```

It'll ask for the school name and address first, then drop you into the menu.

## The menu

1. Add student
2. Add course
3. Add teacher
4. Assign teacher to course
5. Enroll student
6. Drop student from course
7. View students
8. View courses
9. View teachers
10. View student courses
11. View course students
12. Save and exit

## The four classes

**Student** — id, name, age, and a list of enrolled course codes. Can enroll/drop courses.

**Course** — code (auto-generated from the name, e.g. `PYT300`), name, assigned teacher, list of enrolled student IDs.

**Teacher** — id, name, subject taught, and a list of assigned course codes.

**School** — holds everything (three dictionaries: students, teachers, courses) and handles all the cross-entity stuff: enrolling, dropping, assigning, and all the display/reporting.

## Data & errors

Every object has a `to_dict()` used to save it, and on startup the app rebuilds everything from the JSON files. The ID counters (`S100`, `T200`, `PYT300`...) pick up right where they left off, so reloaded data never collides with new records.

Every file read/write is wrapped in try/except — missing file, corrupted JSON, missing field — none of it crashes the app, it just prints a message and logs it.

## Diagrams


![Use case diagram](diagrams/useCsediagram.jpg)


![Activity diagram](diagrams/avtivitydiagramschool.jpg)


![Class diagram](diagrams/classdiagramSchool.png)