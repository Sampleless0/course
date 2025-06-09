# receive inputs as float
first = float(input("first student score -> ")
second = float(input("second student score -> ")
third = float(input("third student score -> ")

# calculate average and print as 1dp
avg = (first + second + third) / 3
print(f'average score: {avg:.1f}')

# if else to check if average >95
if avg > 95:
    print("congratulations. excellent performance")
else:
    print("good luck next time")
