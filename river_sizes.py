
list_of_used = []
list_of_lengths = []


def find_neighbours(pos, matrix):
    y, x = pos
    neighbours = []
    if x >= 1:
        neighbours.append((y, x-1))
    if x < len(matrix[0]) - 1:
        neighbours.append((y, x+1))
    if y < len(matrix)-1:
        neighbours.append((y+1, x))
    if y >= 1:
        neighbours.append((y-1, x))
    return neighbours


def river_size(mat):
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            if mat[row][col] == 1 and (row, col) not in list_of_used:
                list_of_used.append((row, col))
                river_length = 1
                stack = [(row, col)]

                while stack:
                    current = stack.pop()
                    neighbours = find_neighbours(current, mat)
                    for nb in neighbours:
                        y, x = nb
                        if mat[x][y] == 1 and (y, x) not in list_of_used:
                            river_length += 1
                            stack.append((y, x))
                            list_of_used.append((y, x))

                list_of_lengths.append(river_length)
    return list_of_lengths

if __name__ == '__main__':
    matrix = [[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]
    print(river_size(matrix))