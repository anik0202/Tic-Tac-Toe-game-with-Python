#from IPython.display import clear_output
import random

def display_board(board):
    print('    |   |')
    print('  ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('    |   |')
    print('-------------')
    print('    |   |')
    print('  ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('    |   |')
    print('-------------')
    print('    |   |')
    print('  ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('    |   |')
    





def player_input():
    
    choice = 'WRONG'
    while choice not in ['X', 'O']:
        choice = input('Player 1: Do you want to be X or O?: ').upper()
        if choice == 'X':
            print('Player 1: You are X')
            return ('X', 'O')
        elif choice == 'O':
            print('Player 1: You are O')
            return ('O', 'X')
        else:
            print('Please input a valid choice (X or O)')




def win_check(board, mark):
    
    
    if( board[0] == board[1] == board[2] == mark) or \
       ( board[3] == board[4] == board[5] == mark) or \
       ( board[6] == board[7] == board[8] == mark) or \
       ( board[0] == board[3] == board[6] == mark) or \
       ( board[1] == board[4] == board[7] == mark) or \
       ( board[2] == board[5] == board[8] == mark) or \
       ( board[0] == board[4] == board[8] == mark) or \
       ( board[2] == board[4] == board[6] == mark):
        return True
    else:
        return False




def choose_first():
    first_player = random.randint(1,2)
    if first_player == 1: 
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    
    if board[position - 1] == ' ':
        return True
    else:
        return False

def full_board_check(board):
    
    for i in range(0,9):
        if board[i] == ' ':
            return True
    else: 
        return False
        

def place_marker(board, marker, position):
    
    board[position-1] = marker
    


def player_choice(board):
    
    choice = True
    while choice == True:
        
        position = int(input('Enter the next position to place your marker (1,9): '))
        if position in range(1,10):
            if space_check(board, position):
                return position
            else:
                print('This position is already taken. Please choose another position.')
        else:
            print('Please input a valid position (1-9)')

def replay():
    
    choice = ''
    while choice not in ['Y', 'N']:
        choice = (input('Do you want to play again? (Y/N): ')).upper()
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            print('Please enter a valid choice (Y/N)')




while True:
    #clear_output()
    # Set the game up here
    board = [' ']*9
    
    display_board(board) # Display the initial board that has just been created
    
    p1_marker, p2_marker = player_input() # Ask player 1 to choose X or O
    
    turn = choose_first() # Randomly choose which player goes first
    
    game_on = True # Set the game to be on
    while game_on:

        if turn == 'Player 1':
            #Player 1 Turn
            if full_board_check(board):
                print("It's Player 1's turn")
                display_board(board) # Show the board
                position = player_choice(board) # Ask player 1 to choose a position on the board
                place_marker(board, p1_marker, position) # Place the marker on the board
                turn = 'Player 2'
                if win_check(board, p1_marker):
                    print('Player 1 wins!!')
                    break
            else:
                display_board(board)
                print("It's a TIE!!")
                break
        else:
            #Player2's turn.
            if full_board_check(board):
                print("It's Player 2's turn")
                display_board(board) # Show the board
                position = player_choice(board) # Ask player 2 to choose a position on the board
                place_marker(board, p2_marker, position) # Place the marker on the board
                turn = 'Player 1'
                if win_check(board, p2_marker):
                    print('Player 2 wins!!')
                    break
            else:
                display_board(board)
                print("It's a TIE!!")
                break



            #pass
    if not replay():
        break