def validate_text(prompt):
    name = input(prompt).strip()
    while name.isalpha() != True :
        name = input(f"Invalid characters! \n{prompt}").strip().title()
    return name.title()

def validate_age(prompt):
    while True:
        age = input(prompt).strip()
        if not age.isdigit():
            print(f"cannot be blank ! \n{prompt}")
            continue
        age = int(age)
        if age < 5 or age > 100:
            print("Error: Please enter a valid age between 5 and 100.")
            continue
        return age

def validate_general_text(prompt):
    text = input(prompt).strip()
    while len(text) == 0:
        text = input(f"cannot be blank ! \n {prompt}").strip()
    return text

def validate_menu_choice(prompt, minimum, maximum):
    while True:
        choice = input(prompt).strip()
        if not choice.isdigit():
            print("Error: Please enter a number.")
            continue
        choice = int(choice)
        if choice < minimum or choice > maximum:
            print(
                f"Error: Please choose a number "
                f"between {minimum} and {maximum}."
            )
            continue
        return choice