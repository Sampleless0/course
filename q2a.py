# creating variables
list = []

# asking for 5 numbers
while len(list) < 5:
    number = int(input("input some numbers --> "))
    list.append(number)

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
