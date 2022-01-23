## PSEUDOCODE:

__PART 0__

* CREATE game_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
* CREATE exclusion_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] #to make sure players don't overwrite the others
* CREATE turn_counter = [...] #to determine whose turn it is and who has won<
* OUTPUT game_board

__PART 1__ 

* OUTPUT "Player 1 it's your turn. 
* You are X. To place your X, pick a number on the board."
* INPUT player1 enters a number between 1-9
* IF number in exclusion_list
* OUTPUT "Please chose a different number."
* ELSE
* ADD 1 to turn_counter
* GAME PLACES X game_board[num - 1] = "X"
* STORE number in exclusion_list
* OUTPUT game_board

__PART 2__

* CHECK if row, column or diagonal has three of the same symbol
* IF one returns TRUE
* END game (break), def winner - if turn_count % 2 != 0 -> player1, else player2
* OUTPUT "(Winner) has won the game"
* ELIF 
* CHECK if len(exclusion_list)==9
* END game (break), 
* OUTPUT "It's a draw."
* ELSE continue with next player

__PART 3__

* OUTPUT "Player 2 it's your turn. 
* You are O. To place your O, pick a number on the board."
* INPUT player2 enters a number between 1-9
* IF number in exclusion_list
* OUTPUT "Please chose a different number."
* ELSE 
* ADD 1 to turn_counter
* GAME PLACES X game_board[num - 1] = "O"
* STORE number in exclusion_list
* OUTPUT game_board

__REPEAT PARTS 1-3 UNTIL PART 2 breaks__

__IMPLEMENTATION PLAN:__ <br>
The implementation workflow for this project is as follows:

<img src="https://github.com/neuefische/muc-analytics-21-1-daily-review/blob/main/media/Advanced_Decision_Tree.png" width=50% height=50%>
