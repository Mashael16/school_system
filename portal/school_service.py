"""Creates the one School object the website uses, and loads saved data."""

import os
from pathlib import Path

# Run from the project folder so "data/..." and "logs.txt" paths always work,
# no matter where the server starts.
os.chdir(Path(__file__).resolve().parent.parent)

from models.school import School
from main import load_students, load_teachers, load_courses, save_all_data

school = School("My School", "School address")

load_students(school)
load_teachers(school)
load_courses(school)