def ai_move(board):
    # Step 1: Check if AI can win
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                if check_win(board, 'X'):
                    return i, j
                board[i][j] = ' '

    # Step 2: Block opponent from winning
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                if check_win(board, 'O'):
                    return i, j
                board[i][j] = ' '

    # Step 3: Take center or corner
    if board[1][1] == ' ':
        return 1, 1
    for i, j in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if board[i][j] == ' ':
            return i, j

    # Step 4: Random move
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return i, j

def check_win(board, player):
    # This function checks if the given player has won
    for i in range(3):
        if all(board[i][j] == player for j in range(3)): return True
        if all(board[j][i] == player for j in range(3)): return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    while True:
        print_board(board)
        
        # Player's move (human)
        row, col = map(int, input("Enter your move (row and col): ").split())
        if board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue
        board[row][col] = 'O'
        
        if check_win(board, 'O'):
            print_board(board)
            print("You win!")
            break
        
        # AI's move
        ai_row, ai_col = ai_move(board)
        board[ai_row][ai_col] = 'X'
        
        if check_win(board, 'X'):
            print_board(board)
            print("AI wins!")
            break
        
        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()