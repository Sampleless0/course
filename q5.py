student = [float(input("first test score -> ")), \
           float(input("second test score -> ")), \
           float(input("third test score -> "))]

def calculateSuccess(score):
    avg = sum(score) / len(score)
    if avg < 85:
        return "not eligible"
    else:
        for i in score:
            if i < 50:
                return "not eligible"
    return "eligible"

print(calculateSuccess(student))
