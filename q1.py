# set variables
sufficient = False
amtF = 0

# while loop
while amtF * 2 < 180:
    # calculate amount saved
    amt = float(input("How much are you saving this round? -> "))
    print(f"Matched amount from parents: ${amt * 2}")
    multiplier = 1

    # check for when money reaches 180
    while amt * multiplier * 2 <= (180-(amtF*2)):
        multiplier += 1
    amtF += amt
    # print results when done
    if amt * 2 < 180 and amtF * 2 < 180:
        print(f"You need to save this amount {multiplier-1} more time(s) to reach $180")
print("Great job! You've saved enough to buy the wireless earbuds!")
