# ---Global Variables---
game_still_going = True
winner = None
current_player = 'X'


# CREATING BOARD
board = ['-', '-','-',
         '-','-','-',
         '-','-','-']


# DISPLAING BOARD
def display_board():
   
            
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

    






# HANDLING PLAYER'S TURN
def handle_turn(player):
     

    print(player+"'s turn")

    # TAKING INDEX POSITION FROM USER
    position = (input("Enter a position from 1-9 => "))

    # HANDLING ERROR FROM USER
    valid = False
    while not valid:


        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Not a valid input enter again")
            position = (input("Enter a valid command between 1-9=>"))
            
        try:


            
            position = int(position)
        except:
            print("Wrong input! try again")
            play_game()
        position = position-1

        if board[position] == '-':
            valid = True
        else:
            print("You cant go there! Try again")


    # GETTING USER'S POSITION
    board[position] = player
    display_board()
    


# USING ALL FUNCTIONALITY IN PLAY GAME FUNCTION
def play_game():

    # checking for empty space in board

    


    display_board()

    
    
    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()
        flip_player()

    
    # SHOWING WINNER'S RESULT
    if winner == 'X' or winner == 'O':
        print(winner + " Won")

    elif winner == None:
        print("Game tied")

    
# CHECKINH FOE GAME IS STILL IN THE PROGRESS OR NOT
def check_if_game_over():


    check_win()
    check_tie()


# CHECKING FOR THE WINNER
def check_win():
    global winner
    # CHECK ROWS
    row_winner = check_rows()
    

    # CHECK COLUMNS
    column_winner = check_columns()
    # CHECK DIAGONAL
    diagonal_winner = check_diagonals()
    
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# CHECKING FOR THE ROW WINNER IN ROWS
def check_rows():
    # GETTING GLOBAL VARIABLE
    global game_still_going
    
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    if row1 or row2 or row3:
        game_still_going = False

    if row1:
        return board[0]

    elif row2:
        return board[3]

    elif row3:
        return board[6]

    return
    
    

    


# CHECKING FOR THE WINNER IN THE COLUMNS
def check_columns():
    global game_still_going

    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'

    if column1 or column2 or column3:
        game_still_going = False

    if column1:
        return board[0]

    elif column2:
        return board[1]

    elif column3:
        return board[2]
    
    

  
    
# CHECKING FOR THE WINNER IN DIAGONALS
def check_diagonals():
    global game_still_going
    diagonal1 = board[2] == board[4] == board[6] != '-'
    diagonal2 = board[0] == board[4] == board[8] != '-'
    if diagonal1 or diagonal2:
        game_still_going = False
    if diagonal1:
        return board[2]

    elif diagonal2:
        return board[0]

    
# HANDLING PLAYER'S TURN OR SWITCHING PLAYER
def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'

# CHECKING FOR  A TIE

def check_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False
        return True
    else:
        return False


play_game()