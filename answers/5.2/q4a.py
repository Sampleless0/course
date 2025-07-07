# list of dictionaries
students = [
    {"Learner": "Jane", "English": 75, "Math": 80, "Science": 85},
    {"Learner": "John", "English": 60, "Math": 68, "Science": 74},
    {"Learner": "Jerome", "English": 81, "Math": 63, "Science": 77},
    {"Learner": "Jason", "English": 55, "Math": 76, "Science": 67},
    {"Learner": "Jessica", "English": 62, "Math": 45, "Science": 68},
    {"Learner": "Joanne", "English": 52, "Math": 47, "Science": 51},
]

# ask for person
selected = input("Enter student name: ")

# check for person and print results
for student in students:
    if selected == student["Learner"]:
        print("Result of Jane")
        print("="*35)
        print(f"English: {student["English"]}")
        print(f"Math: {student["Math"]}")
        print(f"Science: {student["Science"]}")
        print(f"Average mark for {student["Learner"]}: {(student["English"] + student["Math"] + student["Science"])/3:.1f}")

    
    
# expected result

# Enter student name: Jane
# Result of Jane
# ===================================
# English: 75
# Math: 80
# Science: 85
# Average mark for Jane: 80.0
