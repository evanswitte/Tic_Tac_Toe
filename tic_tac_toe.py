# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for displaying the board
exclusion_list = []
game_board = ['1','2','3','4','5','6','7','8','9']
backup_list = ["1","2","3","4","5","6","7","8","9"]

def board_game_display():   
    print("---------------")
    print(game_board[0:3])
    print(game_board[3:6])
    print(game_board[6:10])
    print("---------------")

# Function for resstart
def restart_the_game():
    restart = input("In the mood for another round (y/n)")

    if restart == "y" or restart == "Y":
        board_game_display()
        play_round()
    elif restart == "n" or restart == "N":
        exit()

# Function to play
def play_round():
    input_name_p1 = input('Player 1, please enter your nickname: ')
    input_name_p2 = input('Player 2, please enter your nickname: ')
    board_game_display()
    turn_counter = 1
    game_ongoing = True
    while game_ongoing == True:
        
        if turn_counter %2 != 0:
                input_player1 = input("{} its your turn.You are X. To place your X, pick a number on the board.".format(input_name_p1))

                while input_player1 not in backup_list:
                      input_player1 = input("We are asking for NUMBERS between 1 and 9, {}. Please, try again.".format(input_name_p1))
                      
                      if input_player1 in backup_list:
                          continue
                
                
                while int(input_player1) in exclusion_list: 
                    input_player1 = input("Please chose a different number.")
                
                else:
                    exclusion_list.append(int(input_player1))
                    game_board[int(input_player1)-1] = 'X'
                    turn_counter +=1
                    
                if (game_board[0] == game_board[1] == game_board[2]) == True or \
                    (game_board[3] == game_board[4] == game_board[5]) == True or \
                    (game_board[6] == game_board[7] == game_board[8]) == True or \
                    (game_board[0] == game_board[3] == game_board[6]) == True or \
                    (game_board[1] == game_board[4] == game_board[7]) == True or \
                    (game_board[2] == game_board[5] == game_board[8]) == True or \
                    (game_board[0] == game_board[4] == game_board[8]) == True or \
                    (game_board[2] == game_board[4] == game_board[6]) == True:
            
                    if turn_counter % 2 == 0:
                        print("{} has won the game and is the new CHAMPION".format(input_name_p1))
                    else:
                        print("{} has won the game and is the new CHAMPION".format(input_name_p2))
                    game_ongoing = False

                elif len(exclusion_list) == 9:
                     print("It's a draw")
                     game_ongoing = False
              
                board_game_display()
                

        else:
            input_player2 = input("{} its your turn.You are X. To place your X, pick a number on the board.".format(input_name_p2))

            while input_player2 not in backup_list:
                      input_player2 = input("We are asking for NUMBERS between 1 and 9, {}. Please, try again.".format(input_name_p2))
                      
                      if input_player2 in backup_list:
                          continue 

            while int(input_player2) in exclusion_list: 
                input_player2 = input("Please chose a different number.")


            else:
                exclusion_list.append(int(input_player2))
                game_board[int(input_player2)-1] = 'O'
                turn_counter += 1

                if (game_board[0] == game_board[1] == game_board[2]) == True or \
                    (game_board[3] == game_board[4] == game_board[5]) == True or \
                    (game_board[6] == game_board[7] == game_board[8]) == True or \
                    (game_board[0] == game_board[3] == game_board[6]) == True or \
                    (game_board[1] == game_board[4] == game_board[7]) == True or \
                    (game_board[2] == game_board[5] == game_board[8]) == True or \
                    (game_board[0] == game_board[4] == game_board[8]) == True or \
                    (game_board[2] == game_board[4] == game_board[6]) == True:
            
                    if turn_counter % 2 != 0:
                        print("{} has won the game and is the new CHAMPION".format(input_name_p2))
                    else:
                        print("{} has won the game and is the new CHAMPION".format(input_name_p1))
                    game_ongoing = False

                elif len(exclusion_list) == 9:
                    print("It's a draw")
                    game_ongoing = False
              
            board_game_display()

    del game_board[:]
    game_board.extend(['1','2','3','4','5','6','7','8','9'])
    del exclusion_list[:]
    restart_the_game()


# Tic-tac-toe game
if __name__ == "__main__":
    exclusion_list = []
    game_board = ['1','2','3','4','5','6','7','8','9']
    backup_list = ["1","2","3","4","5","6","7","8","9"]
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    print("Let's start the game who will be tic tac toe master \n" 'the king of the jungle\n''ruler of the seas \n''world champion \n and master of every tic tac toe board '.upper())
    play_round()

