"""
File:    proj2.py
Author:  Hamza Qureshi
Date:    04/23/2020
Section: 15
E-mail:  hamz1@umbc.edu
Description:
  Connect 4 game, with 2 players or with computer
"""
# tried to split by x and o, but did not work, so can only use grid with no x/o already entered

class AdjoinTheSpheres:
    def __init__(self):
        self.game_options = []

    def main_menu(self, game_type):

        self.game_options.append(game_type)

    def load_game(self):
        game_file = input('What map do you want to load? ')
        # opening the file and making it readable
        game_file = open(game_file, 'r+')
        lines = game_file.readlines()
    # tried to split by x and o
    #    for element in lines:
    #        if element == 'x' or element == 'o':
    #            element.split('x')
    #            element.split('o')

        self.turn = lines[1]

        # adding all the rows to a list and splitting them
        self.final_board = []
        self.final_board.append(lines[2].strip('\n').split(' '))
        self.final_board.append(lines[3].strip('\n').split(' '))
        self.final_board.append(lines[4].strip('\n').split(' '))
        self.final_board.append(lines[5].strip('\n').split(' '))
        self.final_board.append(lines[6].strip('\n').split(' '))

         # converting all spaces in board to periods
        for row in range(len(self.final_board)):
        # remove last column b/c game board said 7 but had 8
            self.final_board[row].pop()
            for col in range(len(self.final_board[row])):
                if self.final_board[row][col] == '':
                    self.final_board[row][col] = '.'
                    print(self.final_board[row][col], end= '')
            print()
        return self.final_board

    def player_vs_player(self):
        count = 1
        while not self.connect_four():
            if count % 2 > 0:
                player_input = input('Player x What move do you want to make? Answer as Row (vertical) '
                                     'Column (horizontal) or save game or load game: ')

                if player_input == 'load game':
                    self.load_game()
                elif player_input == 'save game':
                    self.save_game()
                else:
                    # converting str to int if move entered
                    move_list = (player_input.split())
                    final_move = []
                    for i in move_list:
                        final_move.append(int(i)-1)
                    move_list = final_move


                # makes sure space is not  forbidden
                if self.final_board[move_list[0]][move_list[1]] == '*':
                    print('That is a forbidden position try again!')
                    player_input = input('Player x What move do you want to make? Answer as Row (vertical) '
                                                'Column (horizontal) or save game or load game: ')
            # makes sure space isnt already taken
                elif self.final_board[move_list[0]][move_list[1]] == 'x' or self.final_board[move_list[0]][move_list[1]] == 'o':
                    print('Space already occupied! Try again')
                    player_input = input(
                        'Player x What move do you want to make? Answer as Row (vertical) '
                                                'Column (horizontal) or save game or load game: ')

                else:
                    count += 1
                    self.final_board[move_list[0]][move_list[1]] = 'x'
                    for row in range(len(self.final_board)):
                        for col in range(len(self.final_board[row])):
                                print(self.final_board[row][col], end='')
                        print()

            elif count % 2 ==  0:
                # converting str to int if move entered
                move_list = (player_input.split())
                final_move = []
                for i in move_list:
                    final_move.append(int(i)-1)
                move_list = final_move

                # makes sure space is not  forbidden
                if self.final_board[move_list[0]][move_list[1]] == '*':
                    print('That is a forbidden position try again!')
                    player_input = input(
                        'Player o What move do you want to make? Answer as Row (vertical) '
                                                 'Column (horizontal) or save game or load game: ')
            # makes sure space isnt already taken
                elif self.final_board[move_list[0]][move_list[1]] == 'x' or self.final_board[move_list[0]][move_list[1]] == 'o':
                    print('Space already occupied! Try again')
                    player_input = input('Player o What move do you want to make? Answer as Row (vertical) '
                                                   'Column (horizontal) or save game or load game: ')

                else:
                    count += 1
                    self.final_board[move_list[0]][move_list[1]] = 'o'
                    for row in range(len(self.final_board)):
                        for col in range(len(self.final_board[row])):
                                print(self.final_board[row][col], end='')
                        print()
        if self.connect_four():
            print('You win')

    def player_vs_computer(self):
        count = 1
        while not self.connect_four():
            if count % 2 > 0:
                player_input = input('Player x What move do you want to make? Answer as Row (vertical) '
                                     'Column (horizontal) or save game or load game: ')

                if player_input == 'load game':
                    self.load_game()
                elif player_input == 'save game':
                    self.save_game()
                else:
                    # converting str to int if move entered
                    move_list = (player_input.split())
                    final_move = []
                    for i in move_list:
                        final_move.append(int(i) - 1)
                    move_list = final_move

                # makes sure space is not  forbidden
                if self.final_board[move_list[0]][move_list[1]] == '*':
                    print('That is a forbidden position try again!')
                    player_input = input(
                        'Player x What move do you want to make? Answer as Row (vertical) '
                                                'Column (horizontal) or save game or load game: ')
                # makes sure space isnt already taken
                elif self.final_board[move_list[0]][move_list[1]] == 'x' or self.final_board[move_list[0]][
                    move_list[1]] == 'o':
                    print('Space already occupied! Try again')
                    player_input = input(
                        'Player x What move do you want to make? Answer as Row (vertical) '
                                                'Column (horizontal) or save game or load game: ')

                else:
                    count += 1
                    self.final_board[move_list[0]][move_list[1]] = 'x'
                    for row in range(len(self.final_board)):
                        for col in range(len(self.final_board[row])):
                            print(self.final_board[row][col], end='')
                        print()

            elif count % 2 == 0:
                from random import randint
                move_list = [randint(0,4), randint(0,6)]

                # makes sure space is not  forbidden
                if self.final_board[move_list[0]][move_list[1]] == '*':
                    print('That is a forbidden position try again!')
                    move_list = [randint(0, 4), randint(0, 6)]
                # makes sure space isnt already taken
                elif self.final_board[move_list[0]][move_list[1]] == 'x' or self.final_board[move_list[0]][move_list[1]] == 'o':
                   print('That space is already taken')
                   move_list = [randint(0, 4), randint(0, 6)]
                else:
                    count += 1
                    self.final_board[move_list[0]][move_list[1]] = 'o'
                    print('Computer turn completed')
                    for row in range(len(self.final_board)):
                        for col in range(len(self.final_board[row])):
                            print(self.final_board[row][col], end='')
                        print()
        if self.connect_four():
            print('You win')

    def save_game(self):
        pass

    def connect_four(self):
        # check for connect 4 horizontally and vertically
        for row in range(len(self.final_board)):
            for col in range(len(self.final_board[row])):
                if 'x x x x' in self.final_board[row][col] or 'o o o o' in self.final_board[row][col]:
                    self.winner = "You win"
                    return self.winner


    def play_game(self):
        # adding game options to menu
        print('AdjoinTheSpheres Main Menu')
        print(self.game_options[0])
        print(self.game_options[1])
        print(self.game_options[2])
        # input validation for menu
        options = int(input('Select option from the menu: '))
        while options != 1 and options != 2 and options != 3:
            print('Please select a valid option from the menu')
            options = int(input('Select an option from the menu: '))
        # calls load_game function
        if options == 1 or options == 2:
            # self.game_file = input('What map do you want to load? ')
            self.load_game()

        if options == 1:
            self.player_vs_player()
        elif options == 2:
            self.player_vs_computer()

if __name__ == "__main__":

    game_1 = AdjoinTheSpheres()
    game_1.main_menu( '1.) New game (2 Players)')
    game_1.main_menu( '2.) New Game (Player vs Computer)')
    game_1.main_menu( '3.) Exit Game')
    game_1.play_game()