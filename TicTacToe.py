#below is the code for TicTacToe
board=["-","-","-",
	   "-","-","-",
	   "-","-","-"]

game_continues = True

Winner = None 

#Allow us to know who is the current player
current_player = "X"

#Set a a 3x3 grid with empty slots in the beginning
def display_board():
	print(board[0]+"|" +board[1]+"|" +board[2]+"|")
	print(board[3]+"|" +board[4]+"|" +board[5]+"|")
	print(board[6]+"|" +board[7]+"|" +board[8]+"|")


#Game Logic
def play_game():

	display_board()

	#A loop to keep the game going 
	while game_continues:
		handle_turn(current_player)
		
		#fcn that determines gmae is over
		game_over()
		#Flip to other player
		flip_players()
	#check if the game is over.Needs to break out of the loop
	if winner =="X" or winner == "O":
		print(winner + "won !")
	elif winner == None:
		print("Tie game.")
	
#handle a single turn of a arbitrary player
def handle_turn(player):
	#prompt the user to choose a spot out of 9
	position = input("Choose a position from 1-9: ")
	

	#Exceptions
	player_logic = False
	while not player_logic:
		while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			position =input("choose a postion from 1-9")

		#-1 as python index from 0
		position = int(position) - 1

		if board[position] =="-":
			player_logic = True
		else:
			print("It's taken, get to a different position")

	board[position] = player

	display_board()

def game_over():

	check_win()
	check_tie()

def check_win():
	#check rows
	row_winner = checkrows()
	


	#check columns
	column_winner = checkcolumns()




	#check diagonal
	diawinner = checkdiagonals()

	if row_winner:
		winner = row_winner
	elif column_winner:
		winner = column_winner
	elif diawinner:
		winner = diawinner
	else:
		winner = None

	return False

def check_tie():
	#global variable 
	global game_continues
	if "-" not in board:
		game_continues = False
		return True
	else:	
		return False

#to allow the next player to choose a position, alternative "O"/"X".
def flip_players():

	global current_player

	if current_player =="X":
		current_player ="O"
	elif current_player =="O":
		current_player = "X"

def checkrows():
    global game_continues
    
    row_1 = board[0] == board[1] == board[2] != "-"

    row_2 = board[3] == board[4] == board[5] != "-"

    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_continues = False
 	#indicates which row makes a winner
    if row_1:
        return board[0]	

    elif row_2:
        return board[3] 

    elif row_3:
        return board[6] 
    else:
        return None

def checkdiagonals():

	global game_continues
	diagonal_1 = board[0] == board[4] == board[8] != "-"
	diagonal_2 = board[2] == board[4] == board[6] != "-"
	if diagonal_1 or diagonal_2:
		game_continues
	if diagonal_1:
		return board[0]
	if diagonal_2:
		return board[2]
	else:
		return False

def checkcolumns():
	global game_continues

	column_1 = board[0] == board[3] == board[6] != "-"

	column_2 = board[1] == board[4] == board[7] != "-"

	column_3 = board[2] == board[5] == board[8] != "-"

	if column_1 or column_2 or column_3:
		game_still_going = False
	if column_1:
	    return board[0]	
	elif column_2:
	    return board[1] 

	elif column_3:
	    return board[3] 
	else:
	    return None
play_game()