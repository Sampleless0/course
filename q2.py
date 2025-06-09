# receive input
robotPathStatus = input("what is the robot's path status (clear, obstacle, destination) -> ").lower()
battery = int(input("input battery percentage -> "))

# check for battery and input while printing result
if robotPathStatus == "destination":
    print("stopped at destination")
elif robotPathStatus == "clear" and battery > 20:
    print("moving forward")
elif robotPathStatus == "obstacle" and battery > 20:
    print("turn left or right")
else:
    print("invalid input or battery insufficient")
