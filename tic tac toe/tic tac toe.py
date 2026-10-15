board = [' ' for _ in range(9)]

def display_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False

def check_draw():
    return ' ' not in board

def play_game():
    current_player = 'X'

    while True:
        display_board()

        try:
            position = int(input(f"Player {current_player}, choose a position (1-9): "))
        except ValueError:
            print("Please enter a number.")
            continue

        if position < 1 or position > 9:
            print("Choose a position between 1 and 9.")
            continue

        index = position - 1

        if board[index] != ' ':
            print("That position is already occupied.")
            continue

        board[index] = current_player

        if check_winner(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            break

        if check_draw():
            display_board()
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_game()
