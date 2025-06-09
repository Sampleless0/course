# import random module
import random

# gets a random integer between 1 to 10000
num1 = random.randint(1, 10000)
num2 = random.randint(1, 10000)

# forever loop
while True:
    # tries to get an input as int
    try:
        guess = int(input(f"whats {num1} + {num2}: "))
    except Exception:
        print("sorry, try again")
        # restarts loop
        continue
    else:
        
        # check if ans is correct
        if guess == (num1 + num2):
            print("you guessed right")
            break
        else:
            print("sorry, try again")
