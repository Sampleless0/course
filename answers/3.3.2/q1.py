gridsize = 0

# while loop
while gridsize == 0:
    # try to receive input
    try:
        gridsize = int(input("grid size -> "))
    except Exception:
        # if fail
        print("bro put in a real number")

# loop in range
for i in range(gridsize):
    print()
    for j in range(gridsize):
        print(gridsize * i + j + 1, end=" ")
