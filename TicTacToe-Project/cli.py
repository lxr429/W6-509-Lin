# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import logging
from logic import make_empty_board, get_winner, other_player

logging.basicConfig(
    filename='logs/game.log',  
    level=logging.INFO,        
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def print_board(board):
    for row in board:
        print(" | ".join(cell if cell is not None else " " for cell in row))
        print("-" * 9)

# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player = 'X'

    logging.info("Game started.")
    
    while winner == None:
        print(f"Player {current_player}'s turn")

        # TODO: Show the board to the user.
        print_board(board)
        logging.info(f"Player {current_player}'s turn")

        # TODO: Input a move from the player.
        row, col = map(int, input("Enter row and column (e.g., 1 2): ").split())
        if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] is not None:
            print("Invalid input. Try again.")
            logging.warning("Invalid input from the player.")
            continue

        # TODO: Update the board.
        board[row - 1][col - 1] = current_player
        logging.info(f"Player {current_player} placed {current_player} at ({row}, {col}).")

        # Check for a winner using get_winner from logic.py
        winner = get_winner(board)
        if winner == 'Draw':
            print_board(board)
            print("It's a draw!")
            logging.info("The game ended in a draw.")
            break
        elif winner:
            print_board(board)
            print(f"Player {winner} wins!")
            logging.info(f"Player {winner} wins the game.")
            break

        # TODO: Update who's turn it is.
        current_player = other_player(current_player)
    
    print_board(board)
    logging.info("Game ended.")
