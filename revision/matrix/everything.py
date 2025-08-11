import copy

matrixA = [
    [2, 1, -1],
    [-3, 2, 4],
    [1, -3, 2]
]
matrixB = [
    [3.31429],
    [-0.428571],
    [1.2]
]



def add(matrixA, matrixB):
    if len(matrixA) == len(matrixB) and len(matrixA[0]) == len(matrixB[0]):
        result = []
        for i in range(len(matrixA)):
            list = []
            for j in range(len(matrixB)):
                list.append(matrixA[i][j] + matrixB[i][j])
            result.append(list)
        return result
    return None



def subtract(matrixA, matrixB):
    if len(matrixA) == len(matrixB) and len(matrixA[0]) == len(matrixB[0]):
        result = []
        for i in range(len(matrixA)):
            list = []
            for j in range(len(matrixB)):
                list.append(matrixA[i][j] - matrixB[i][j])
            result.append(list)
        return result
    return None



def multiply(matrixA, matrixB):
    if len(matrixA[0]) == len(matrixB):
        result = []
        for i in range(len(matrixA)):
            result.append([])
            for j in range(len(matrixB[0])):
                result[i].append(0)
                for k in range(len(matrixB)):
                    result[i][j] += matrixA[i][k] * matrixB[k][j]
        return result
    return None





def main():
    while True:
        inp = input('what function do you want to use? \n--> ')
        if inp == "+":
            print(add(matrixA, matrixB))
        elif inp == "-":
            print(subtract(matrixA, matrixB))
        elif inp == "*":
            print(multiply(matrixA, matrixB))
        else:
            print("invalid input")

main()
