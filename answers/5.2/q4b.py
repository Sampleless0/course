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
        print("="*35)
        
        # calculate total for each subject
        englishAvg = 0
        mathAvg = 0
        scienceAvg = 0
        for avg in students:
            englishAvg += avg["English"]
            mathAvg += avg["Math"]
            scienceAvg += avg["Science"]
            print(f"Average mark for {avg["Learner"]}: {(avg["English"] + avg["Math"] + avg["Science"]) / 3:.1f}")
        print("=" * 35)
        
        # convert to average for each subject
        print(f"Average mark for English: {englishAvg/len(students):.1f}")
        print(f"Average mark for Math: {mathAvg/len(students):.1f}")
        print(f"Average mark for Science: {scienceAvg/len(students):.1f}")


# expected result

# Enter student name: Jane
# Result of Jane
# ===================================
# English: 75
# Math: 80
# Science: 85
# Average mark for Jane: 80.0
# ===================================
# Average mark for Jane: 80.0
# Average mark for John: 67.3
# Average mark for Jerome: 73.7
# Average mark for Jason: 66.0
# Average mark for Jessica: 58.3
# Average mark for Joanne: 50.0
# ===================================
# Average mark for English: 64.2
# Average mark for Math: 63.2
# Average mark for Science: 70.3
