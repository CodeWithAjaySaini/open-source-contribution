import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if any player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full (tie)
def check_tie(board):
    return all([spot != ' ' for row in board for spot in row])

# Function to get player's move
def player_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            row, col = divmod(int(move) - 1, 3)
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("That spot is already taken. Try again.")
        else:
            print("Invalid input! Enter a number between 1 and 9.")

# Function for the computer's move
def computer_move(board):
    available_moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    move = random.choice(available_moves)
    board[move[0]][move[1]] = 'O'

# Main function to run the game
def tic_tac_toe():
    # Initialize empty board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        # Player's move
        player_move(board)
        print_board(board)
        
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if check_tie(board):
            print("It's a tie!")
            break
        
        # Computer's move
        computer_move(board)
        print("Computer's move:")
        print_board(board)
        
        if check_winner(board, 'O'):
            print("Computer wins!")
            break
        if check_tie(board):
            print("It's a tie!")
            break

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
