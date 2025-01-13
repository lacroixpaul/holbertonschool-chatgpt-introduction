#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows for winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        
        # Input validation loop for row and column
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                
                # Check if the row and column are within bounds
                if row not in range(3) or col not in range(3):
                    print("Invalid row or column! Please enter values between 0 and 2.")
                    continue
                
                # Check if the spot is taken
                if board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                    continue
                
                break  # If input is valid, break the loop
            except ValueError:
                print("Invalid input! Please enter integers for row and column.")
        
        # Place the player's move
        board[row][col] = player

        # Switch player
        if player == "X":
            player = "O"
        else:
            player = "X"

    # Print the final board and the winner
    print_board(board)
    # Switch the player back to the one who actually won
    if player == "X":
        winner = "O"
    else:
        winner = "X"
    print(f"Player {winner} wins!")

tic_tac_toe()
