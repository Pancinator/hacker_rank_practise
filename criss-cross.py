import array

class crissCross:
    size = 5
    rows = list()
    def __init__(self, size):
        self.size = size

    def create_board(self):
        for i in range(self.size):
            row = input("napiste hodntoy oddelene medzerou").split()
            if len(row) > self.size:
                print("Zadali ste privela arguemntov!! Zadajte hodnoty pre dany riadok znova")
            else:
                self.rows.append(row)
        return self.rows

    def print_board(self):
        for row in self.rows:
            print(*row)

    def solve_board(self):
        number_of_triplets = 0
        for r in range(len(self.rows)):
            for c in range(len(self.rows[r])):
                if self.rows[r][c] == 'X':
                    actual_position_x = c
                    actual_position_y = r
                    if ((actual_position_x + 2) <= (self.size-1)):
                        if self.rows[actual_position_y][actual_position_x + 1] == 'X':
                            if self.rows[actual_position_y][actual_position_x + 2] == 'X':
                                number_of_triplets += 1

                    if (actual_position_y + 2) <= (self.size - 1):
                        if self.rows[actual_position_y + 1][actual_position_x] == 'X':
                            if self.rows[actual_position_y + 2][actual_position_x] == 'X':
                                number_of_triplets += 1

                    if ((actual_position_x + 2) <= (self.size - 1)) and ((actual_position_y + 2) <= (self.size - 1)):
                        if self.rows[actual_position_y + 1][actual_position_x + 1] == 'X':
                            if self.rows[actual_position_y + 2][actual_position_x + 2] == 'X':
                                number_of_triplets += 1
        return number_of_triplets

if __name__ == '__main__':

    size = int(input("Zadajte velkost hracej plochy"))
    play_board = crissCross(size)
    play_board.create_board()
    play_board.print_board()
    print(play_board.solve_board())


