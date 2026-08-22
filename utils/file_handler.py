import json

def read_file(file_path):

    with open(file_path, "r" , encoding = "utf-8") as file:
        loaded_data = json.load(file)
        
        return loaded_data


def update_file(file_path , write_data):

    with open(file_path, "w" , encoding = "utf-8") as file:
        json.dump(write_data , file ,indent = 4)


