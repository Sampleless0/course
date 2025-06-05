def isLeftClear():
    #code to check if left side is clear
    return True

robotPathStatus = input("what is the robot's path status (clear, obstacle, destination) -> ").lower()
battery = int(input("input battery percentage -> "))

if robotPathStatus == "destination":
    print("stopped at destination")
elif robotPathStatus == "clear" and battery > 20:
    print("moving forward")
elif robotPathStatus == "obstacle" and battery > 20:
    if isLeftClear():
        print("turning left")
    else:
        print("turning right")
else:
    print("invalid input or battery insufficient")
