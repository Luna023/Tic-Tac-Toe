import os
import random

def draw_board(board):
    """Draw the Tic Tac Toe board"""
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("---|---|---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("---|---|---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])

def check_for_win(board):
    """Check if there's a winner"""
    win_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                      [1, 4, 7], [2, 5, 8], [3, 6, 9],
                      [1, 5, 9], [3, 5, 7]]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True
    return False

def check_turn(turn):
    """Determine the current player's symbol"""
    return 'X' if turn % 2 == 0 else 'O'

def ai_move(board):
    """Generate a random computer move"""
    available_spots = [spot for spot in board if board[spot] not in ['X', 'O']]
    return random.choice(available_spots)


def choose_mode():
    """Function to choose game mode"""
    print("Choose Game Mode:")
    print("1. Play against Computer")
    print("2. Play against another player")
    mode = input("Enter the number of your choice: ")
    while mode not in ['1', '2']:
        mode = input("Invalid input. Please enter 1 or 2: ")
    return int(mode)


spots = {i: str(i) for i in range(1, 10)}
playing = True
turn = 0
prev_turn = -1


mode = choose_mode()


while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)

    if prev_turn == turn:
        print("Invalid spot selected, please pick another.")
    prev_turn = turn

    player_symbol = check_turn(turn)
    if (mode == 1 and player_symbol == 'X') or mode == 2:
        print("Player {}'s turn: Pick your spot (1-9) or press q to quit".format(1 if player_symbol == 'X' else 2))
        choice = input()
        if choice == 'q':
            playing = False
            break
        elif choice.isdigit() and int(choice) in spots:
            if spots[int(choice)] not in {"X", "O"}:
                turn += 1
                spots[int(choice)] = player_symbol
    else:
        print("AI's turn...")
        input("Press Enter to see AI's move...")
        ai_choice = ai_move(spots)
        turn += 1
        spots[ai_choice] = player_symbol

    if check_for_win(spots):
        playing = False

    if turn > 8:
        playing = False

os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

if check_for_win(spots):
    print("Player {} Wins!".format(1 if player_symbol == 'X' else 2))
else:
    print("It's a Tie!")

print("Thanks for playing!")
