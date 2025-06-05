budget = float(input("how much ur budget -> "))

while budget >= 0:
    spend = float(input("how much u spend -> "))
    if budget - spend < 0:
        print("This expense exceeds your remaining budget. Please enter a smaller amount.")

    elif (input("do u really want to spend money (yes/no) -> ".lower())) == "yes":
        budget -= spend
        print(f"spent amount: {spend}")
        print(f"your remaining budget: {budget}")
        if budget == 0:
            print("Budget limit reached! No more spending allowed.")
            break
        elif budget <= 5:
            print("Warning: You are close to exceeding your budget!")
