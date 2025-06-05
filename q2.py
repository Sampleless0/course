def weightOK(weight):
    if weight >= 25:
        return True
    return False

if weightOK(int(input("how many kilograms does your luggage weight -> "))):
    print("there is an extra charge of $20")

print("thank you")
