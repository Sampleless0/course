def check(physics, chemistry, math):
    if (physics + chemistry + math) / 3 >= 50:
        return "Pass"
    else:
        return "Fail"

try:
    phy = int(input("Enter the physics: "))
    chem = int(input("Enter the chemistry: "))
    math = int(input("Enter the mathematics: "))
except Exception:
    print("invalid input")
else:
    print(check(phy, chem, math))
