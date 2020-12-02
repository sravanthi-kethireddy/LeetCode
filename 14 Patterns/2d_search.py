def search_2d(matrix, num):
    cols = len(matrix[0])
    rows = len(matrix)
    for i in range(rows):
        for j in range(cols):
            if num == matrix[i][j]:
                return True
    return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

print(search_2d(matrix,53))