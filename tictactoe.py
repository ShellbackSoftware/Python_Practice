## Simple tic-tac-toe game that you can play in the terminal
# Board with 9 blank strings in it
board = [" " for i in range(9)]
# Checks for a successful turn
turn_success = True

def print_board():
    output = "\n"
    for i in range(9):
        if i % 3 == 0:
            output += "{} | {} | {}".format(board[i], board[i+1], board[i+2])
            output += "\n"
        else:
            pass
    print(output)

def player_move(icon):
    global turn_success
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print("Your turn, player {}".format(number))
    choice = int(raw_input("Enter your move (1-9):").strip())-1
    if board[choice] == " ":
        board[choice] = icon
        turn_success = True
    else:
        turn_success = False
        print()
        print("That space is taken!")

# Checks for victory
def is_victory(icon):
    for space in range(9):
        if space == 0 or space == 3 or space == 6: # Check for Row win
            if board[space] == board[space+1] == board[space+2] == icon:
                print("Win for player {} on row {}!".format(icon,space))
                return True
        if space == 0 or space == 1 or space == 2: # Check for Column win
            if board[space] == board[space+3] == board[space+6] == icon:
                print("Win for player {} on column {}!".format(icon,space))
                return True
        if space == 0:      # Check for right diagonal win
            if board[space] == board[space+4] == board[space+8] == icon:
                print("Win for {} on diagonal!".format(icon))
                return True
        if space == 2:      # Check for left diagonal win
            if board[space] == board[space+2] == board[space+4] == icon:
                print("Win for {} on diagonal!".format(icon))
                return True
    return False

# Checks for a draw
def is_draw():
    if " " not in board:
        return True
    else:
        return False
        
# "Game Loop"
# Keeps program alive
while True:
    print_board()
    player_move("X")
    while not turn_success:
        player_move("X")
    print_board()
    if is_victory("X"):
        break
    elif is_draw():
        print("Draw! Nobody wins.")
        break
    player_move("O")
    while not turn_success:
        player_move("O")
    if is_victory("O"):
        print_board()
        break
    elif is_draw():
        print("Draw! Nobody wins.")
        break
