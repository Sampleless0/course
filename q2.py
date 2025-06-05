import random

def check(ans, guess):
    if guess == ans:
        return "u did it"
    elif guess < ans:
        return "higher"
    elif guess > ans:
        return "lower"
    return None

while True:
    guess = 0
    ans = random.randint(1, 100)

    while ans != guess:
        try:
            guess = int(input('Enter your choice: '))
        except Exception:
            print("invalid input")
        else:
            print(check(ans, guess))

    result = input("do u wanna play again? y/n: ")
    if result == "y":
        print("ok\n\n")
    else:
        break
