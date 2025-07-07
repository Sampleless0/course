# creating variables
list = []

# asking for 5 numbers (with try except)
while len(list) < 5:
    try:
        number = int(input("input some numbers --> "))
        list.append(number)
    except ValueError:
        print("invalid input, please try again")

# find lowest & highest
lowest = min(list)
highest = max(list)
total = sum(list)
average = sum(list) / len(list)

# print results
print(f"lowest = {lowest}")
print(f"highest = {highest}")
print(f"total = {total}")
print(f"average = {average}")
