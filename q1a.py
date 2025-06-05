def isValueCorrect(value):
    if value <= 0 // value > 100:
        return "out of range"
    return "ok"

print(isValueCorrect(int(input("gib me number -> "))))


