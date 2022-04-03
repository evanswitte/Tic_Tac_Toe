# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Import
import os
import random
import sys
import time as tm

from termcolor import colored, cprint
from tqdm import tqdm

# List to check numbers that are entered
exclusion_list =[]

# Gameboard list
game_board = ["*","1","2","3","4","5","6","7","8","9"]

# List to check which only numbers got entered
allowed_input = ["1","2","3","4","5","6","7","8","9"]

# Enter your game name
player1 = colored(input(f" What is your name " + colored("player 1", "red") + " ? "), "red")
player2 = colored(input(f" What is your name " + colored("player 2", "green") + " ? "), "green")


# Function for displaying the board
''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''
    
def display_board(board):
    print(board[1]+" | " +board[2]+" | "+board[3])
    print('- + - + -')
    print(board[4]+" | " +board[5]+" | "+board[6])
    print('- + - + -')
    print(board[7]+" | " +board[8]+" | "+board[9])


# Function for Player name

def player_input():
    player1_marker = colored("X","red")
    player2_marker = colored("O","green")
    
    # cprint(f"{player1}","red") + cprint(f"your marker is {player1_marker}")
    cprint(f"{player1} your marker is {player1_marker}","red")
    
    cprint(f"{player2} your marker is {player2_marker}","green")
    
    return(player1_marker,player2_marker)


# Input from player1
def player1_input():
    choice = input(f"{player1} please enter a number: ")
    
    if choice in game_board:
        exclusion_list.append(choice)
        game_board[int(choice)] = colored("X","red")
    elif choice in exclusion_list:
        while choice in exclusion_list:
            choice = input("Already chosen! Please choose another number: ")
            while choice not in allowed_input:
                choice = input("Please enter a Number from [1-9]: ")
        exclusion_list.append(choice)       
        game_board[int(choice)] = colored("X","red")
            
    else:
        while choice not in allowed_input:
            choice = input("Please enter a Number from [1-9]: ")
            while choice in exclusion_list:
                choice = input("Already chosen! Please choose another number: ")
        exclusion_list.append(choice)
        game_board[int(choice)] = colored("X","red")


# Input from player2          
def player2_input():
    choice = input(f"{player2} please enter a number: ")
    
    if choice in game_board:
        exclusion_list.append(choice)
        game_board[int(choice)] = colored("O","green")
    elif choice in exclusion_list:
        while choice in exclusion_list:
            choice = input("Already chosen! Please choose another number: ")
            while choice not in allowed_input:
                choice = input("Please enter a Number from 1-9: ")
        exclusion_list.append(choice)       
        game_board[int(choice)] = colored("O","green")
            
    else:
        while choice not in allowed_input:
            choice = input("Please enter a Number from 1-9: ")
            while choice in exclusion_list:
                choice = input("Already chosen! Please choose another number: ")
        exclusion_list.append(choice)
        game_board[int(choice)] = colored("O","green")
        
# Player turn use random like a flip coin
def player_turn():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return player2
    else:
        return player1

# Win check
def win_check(board,mark):
    
    return((board[1] == mark and board[2] == mark and board[3] == mark) or #across the top
           (board[4] == mark and board[5] == mark and board[6] == mark) or #across the middle
           (board[7] == mark and board[8] == mark and board[9] == mark) or #across the bottom
           (board[1] == mark and board[4] == mark and board[7] == mark) or #down left
           (board[2] == mark and board[5] == mark and board[8] == mark) or #down middle 
           (board[3] == mark and board[6] == mark and board[9] == mark) or # down right
           (board[1] == mark and board[5] == mark and board[9] == mark) or #diagonal
           (board[7] == mark and board[5] == mark and board[3] == mark))  #diagonal
    
# Function to print the score-board
def print_scoreboard(score_board):
    print("--------------------------------")
    print("            SCOREBOARD       ")
    print("--------------------------------")
 
    players = list(score_board.keys())
    print("   ", players[0], "    ", score_board[players[0]])
    print("   ", players[1], "    ", score_board[players[1]])
 
    print("--------------------------------\n")

# Stores the scoreboard
score_board = {player1: 0, player2: 0}

# Asking for a new game Y/N
def restart_the_game():
    del game_board[:]
    game_board.extend(["*","1","2","3","4","5","6","7","8","9"])
    del exclusion_list[:]
    restart = input("In mood for another round. Enter y or n: ")
    
    if restart.lower() == "y":
        pass
    elif restart.lower() == "n":
        quit()


# Tic-tac-toe game
# Now we'll write the main function which has all the gameplay functionality.
if __name__ == "__main__":


    # Start a new round of Tic-tac-toe
    cprint('\033[1m' + 'WELCOME TO A NEW ROUND OF TIC-TAC-TOE!' + '\033[0m', 'yellow', 'on_magenta')
 
    
    # Loading bar until the game begins until the game begins
    for i in tqdm(range(100)):
        tm.sleep(0.003)
    
def play_round():
     
    player1_marker,player2_marker = player_input()
    
    turn = player_turn()
    
    
    
    while True:
      
        
        if turn == player1:
            
            display_board(game_board)
            
            player1_input()

            if win_check(game_board,player1_marker):
                display_board(game_board)
                cprint(f"CONGRATULATIONS!!! {player1} you won!","red")
                score_board[player1] += 1
                print_scoreboard(score_board)
                restart_the_game()
            elif len(exclusion_list) == 9:
                print("It's a Tie!!")
                print_scoreboard(score_board)
                restart_the_game()
            else:
                turn = player2   
            
        else:
            display_board(game_board)
            
            player2_input()
            
            if win_check(game_board,player2_marker):
                display_board(game_board)
                cprint(f"CONGRATULATIONS!!! {player2} you won!","green")
                score_board[player2] += 1
                print_scoreboard(score_board)
                restart_the_game()
            elif len(exclusion_list) == 9:
                print("It's a Tie!!")
                print_scoreboard(score_board)
                restart_the_game()
            else:
                turn = player1

play_round()

