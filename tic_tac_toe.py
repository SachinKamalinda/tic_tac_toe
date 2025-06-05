import sys
class TicTacToe:
#initialize the game with session statistics and current player
    def __init__(self):
        self.player1_wins = 0
        self.player2_wins = 0
        self.draws = 0
        self.session_count = self.load_session_count()  
        self.current_player = 'Player 1' 
#generate board
    def generate_board(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]
#confirm spot
    def confirm_spot(self, row, col, player):
        marker = 'O' if player == 'Player 1' else 'X'
        if self.board[row][col] == '-':
            self.board[row][col] = marker
        else:
            print("Spot already chosen. Choose another spot.")
            return False
        return True

#check if player win
    def is_player_win(self, player):
        marker = 'O' if player == 'Player 1' else 'X'
        n = len(self.board)
# Check all rows and columns
        for i in range(n):
            if all(self.board[i][j] == marker for j in range(n)) or \
               all(self.board[j][i] == marker for j in range(n)):
                return True

# Check all diagonals
        if all(self.board[i][i] == marker for i in range(n)) or \
           all(self.board[i][n - 1 - i] == marker for i in range(n)):
            return True

        return False
#check if board full
    def is_board_full(self):
        for row in self.board:
            if '-' in row:
                return False
        return True
#change player turn
    def change_player_turn(self):
        self.current_player = 'Player 2' if self.current_player == 'Player 1' else 'Player 1'
#show the board
    def show_board(self):
        for row in self.board:
            print(" ".join(row))
        print()
#save game stats to text file
    def save_session_stats(self):
        filename = f"session_{self.session_count}_stats.txt"
        with open(filename, 'w') as f:
            f.write(f"Player 1 Wins: {self.player1_wins}\n")
            f.write(f"Player 2 Wins: {self.player2_wins}\n")
            f.write(f"Draws: {self.draws}\n")
        print(f"Session {self.session_count} statistics saved to {filename}")
#load session count
    def load_session_count(self):
        try:
            with open("session_count.txt", "r") as f:
                return int(f.read().strip())
        except FileNotFoundError:
            return 1  
#save session count to text file
    def save_session_count(self):
        with open("session_count.txt", "w") as f:
            f.write(str(self.session_count + 1))  
#start the game
    def start(self):
        while True:
            self.generate_board()  
# Start with Player 1
            self.current_player = 'Player 1'  
            while True:
                print(f"{self.current_player}'s turn")
                self.show_board()

                try:
                    row, col = list(map(int, input(f"Enter row and column numbers to fix spot for {self.current_player} (1-3): ").split()))
                except ValueError:
                    print("Invalid input. Please enter two integers separated by space.")
                    continue
# when spot already chosen then continue to next iteration
                if 1 <= row <= 3 and 1 <= col <= 3:
                    if not self.confirm_spot(row - 1, col - 1, self.current_player):
                        continue  
                else:
                    print("Row and column numbers should be between 1 and 3.")
                    continue

                if self.is_player_win(self.current_player):
                    print(f"{self.current_player} wins the game!")
                    if self.current_player == 'Player 1':
                        self.player1_wins += 1
                    else:
                        self.player2_wins += 1
                    break

                if self.is_board_full():
                    print("Match Draw!")
                    self.draws += 1
                    break

                self.change_player_turn()

 # Check if the player wants to exit the game
                exit_choice = input("Enter 'exit' to leave the game, or press Enter to continue: ").lower()
                if exit_choice == 'exit':
                    self.save_session_stats()
                    self.save_session_count()
                    sys.exit("Exiting the game.")

            self.show_board()
            self.save_session_stats()
            self.save_session_count()  
#check if player want start new game
            choice = input("Do you want to start another game in this session? (yes/no): ").lower()
            if choice != 'yes':
                break
