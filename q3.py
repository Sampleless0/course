attempts = 3
while attempts > 0:
    password = input("Enter your password: ")
    if len(password) < 6:
        attempts -= 1
        print("Your password is too short!")
    elif not(any(letter.isdigit() for letter in password)):
        attempts -= 1
        print("your password does not have at least one digit")
    else:
        break
if attempts == 0:
    print("Too many failed attempts. System locked.")
else:
    print("good job")
