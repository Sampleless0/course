# list people
people = [
    {"name": "Mary Tan", "nric": "S1234567A"},
    {"name": "Steve Lim", "nric": "S2340986T"},
    {"name": "Yeo Ming Ming", "nric": "S6734278E"},
    {"name": "Aaron Smith", "nric": "G7878439K"},
    {"name": "Lam Lin Shan", "nric": "S4456223G"}
]

# search for nric
input = input("NRIC --> ").upper()
searched = []

# check for valid nric
for person in people:
    if input == person["nric"]:
        searched.append(person)

# print name and nric for each person
if searched:
    for person in searched:
        print(f'Name: {person["name"]}, NRIC: {person["nric"]}')
else:
    print("Record Not Found")
