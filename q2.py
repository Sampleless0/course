# list variables
current = 0
future = 10000
interest = 0.05
years = 10

# calculate for compound interest
current = future/((1+interest)**years)

# print result
print(f"You need to deposit today: ${current:.2f}")
