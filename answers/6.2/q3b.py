# store matrix of A and B
A = [
    [2, -3],
    [4, 5]
]

B = [
    [1, 7],
    [-2, 0]
]

def multiply(matrix1, matrix2):
    result = []
    for row in range(len(matrix1)):
        result.append([])
        for item in range(len(matrix1[row])):
            result[row].append(0)
            for element in range(len(matrix1[row])):
                result[row][item] += matrix1[row][element] * matrix2[element][item]
    return result

print(multiply(A, B))
