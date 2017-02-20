
'''

USER REQUIREMENTS (Unordered)

-> There needs to be a 3 x 3 board

-> Need user input for player 1 and player 2

-> Need to be able to make move by choosing spot on board

-> Announce a winner

-> Check for a winner

-> display current board to the user

'''

'''
USER REQUIREMENTS (PRIORITY)

PRIORITY LEVEL 1

    -> There needs to be a 3 x 3 board (DONE-TESTED)
    -> display current board to the user (DONE-TESTED)

PRIORITY LEVEL 2


    -> Need to be able to make move by choosing spot on board
        // users need to input two numbers in order to make a move
        // numbers must be between 0 and 2
        // keep track of users input
        // if spot is in use ask again

PRIORITY LEVEL 3

    -> Check for a winner
    -> Announce a winner

'''

game_board = []
player_turn = 0 # X --> 0 and O--> 1

'''
USAGE: Creates a 3 x 3 board that will store our values in a
2d array in our global variable game_board that will be represented by the following

*  *  *
*  *  *
*  *  *

INPUT: NONE

OUTPUT: NONE

'''
def create_board():
    global game_board

    for i in range(0,3):
        temp_list = []

        for j in range(0,3):

            temp_list.append('*')

        game_board.append(temp_list)



'''
USUAGE: displays the current state of the game board

*  *  *
*  *  *
*  *  *

INPUT: NONE

OUTPUT: print our board
'''
def display_board():
    global game_board
    our_board = '''
                {} {} {}

                {} {} {}

                {} {} {}
                '''.format(game_board[0][0], game_board[0][1], game_board[0][2], game_board[1][0], game_board[1][1], game_board[1][2], game_board[2][0], game_board[2][1], game_board[2][2])

    print(our_board)



def make_move(row,col):
    # global game_game board
    global game_board
    # get player turn and store as variable 'move'
    move = get_turn()
    # change game_board[row][col] = 'move'
    game_board[int(row)][int(col)] = move
    # change player turn
    change_turn()



'''
USAGE: Checks if the users move is valid or not
INPUT: A row and a col integer
OUTPUT: True if valid False otherwise
'''
def is_valid_move(row, col):

    global game_board

    if str(row).isdigit() == False or str(col).isdigit() == False:

        return False


    elif (int(row) < 0 or int(row) > 2) or (int(col) < 0 or int(col) > 2):
        return False

    elif game_board[int(row)][int(col)] != "*":
        return False

    else:
        return True



'''
USAGE: Ask the user for a row and a column
INPUT: NONE
OUTPUT: The row and column
'''
def get_user_move():

    row = input("Enter a row between 0 and 2 >>> ")

    col = input("Enter a column between 0 and 2 >>> ")

    if is_valid_move(row,col) == True:


        make_move(row,col)
        display_board()
    else:

        get_user_move()






'''
USAGE: Get the current players move
INPUT: NONE use player_turn global variable
OUTPUT: return either x or o
'''
def get_turn():

    global player_turn


    if player_turn == 0:
        return "X"
    else:
        return "O"





'''
USAGE: Change from player 1 to player 2 with each turn
INPUT: None - use global variable player_turn
OUTPUT: None
'''
def change_turn():

    global player_turn

    if player_turn == 0:
        player_turn = 1
    elif player_turn == 1:
        player_turn = 0
    else:
        print("error")

'''
USAGE: Checks if the board is filled
INPUT: NONE
GLOBAL: game_board
OUTPUT: TRUE if full, False OTHERWISE
'''
def is_board_filled():

    global game_board
    for i in range(0,3):
        for j in range(0,3):
            spot = game_board[i][j]
            if spot == "*":
                return False
    return True


'''
USAGE: Creating a filled board to check is_board_filled function
INPUT: NONE
GLOBAL: game_board
OUTPUT: NONE
'''
def fill_board():
    global game_board
    for i in range(0,3):
        for j in range(0,3):
            game_board[i][j] = 'x'

'''
USAGE: Clears board for doctest
INPUT: None
GLOBAL: game_board
OUTPUT: None
'''
def clear_board():
    global game_board
    for i in range(0, 3):
        for j in range(0, 3):
            game_board[i][j] = '*'


'''
USAGE: Checks if player has won horizontally
INPUT: NONE
GLOBAL: game_board
OUTPUT: TRUE if horizontal win, FALSE otherwise
'''
def is_horizontal_win():
    global game_board
    for row in range(len(game_board)):
        if game_board[row][0] == game_board[row][1] == game_board[row][2] == 'X':
            return True
        if game_board[row][0] == game_board[row][1] == game_board[row][2] == 'O':
            return True
    return False

'''
USAGE: Checks if player has won vertically
INPUT: NONE
GLOBAL: game_board
OUTPUT: TRUE if vertical win, FALSE otherwise
'''
def is_vertical_win():
    global game_board
    for col in range(len(game_board)):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] == 'X':
            return True
        if game_board[0][col] == game_board[1][col] == game_board[2][col] == 'O':
            return True
    return False


'''
USAGE: Checks if player has won diagonally
INPUT: NONE
GLOBAL: game_board
OUTPUT: TRUE if diagonal win, FALSE otherwise
'''
def is_diagonal_win():
    global game_board
    if game_board[0][0] == game_board[1][1] == game_board[2][2] == 'X':
        return True
    if game_board[0][0] == game_board[1][1] == game_board[2][2] == 'O':
        return True
    if game_board[0][2] == game_board[1][1] == game_board[2][0] == 'X':
        return True
    if game_board[0][2] == game_board[1][1] == game_board[2][0] == 'O':
        return True
    return False


def is_win():
    global game_board
    if is_horizontal_win() == False and is_vertical_win() == False and is_diagonal_win() == False:
        return False
    return True

def main():
    global game_board
    create_board()
    display_board()


    while is_board_filled() == False:
        get_user_move()
        if is_win() == True:
            break


main()
