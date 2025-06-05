inputPin = input("Enter 4 digit PIN: ")
if inputPin == "1234":
    amount = int(input("withdrawal amount: "))
    if amount <= 500:
        print(f"withdrawal successful, remaining amount = {500 - amount}")
    else:
        print("insufficient funds")
else:
    print("incorrect pin, access denied")
