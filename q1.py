gridsize = 0
while gridsize == 0:
    try:
        gridsize = int(input("grid size -> "))
    except Exception as e:
        print("bro put in a real number")

for i in range(gridsize):
    print()
    for j in range(gridsize):
        print(gridsize * i + j + 1, end=" ")
