def validate_text(prompt):
    name = input(prompt).strip().title()
    while name.isalpha() != True :
        name = input(f"Invalid characters! \n{prompt}").strip().title()
    return name

    
def validate_number(prompt):
    number = input(prompt).strip()
    while number.isnumeric() != True :
        number = input(f"Invalid age \n{prompt}").strip()
    return int(number)

       
def validate_general_text(prompt):
    text = input(prompt).strip()
    while len(text) == 0:
        text = input(f"cannot be blank ! \n {prompt}").strip()
    return text
