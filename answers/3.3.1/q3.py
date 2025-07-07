attempts = 3

# while loop if got attempts
while attempts > 0:
    password = input("Enter your password: ")
    
    # check if number of characters is >6
    if len(password) < 6:
        attempts -= 1
        print("Your password is too short!")

    # check if there is no digits inside the password
    elif not(any(letter.isdigit() for letter in password)):
        attempts -= 1
        print("your password does not have at least one digit")
    
    else:
        break

# print results
if attempts == 0:
    print("Too many failed attempts. System locked.")
else:
    print("good job")
