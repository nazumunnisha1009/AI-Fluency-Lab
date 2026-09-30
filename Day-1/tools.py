import json


def read_student_data():
    with open("student_data.json", "r") as file:
        return json.load(file)
    