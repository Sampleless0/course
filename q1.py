import random

num1 = random.randint(1, 10000)
num2 = random.randint(1, 10000)

while True:
    try:
        guess = int(input(f"whats {num1} + {num2}: "))
    except Exception:
        print("sorry, try again")
        continue
    else:
        if guess == (num1 + num2):
            print("you guessed right")
            break
        else:
            print("sorry, try again")
