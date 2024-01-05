import tkinter as tk
import time
import boardAlgo

class PuzzleGUI:
    def __init__(self, master, initial_board):
        self.master = master
        self.master.title("8 Puzzle Solver")
        self.board = initial_board
        self.dimension = int(len(initial_board) ** 0.5)

        # Dark theme colors
        self.bg_color = "#333"
        self.tile_color = "#A47449"
        self.text_color = "white"

        # Font settings
        self.font_size = 24
        self.font = ("Helvetica", self.font_size)

        self.tiles = [[None] * self.dimension for _ in range(self.dimension)]
        self.empty_position = self.board.index(0)

        self.init_board()
        self.draw_board()

    def init_board(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                value = self.board[i * self.dimension + j]
                self.tiles[i][j] = tk.Button(
                    self.master,
                    text=str(value) if value != 0 else "",
                    width=10,
                    height=5,
                    bg=self.tile_color,
                    fg=self.text_color,
                    font=self.font,
                    command=lambda row=i, col=j: self.move_tile(row, col),
                )
                self.tiles[i][j].grid(row=i, column=j)

    def draw_board(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                value = self.board[i * self.dimension + j]
                self.tiles[i][j].config(
                    text=str(value) if value != 0 else "",
                    bg=self.tile_color,
                    fg=self.text_color,
                    font=self.font,
                )

    def move_tile(self, row, col):
        current_position = row * self.dimension + col
        if self.is_valid_move(current_position):
            self.board[current_position], self.board[self.empty_position] = (
                self.board[self.empty_position],
                self.board[current_position],
            )
            self.empty_position = current_position
            self.draw_board()

    def is_valid_move(self, current_position):
        i, j = divmod(current_position, self.dimension)
        empty_i, empty_j = divmod(self.empty_position, self.dimension)
        return (
            (i == empty_i and abs(j - empty_j) == 1)
            or (j == empty_j and abs(i - empty_i) == 1)
            and (i != empty_i or j != empty_j)
        )


def solve_puzzle_with_moves(puzzle_gui, moves):
    for move in moves:
        if move == "up":
            row, col = divmod(puzzle_gui.empty_position - puzzle_gui.dimension, puzzle_gui.dimension)
        elif move == "down":
            row, col = divmod(puzzle_gui.empty_position + puzzle_gui.dimension, puzzle_gui.dimension)
        elif move == "left":
            row, col = divmod(puzzle_gui.empty_position - 1, puzzle_gui.dimension)
        elif move == "right":
            row, col = divmod(puzzle_gui.empty_position + 1, puzzle_gui.dimension)
        puzzle_gui.move_tile(row, col)
        puzzle_gui.master.update()
        time.sleep(1)  # Delay for better visualization


def main():
    root = tk.Tk()
    initial_board = [1,8,2,0,4,3,7,6,5]
    puzzle_gui = PuzzleGUI(root, initial_board)

    board = boardAlgo.BoardManager(initial_board)
    moves = board.moves.copy()

    solve_puzzle_with_moves(puzzle_gui, moves)

    # Configure root window background color
    root.configure(bg="#333")

    root.mainloop()


if __name__ == "__main__":
    main()
