import math
import time

board = [" " for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 9)
    print("\n")

def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  
                      (0, 4, 8), (2, 4, 6)]  
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def is_board_full():
    return " " not in board

def minimax(board, depth, is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_board_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

def play_game():
    print("Welcome to Tic-Tac-Toe AI! You are 'X' and AI is 'O'.")
    print_board()

    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
            else:
                print("Invalid move! Try again.")
                continue
        except (IndexError, ValueError):
            print("Invalid input! Enter a number between 1-9.")
            continue

        print_board()

        if check_winner("X"):
            print("\n🎉 Congratulations! You win!\n")
            break  

        if is_board_full():
            print("\n😮 It's a tie!\n")
            break  

        print("AI is thinking...\n")
        time.sleep(1)
        best_move()
        print_board()

        if check_winner("O"):
            print("\n😢 AI wins! Better luck next time.\n")
            break  

        if is_board_full():
            print("\n😮 It's a tie!\n")
            break  

    print("\nGame Over. Thanks for playing!\n")

if __name__ == "__main__":
    play_game()
