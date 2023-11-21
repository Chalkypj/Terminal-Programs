def create_board():
    board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
    return board


def new_game():
    board = create_board()
    player1 = "X"
    player2 = "O"
    running = True
    return board, player1, player2, running


def print_board(board):
    print()
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print(" - + - + -")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print(" - + - + -")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print()


def get_input(board):
    while True:
        try:
            position = int(input("Please Input a Valid Position (1-9): "))
            if position < 1 or position > 9:
                raise ValueError
            if not check_empty_space(board, position):
                raise ValueError
        except ValueError:
            print_board(board)
            print("Input Error!!!\nYou Must Input a Valid Empty Position\nTry Again\n")
            # continue
        else:
            return position


def check_empty_space(board, position):
    if board[position] == " ":
        return True
    return False


def x_turn(board):
    position = get_input(board)
    board[position] = "X"
    return board


def o_turn(board):
    position = get_input(board)
    board[position] = "O"
    return board


def check_end(player, board):
    if check_win(board):
        print(player, "Wins")
        winner = True
    elif check_draw(board):
        print("Game Drawn")
        winner = True
    else:
        winner = False
    return winner


def check_win(board):
    if board[1] == board[2] and board[1] == board[3] and board[1] != " ":
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != " ":
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != " ":
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] != " ":
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != " ":
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != " ":
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] != " ":
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] != " ":
        return True
    else:
        return False


def check_draw(board):
    for key in board.keys():
        if board[key] == " ":
            return False
    return True


if __name__ == "__main__":
    board, player1, player2, running = new_game()
    print_board(board)
    while running:
        winner = False
        if not winner:
            board = x_turn(board)
            print_board(board)
            winner = check_end(player1, board)
        if not winner:
            board = o_turn(board)
            print_board(board)
            winner = check_end(player2, board)
        else:
            running = False
