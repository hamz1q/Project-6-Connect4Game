# Hamza Qureshi Testing Script
" if the user chooses player vs player then this function will determine whose turn it is "

#from proj2 import AdjoinTheSpheres

def player_vs_player(move_1, move_2):
    return None



def test_player_vs_player():
    move_1 = int(input('Move: '))
    move_2 = int(input('Move: '))
    # while move_1 is selected, player 2 should not be allowed to enter something
    while move_1:
        if move_2:
            print('Failed')
        else:
            print('Passed')
    while move_2:
        if move_1:
            print('Failed')
        else:
            print('Passed')
    # tests to ensure the turns are not the same
    if move_1 == move_2:
        print('Fail')
    elif move_2 == move_1:
        print('Failed')
    else:
        print('Passed')

    # test to avoid forbidden postion
    if move_1 == '*' or move_2 == '*':
        print('Failed')
    else:
        print('Passed')

# if the user chooses player vs computer then this function will determine whose turn it is "

def player_vs_computer(player_move, computer_move):
    return None


def test_player_vs_computer():
    from random import randint
    computer_move = randint
    player_move = int(input('Move: '))

    # test randint function
    # test player move and ranint not equal
    # test to avoid forbidden space
    if computer_move == randint:
        print('Passed')
    else:
        print('Failed')

    if computer_move == player_move:
        print('Failed')
    elif player_move == computer_move:
        print('Failed')
    else:
        print('Passed')

    if computer_move == '*' or player_move == '*':
        print('Failed')
    else:
        print('Passed')


# function should load the board
def load_game(file):
    return None

def test_load_game(file):
    with open(file) as read_file:
        print(read_file.readlines)

    # makes sure the file exists
    if read_file(file).is_file():
        print('Passed')
    else:
        print('Failed')

    # makes sure board is at least 4x4
    for x in range(len(file)):
        for y in range(len(file)):
            if x * y == 16 or x * y > 16:
                print('Passed')
            else:
                print('Failed')


    # idk what else i could test load game for ??

def game_options():
    return None

def test_game_options(selection, ):
# tests to make sure all input options are correct 
    if selection == 'Player vs Player':
        print('Passed')
    elif selection == 'Computer vs Player':
        print('passed')
    else:
        print('Failed')

    if selection == 'save game':
        print('Passed')
    elif selection == 'load game':
        print('PAssed')
    else:
        print('Failed')
        
    if selection != int:
        print('Failed')
    else:
        print('Passed')

def play_game():
    return None



def test_play_game(move1, move2, board):
    # test for valid location

    if move1 == '.' or move1 == '':
        print('Passed')
    else:
        print('Failed')
    if move2 =='.' or move2 == '':
        print('Passed')
    else:
        print('Failed')
    # tests for connect 4 ??
    for row in board:
        if board[row][0] == move1 * 4:
            print('Passed')
        else:
            print('Failed')
    for col in board:
        if board[0][row] == move1 * 4:
            print('Passed')
        else:
            print('Failed')

    for row in board:
        if board[row][0] == move2 * 4:
            print('Passed')
        else:
            print('Failed')
    for col in board:
        if board[0][row] == move2 * 4:
            print('Passed')
        else:
            print('Failed')