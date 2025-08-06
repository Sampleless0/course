matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]


def add(matrix1, matrix2):
    result = [
    ]
    for i in range(len(matrix1)):
        result.append([])
        for j in range(len(matrix1[0])):
            result[i].append(matrix1[i][j] + matrix2[i][j])

    for i in range(len(result)):
        print(result[i])


add(matrix1, matrix2)
