board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def board_reset():
    for i in range(4):
        for j in range(4):
            board[i][j] = 0

def find_next_location(starting_position):
    for i in range(starting_position[0], 4):
        for j in range(4):
            if board[i][j] == 0:
                return [i, j]
    return -1


def place_queen(queen_number, starting_position=None):
    board[starting_position[0]][starting_position[1]] = queen_number

def set_conflict_locations(queen_number, queen_row, queen_col):
    conflict = queen_number[1]
    for x in range(4):
        if board[queen_row][x] != queen_number and board[queen_row][x] == 0:
            board[queen_row][x] = conflict
    for y in range(4):
        if board[y][queen_col] != queen_number and board[y][queen_col] == 0:
            board[y][queen_col] = conflict
    for k in range(1, 4):
        if (queen_row - k)  in range(4):
            if (queen_col - k) in range(4):
                if board[queen_row - k][queen_col - k] != queen_number and board[queen_row - k][queen_col - k] == 0:
                    board[queen_row - k][queen_col - k] = conflict
            if (queen_col + k) in range(4):
                 if board[queen_row - k][queen_col + k] != queen_number and board[queen_row - k][queen_col + k] == 0:
                    board[queen_row - k][queen_col + k] = conflict
        if (queen_row + k)  in range(4):
            if (queen_col + k) in range(4):
                if board[queen_row + k][queen_col + k] != queen_number and board[queen_row + k][queen_col + k] == 0:
                    board[queen_row + k][queen_col + k] = conflict
            if (queen_col - k) in range(4):
                if board[queen_row + k][queen_col - k] != queen_number and board[queen_row + k][queen_col - k] == 0:
                    board[queen_row + k][queen_col - k] = conflict
       
            
def dead_end():
    board_reset()
    dead_end_happened = True
    return dead_end_happened

def display_board():
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == "Q":
                print(board[i][j], end=" ")
            else:
                print(board[i][j], end="  ")
        print(end="\n")
    print(end="\n")

def main():
    solutions = 0
    for i in range(4):
        current_queen = 1
        starting_position = [0, i]
        place_queen(f"Q{current_queen}", starting_position)
        set_conflict_locations(f"Q{current_queen}", starting_position[0], starting_position[1])
        current_queen = 2
        dead_end_happened = False
        for j in range(3):
            next_location = find_next_location(starting_position)
            if next_location == -1:
                dead_end_happened = dead_end()
                break
            else:
                starting_position = next_location
                place_queen(f"Q{current_queen}", starting_position)
                set_conflict_locations(f"Q{current_queen}", starting_position[0], starting_position[1])
                current_queen += 1
        if dead_end_happened == False and current_queen == 5:
            solutions = solutions + 1
            display_board()
            board_reset()
    print(f"There are/is {solutions} solutions")

main()