#tic tac toe game :)
import random

def display_board(board):
    print('************')
    print(f" {board[7]} | {board[8]} | {board[9]}")
    print("--- --- ---")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print("--- --- ---")
    print(f" {board[1]} | {board[2]} | {board[3]}\n")


    
def player_input():
    user_input = 0
    while user_input < 1 or user_input > 9:
        user_input = int(input("Please enter desired position index (numbers 1 - 9) : >> "))
        if user_input < 1 or user_input > 9:
            print("Position invalid!")
    return user_input

def place_marker(board, marker, position):
    board[position] = marker
    
def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    if board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    if board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    if board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    if board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    if board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    if board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    if board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    
    return False
   
def choose_first_player():
    num = random.randint(0, 10)
    if num < 5:
        return "Player 1"
    else:
        return "Player 2"
    
def space_check(board, position):
    if board[position] == "O" or board[position] == "X":
        return False
    else:
        return True
    
def full_board_check(board):
    for x in range(len(board)):
        if x > 0:
            free_space = space_check(board, x)
            if free_space:
                return False
    return True

def player_choice(board):
    player_choice = player_input()
    while not space_check(board, player_choice):
        print("\nPosition is not available!\n")
        player_choice = player_input()
        
    return player_choice

def replay():
    replay =  str(input("Do you want to play again? (Yes or No) : ")).lower()
    
    while (not replay == "yes") and (not replay == "no"):
        print("\nInvalid Choice! Please type ('yes' or 'no')\n")
        replay =  str(input("Do you want to play again? (Yes or No) : ")).lower()
        
    return replay

def play_game():
    Player_1 = 'X'
    Player_2 = 'O'
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    print('Welcome to Tic Tac Toe!')

    print("Player 1 = " + Player_1 + ", Player 2 = " + Player_2)
    display_board(board)
    player_turn = choose_first_player()
    
    print(f"<<{player_turn} goes first!>>")
    while not full_board_check(board):      
        
        if player_turn == "Player 1":
            print("\nIt's Player 1 Turn!")
            choice = player_choice(board)
            place_marker(board, Player_1, choice)
            print("Player 1 = " + Player_1 + ", Player 2 = " + Player_2)
            display_board(board)
            player_turn = "Player 2"
            if win_check(board, Player_1):
                print("\nPlayer 1 Won!!!")
                break
                        
        if player_turn == "Player 2":
            print("\nIt's Player 2 Turn!")
            choice = player_choice(board)
            place_marker(board, Player_2, choice)
            print("Player 1 = " + Player_1 + ", Player 2 = " + Player_2)
            display_board(board)
            player_turn = "Player 1"
            if win_check(board, Player_2):
                print("\nPlayer 2 Won!!!")
                break

    while replay() == "yes":
        play_game()

if __name__ == '__main__':
    play_game()
