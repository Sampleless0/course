# import random module
import random

# function to check ans and guess (takes in "ans" and "guess")
def check(ans, guess):
    if guess == ans:
        return "u did it"
    elif guess < ans:
        return "higher"
    elif guess > ans:
        return "lower"
    return None

# forever loop
while True:
    guess = 0
    # random integer between 1 and 100
    ans = random.randint(1, 100)

    # loop if not guessed correctly
    while ans != guess:
        # tries to receive guess as int
        try:
            guess = int(input('Enter your choice: '))
        except Exception:
            print("invalid input")
        else:
            # print result
            print(check(ans, guess))

    # asking for repeating the game (loop)
    result = input("do u wanna play again? y/n: ")
    if result == "y":
        print("ok\n\n")
    else:
        break
