# store matrix of A and B
A = [
    [2, -3],
    [4, 5]
]

B = [
    [1, 7],
    [-2, 0]
]

# sum
def sum(matrix1, matrix2):
    total = []
    for row in range(len(matrix1)):
        total.append([])
        for item in range(len(matrix1[row])):
            total[row].append(matrix1[row][item] + matrix2[row][item])
    return total

print(sum(A, B))
