import os
import time

# the idea of the minimax algorithm is to maximise the minimum gain, while alpha-beta reduces the number of moves searched by only examining moves that are better than the current best move
class TicTacToe:
    def __init__(self, turn, assist):
        '''Setup the board and moves.'''
        if turn:
            self.player, self.ai, self.next = "X", "O", "X"
        else:
            self.player, self.ai, self.next = "O", "X", "X"
        self.board = [["*" for i in range(3)] for j in range(3)]
        self.assist = assist

    def check(self, x, y):
        '''Check if a move is valid.'''
        return 0 <= x <= 2 and 0 <= y <= 2 and self.board[x][y] == "*"

    def display(self):
        '''Print a formatted board.'''
        print("_____")
        for i in range(3):
            print("|" + "".join(self.board[i]) + "|")
        print("_____")

    def max_res(self, a, b):
        '''Optimal move for the AI.'''
        best, x, y = -float("inf"), -1, -1
        result = self.win()
        if result == self.player:
            return (-1, x, y)
        if result == self.ai:
            return (1, x, y)
        if result == "*":
            return (0, x, y)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "*":
                    self.board[i][j] = self.ai
                    new_best = self.min_res(a, b)[0]
                    if new_best > best:
                        best, x, y = new_best, i, j
                    self.board[i][j] = "*"
                    if best >= b:
                        return best, x, y
                    a = max(best, a)
        return best, x, y

    def min_res(self, a, b):
        '''Optimal move for the player.'''
        worst, x, y = float("inf"), -1, -1
        result = self.win()
        if result == self.player:
            return (-1, x, y)
        if result == self.ai:
            return (1, x, y)
        if result == "*":
            return (0, x, y)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "*":
                    self.board[i][j] = self.player
                    new_worst = self.max_res(a, b)[0]
                    if new_worst < worst:
                        worst, x, y = new_worst, i, j
                    self.board[i][j] = "*"
                    if worst <= a:
                        return worst, x, y
                    b = min(worst, b)
        return worst, x, y

    def start(self):
        '''Actually play the game.'''
        while True:
            self.display()
            result = self.win()
            if result:
                if result == self.player:
                    print("You played well and won!")
                elif result == self.ai:
                    print("Better luck next time!")
                elif result == "*":
                    print("We're too evenly matched!")
                return
            if self.player == self.next:
                if self.assist:
                    start = time.time()
                    temp, x, y = self.min_res(-float("inf"), float("inf"))
                    print(f"Recommend moving ({x}, {y}), used {time.time() - start}s.")
                while True:
                    x, y = map(int, input("Enter (x, y) separated by a space. ").split())
                    if self.check(x, y):
                        self.board[x][y] = self.player
                        self.next = self.ai
                        break
                    else:
                        print("Invalid move, please try again.")
            else:
                start = time.time()
                temp, x, y = self.max_res(-float("inf"), float("inf"))
                print(f"Moved to ({x}, {y}), used {time.time() - start}s.")
                self.board[x][y] = self.ai
                self.next = self.player

    def win(self):
        '''Check if the player or AI won.'''
        positions = [[self.board[0][0], self.board[0][1], self.board[0][2]], [self.board[1][0], self.board[1][1], self.board[1][2]], [self.board[2][0], self.board[2][1], self.board[2][2]], [self.board[0][0], self.board[1][0], self.board[2][0]], [self.board[0][1], self.board[1][1], self.board[2][1]], [self.board[0][2], self.board[1][2], self.board[2][2]], [self.board[0][0], self.board[1][1], self.board[2][2]],
        [self.board[0][2], self.board[1][1], self.board[2][0]]]
        if ["X", "X", "X"] in positions:
            return "X"
        if ["O", "O", "O"] in positions:
            return "O"
        if "*" in self.board[0] or "*" in self.board[1] or "*" in self.board[2]:
            return None
        return "*"

def main():
    while True:
        game = TicTacToe(input("Welcome! Move first? (y/n) ").strip() == "y", input("Display move recommendations? (y/n) ").strip() == "y")
        print("Moves are (x, y), with top left being (0, 0).")
        game.start()
        if input("Good game! Play again? (y/n) ").strip() != "y":
            break
        os.system('cls' if os.name == 'nt' else 'clear')
    print("It was nice playing with you...")

if __name__ == "__main__":
    main()
