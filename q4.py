def calculateAvg(studentScore):
    studentScore = sum(studentScore) / len(studentScore)
    return studentScore

avg = calculateAvg([float(input("first student score -> ")),float(input("second student score -> ")),float(input("third student score -> "))])

print(f'average score: {avg:.1f}')
if avg > 95:
    print("congratulations. excellent performance")
else:
    print("good luck next time")
