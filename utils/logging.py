def log_error(error_message):

    with open("logs.txt" , "a" ,encoding ="utf-8") as file:
        file.write(error_message + "\n")
