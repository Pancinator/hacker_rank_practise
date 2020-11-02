def count_region_cells(matrix, row, col):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[row]):
        return 0
    if matrix[row][col] == 0:
        return 0

    cell_count = 1
    matrix[row][col] = 0

    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r != row or c != col:
                cell_count += count_region_cells(matrix, r, c)

    return cell_count

def connected_cell(matrix):
    max_cell_counter = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                region_cell_count = count_region_cells(matrix, row, col)
                max_cell_counter = max(max_cell_counter, region_cell_count)

    return max_cell_counter

if __name__ == '__main__':
    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connected_cell(matrix)
    print(result)
