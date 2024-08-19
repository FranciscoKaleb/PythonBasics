# Tic-Tac-Toe

# Create the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('---------')
    for i in range(3):
        row = '| '.join(board[i * 3:(i * 3) + 3])
        print(f'| {row} |')
        print('---------')

# Function to check for a win
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to check for a draw
def check_draw():
    return ' ' not in board

# Function to make a move
def make_move(player, position):
    if board[position] == ' ':
        board[position] = player
        return True
    else:
        return False

# Function to play the game
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()

        valid_move = False
        while not valid_move:
            position = int(input(f"Player {current_player}, enter your move (0-8): "))
            valid_move = make_move(current_player, position)
            if not valid_move:
                print("Invalid move. Try again.")

        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_draw():
            print_board()
            print("It's a draw!")
            game_over = True

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()