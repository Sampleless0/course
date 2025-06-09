# input variables as float
first = float(input("first test score -> "))
second = float(input("second test score -> "))
third = float(input("third test score -> "))

# calculate average
avg = (first + second + third) / 3

# check for eligiblility
eligible = ""
if avg < 85 or first < 50 or second < 50 or third < 50:
           eligible = "not eligible"
else:
           eligible = "eligible"

# print result
print(eligible)
