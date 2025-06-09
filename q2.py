# receive input in lowercase
temperature = input("Is it warm or cold? (warm/cold):").lower()

# check with if else and print result
if temperature == "cold":
    raining = input("Is it raining? (yes/no):").lower()
    if raining == "yes":
        print("Wear a raincoat.")
    else:
        print("Wear a warm jacket.")
elif temperature == "warm":
        print("Wear a T-shirt.")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
