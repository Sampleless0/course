def isLeftClear():
    #code to check if left side is clear
    return True

robotPathStatus = input("what is the robot's path status (clear, obstacle, destination) -> ").lower()

if robotPathStatus == "destination":
    print("stopped at destination")
elif robotPathStatus == "clear":
    print("moving forward")
elif robotPathStatus == "obstacle":
    if isLeftClear():
        print("turning left")
    else:
        print("turning right")
else:
    print("invalid input")
