#Code by Tuba
from itertools import cycle

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board + list(zip(*board)) + [(board[0][0], board[1][1], board[2][2]), (board[0][2], board[1][1], board[2][0])]:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]
    return None

def tic_tac_toe():
    board = [[' ']*3 for _ in range(3)]
    players = cycle(['X', 'O'])
    current_player = next(players)

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            elif all(cell != ' ' for row in board for cell in row):
                print_board(board)
                print("It's a tie!")
                break
            else:
                current_player = next(players)
        else:
            print("Cell already occupied. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
