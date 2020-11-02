def get_biggest_region(matrix):
    max_cell_counter = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                size = _get_biggest_region(matrix, row, col) #pass the currnet location to recursive function
                max_cell_counter = max(max_cell_counter, size)
    return max_cell_counter


def _get_biggest_region(matrix, row, col):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[row]):
        return 0
    if matrix[row][col] == 0:
        return 0


    size = 1
    matrix[row][col] = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r != row or c != col:
                size += _get_biggest_region(matrix, r, c)

    return size


def connected_cell(matrix):
    pass

if __name__ == '__main__':
    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = get_biggest_region(matrix)
    print(result)
