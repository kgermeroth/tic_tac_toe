def make_move (board, player, symbol):
    
    print("Ok, {}, make your move!".format(player))

    while True:
        # asks user for a row
        row_choice = int(input("Row 1, Row 2, or Row 3? > ")) - 1
        print()
        
        # asks user for a column
        column_choice = int(input("Column 1, Column 2, or Column 3? > ")) - 1
        print()

        # check if board at row and column has been taken, else put x or o there depending on player

        if tic_tac_toe_board[row_choice][column_choice] == "-":
            tic_tac_toe_board[row_choice][column_choice] = symbol
            break

        else:
            print("That spot is taken, try again!")


def make_rows_pretty(row):
    pretty_line = ""

    for place in row:
        pretty_line = pretty_line + "   " + place

    return (pretty_line)

def print_board(board):
    """Prints board to show the players"""

    print(make_rows_pretty(board[0]))
    print(make_rows_pretty(board[1]))
    print(make_rows_pretty(board[2]))
    print()


def check_winning_line(value1, value2, value3):
    
    game_finished = False
    winner = None

    if (value1 == value2) and (value2 == value3):
        if value1 == "-":
            game_finished = False
            winner = None
        else:
            game_finished = True

            winner = value1

    return (game_finished, winner)        

 
def check_win(board):

    # check rows

    for row in range(3):
        game_finished, winner = check_winning_line(board[row][0], board[row][1], board[row][2])
        
        if game_finished == True:
            return (game_finished, winner)

    # diagonals

    game_finished, winner = check_winning_line(board[0][0], board[1][1], board[2][2])
    if game_finished == True:
        return (game_finished, winner)

    game_finished, winner = check_winning_line(board[2][2], board[1][1], board[2][0])
    if game_finished == True:
        return (game_finished, winner)

    # columns

    for column in range (3):
        game_finished, winner = check_winning_line(board[0][column], board[1][column], board[2][column])

    return (game_finished, winner)


def check_tie(board):
    """Checks if board is full and there's a tie"""
    game_finished = True

    for row in range (3):
        for column in range (3):
            if board[row][column] == "-":
                game_finished = False

    return game_finished


def play(board):
    """Main REPL function to play the game"""
    game_finished = False
    winner = None

    player_1 = input("Name of Player 1: ")
    player_2 = input("Name of Player 2: ")
    print()

    print("{} you are X's, and {}, you are O's".format(player_1,player_2))
    print()

# loop until win or tie conditions met
    while game_finished == False:
        for player, symbol in [(player_1, "X"), (player_2, "O")]:

            # start by printing the board
            print_board(tic_tac_toe_board)
            # have player make a move
            make_move(tic_tac_toe_board, player, symbol)
            # check for win or tie
            game_finished, winner = check_win(tic_tac_toe_board)
            if game_finished:
                break
            game_finished = check_tie(tic_tac_toe_board)
            if game_finished:
                break


    if winner == None:
        print("It's a tie, there is no winner!")

    else:
        if winner == "X":
            winning_player = player_1
        else:
            winning_player = player2
            
    print("Congratulations, {}. You have won the game!".format(winning_player))


#################################################################################
tic_tac_toe_board = [["-","-","-"],["-","-","-"],["-","-","-"]]



play(tic_tac_toe_board)