import json

def run_workflow():
    with open("student_data.json", "r") as file:
        student_data = json.load(file)

    subjects = student_data["subjects"]
    priority_subjects = []

    for subject, marks in subjects.items():
        if marks < 50:
            priority_subjects.append(subject)

    print("===== Rule-Based Workflow =====")
    print("Student:", student_data["student"])
    print("\nStudy Recommendation:")

    for subject in priority_subjects:
        print("-", subject)


if __name__ == "__main__":
    run_workflow()
    