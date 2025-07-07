# receive input and convert it to lowercase (eg DAY --> day)
someoneInRoom = input("is someone in the room -> (yes/no) ").lower()

# check for variables and print result
if someoneInRoom == "yes":
    isDayNight = input("is it day or night -> (day/night) ").lower()
    if isDayNight == "day":
        print("Lights OFF")
    elif isDayNight == "night":
        print("Lights ON")
    else:
        print("invalid input")
elif someoneInRoom == "no":
    print("Lights OFF")
else:
    print("invalid input")
