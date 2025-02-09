# This function makes the AI's move
def ai_move(board):
    # Step 1: Check if the AI can win on its next move
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':  # Only consider empty spots
                board[row][col] = 'X'   # Temporarily place the AI's move
                if check_win(board, 'X'):  # Check if AI wins with this move
                    return row, col      # Return the winning move
                board[row][col] = ' '  # Reset the spot if it doesn't win

    # Step 2: Block the opponent from winning
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':  # Only consider empty spots
                board[row][col] = 'O'   # Temporarily place the opponent's move
                if check_win(board, 'O'):  # Check if the opponent wins
                    return row, col      # Block the opponent's move
                board[row][col] = ' '  # Reset the spot if it doesn't block

    # Step 3: Take the center position if it's free
    if board[1][1] == ' ':
        return 1, 1  # Return the center if it's empty

    # Step 4: Try to take a corner if it's free
    for row, col in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if board[row][col] == ' ':
            return row, col  # Return any free corner

    # Step 5: Choose a random spot if no strategic moves are available
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return row, col  # Return any free spot

# This function checks if a player has won the game
def check_win(board, player):
    # Check all rows for a win
    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            return True  # Return True if any row has all same player pieces

    # Check all columns for a win
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True  # Return True if any column has all same player pieces

    # Check the diagonal from top-left to bottom-right
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    # Check the diagonal from top-right to bottom-left
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False  # Return False if no winning condition is met

# This function prints the board in a user-friendly way
def print_board(board):
    for row in board:
        print(' | '.join(row))  # Join each row's items with a separator
        print('-' * 5)  # Print a line after each row

# This function starts the game and lets the human and AI take turns
def main():
    # Create an empty 3x3 game board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    # The game loop, which keeps going until someone wins or it's a draw
    while True:
        print_board(board)  # Display the current game board
        
        # Ask the player (human) to make a move
        row, col = map(int, input("Enter your move (row and col, 0-based index): ").split())
        
        # Check if the chosen spot is available
        if board[row][col] != ' ':
            print("Invalid move! The spot is already taken.")
            continue  # Ask for another move if the spot is already taken
        
        # Place the player's move on the board
        board[row][col] = 'O'

        # Check if the player has won
        if check_win(board, 'O'):
            print_board(board)
            print("Congratulations! You win!")  # The player wins
            break

        # If the board is full and no one has won, it's a draw
        if all(board[row][col] != ' ' for row in range(3) for col in range(3)):
            print_board(board)
            print("It's a draw!")  # The game ends in a draw
            break

        # AI makes its move
        ai_row, ai_col = ai_move(board)  # Get AI's next move
        board[ai_row][ai_col] = 'X'  # Place the AI's move

        # Check if the AI has won
        if check_win(board, 'X'):
            print_board(board)
            print("Sorry, the AI wins!")  # AI wins
            break

# Start the game
if __name__ == "__main__":
    main()
