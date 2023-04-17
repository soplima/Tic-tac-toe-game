def print_board(board):
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print("   |   |   ")

def check_win(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != ' ':
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != ' ':
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != ' ':
        return True
    if board[2] == board[4] == board[6] and board[2] != ' ':
        return True

    return False

def tic_tac_toe():
    board = [' '] * 9
    player = 'X'
    turns = 0

    while turns < 9:
        print_board(board)
        print("Player {}, it's your turn.".format(player))
        move = int(input("Enter a number between 1 and 9: ")) - 1

        if board[move] == ' ':
            board[move] = player
            turns += 1
            if check_win(board):
                print_board(board)
                print("Congratulations, Player {} wins!".format(player))
                return
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        else:
            print("That space is already taken. Try again.")

    print_board(board)
    print("It's a tie!")

tic_tac_toe()
