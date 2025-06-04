current = 0
future = 10000
interest = 0.05
years = 10

def amountRequired():
    current = future/((1+interest)**years)
    print(f"You need to deposit today: ${current:.2f}")


amountRequired()
