"""Print a Matrix with Row and Column Indices"""


def print_matrix(matrix):
    # Generate column header, offset by 4 space characters
    result = " " * 4
    for col_index in range(len(matrix[0])):
        result += f"{col_index} "
    result += f"\n    {'— '*len(matrix[0])}\n"

    # Generate matrix rows with row indices
    for row in range(len(matrix)):
        result += f"{row} | "
        for col in range(len(matrix[0])):
            result += f"{matrix[row][col]} "
        result += "\n"

    print(result)


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [
    [1, 2, 7, 4, 5, 6],
    [5, 6, 7, 8, 9, 0],
    [0, 0, 0, 0, 0, 0],
    [6, 6, 2, 3, 1, 4],
    [4, 3, 2, 1, 0, 1],
]
print_matrix(matrix1)
print_matrix(matrix2)
