# receive input
robotPathStatus = input("what is the robot's path status (clear, obstacle, destination) -> ").lower()

# check using if else while printing
if robotPathStatus == "destination":
    print("stopped at destination")
elif robotPathStatus == "clear":
    print("moving forward")
elif robotPathStatus == "obstacle":
   print("turn left or right")
else:
    print("invalid input")
