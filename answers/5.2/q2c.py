# list people
people = [
    {"name": "Mary Tan", "nric": "S1234567A"},
    {"name": "Steve Lim", "nric": "S2340986T"},
    {"name": "Yeo Ming Ming", "nric": "S6734278E"},
    {"name": "Aaron Smith", "nric": "G7878439K"},
    {"name": "Lam Lin Shan", "nric": "S4456223G"}
]


# print name and nric for each person
for person in people:
  print(f'Name: {person["name"]}, NRIC: {person["nric"]}')
