"""
Input validation helpers.

Each function keeps asking the user until the input is valid, then
returns the cleaned value. This keeps bad data out of the models.
"""


def validate_text(prompt):
    """Ask for a name made of letters only and return it in Title Case."""
    name = input(prompt).strip()
    while name.isalpha() != True :
        name = input(f"Invalid characters! \n{prompt}").strip().title()
    return name.title()


def validate_age(prompt):
    """Ask for an age and return it as an int between 5 and 100."""
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
    """Ask for any non-empty text and return it without extra spaces."""
    text = input(prompt).strip()
    while len(text) == 0:
        text = input(f"cannot be blank ! \n {prompt}").strip()
    return text


def validate_menu_choice(prompt, minimum, maximum):
    """Ask for a menu number and return it once it is within range.

    Args:
        prompt (str): the text shown to the user.
        minimum (int): the lowest valid option.
        maximum (int): the highest valid option.
    """
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