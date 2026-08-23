import json

def read_file(file_path):

    with open(file_path, "r" , encoding = "utf-8") as file:
        return json.load(file)
        
         


def update_file(file_path , write_data):

    with open(file_path, "w" , encoding = "utf-8") as file:
        json.dump(write_data , file ,indent = 4)


