from models.school import School
from models.teacher import Teacher 
from models.course import Course
from models.student import Student 

from utils.file_handler import read_file , update_file
from utils.validators import validate_text , validate_number , validate_general_text

if __name__ =="__main__":

    print("System Setup---")
    school_name = validate_general_text("Please enter the name of the school: ")
    school_address = validate_general_text("Please enter the school's address")

    my_school =School(school_name, school_address)
    print(f"Welcome to {my_school.name} Managemet System")

    git