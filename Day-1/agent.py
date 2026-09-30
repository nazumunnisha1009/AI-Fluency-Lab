from tools import read_student_data

print("===== AI Agent =====")

user_request = input("\nUser: ")

print("\nAgent: I need to check the student's private study data.")

student_data = read_student_data()

print("Agent: Private data retrieved successfully.")

subjects = student_data["subjects"]

priority_subjects = []

for subject, marks in subjects.items():
    if marks < 50:
        priority_subjects.append(subject)

print("\nAgent: Based on the student's current progress,")
print("you should focus on:")

for subject in priority_subjects:
    print("-", subject)