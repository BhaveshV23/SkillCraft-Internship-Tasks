import tkinter as tk
from tkinter import messagebox
import time

from solver import solve
from validator import is_board_valid
from constants import *


class SudokuGUI:

    def __init__(self, root):
        self.root = root
        root.title("Sudoku Solver GUI")
        root.config(
            padx=WINDOW_PADDING_X,
            pady=WINDOW_PADDING_Y,
            bg=BACKGROUND_COLOR
        )

        self.gui_board = []

        self.create_grid()
        self.create_buttons()

    def validate_input(self, value):
        """Allow only digits 1-9 or empty."""
        return value == "" or (value.isdigit() and 1 <= int(value) <= 9)


    def create_grid(self):
        validator = self.root.register(self.validate_input)

        for r in range(GRID_SIZE):
            row_entries = []

            for c in range(GRID_SIZE):
                entry = tk.Entry(
                    self.root,
                    bg=GRID_COLOR,
                    width=3,
                    justify="center",
                    font=FONT,
                    validate="key",
                    validatecommand=(validator, "%P")
                )

                pad_x = (1, 5) if c in (2, 5) else 1
                pad_y = (1, 5) if r in (2, 5) else 1

                entry.grid(row=r, column=c, padx=pad_x, pady=pad_y)

                row_entries.append(entry)

            self.gui_board.append(row_entries)


    def create_buttons(self):
        frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        frame.grid(row=9, column=0, columnspan=GRID_SIZE, pady=20)

        self.solve_btn = tk.Button(
            frame,
            text="Solve Puzzle",
            bg=PRIMARY_COLOR,
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=12,
            command=self.solve_clicked
        )

        self.solve_btn.grid(row=0, column=0, padx=10)

        clear_btn = tk.Button(
            frame,
            text="Clear Board",
            bg=CLEAR_COLOR,
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=12,
            command=self.clear_clicked
        )

        clear_btn.grid(row=0, column=1, padx=10)


    def read_board(self):
        board = []

        for row in self.gui_board:
            current_row = []

            for entry in row:
                value = entry.get()
                current_row.append(int(value) if value else 0)

            board.append(current_row)

        return board


    def write_solution(self, board):
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                entry = self.gui_board[r][c]

                if entry.get() == "":
                    entry.insert(0, board[r][c])
                    entry.config(
                        fg=SOLVED_COLOR,
                        state="readonly"
                    )


    def solve_clicked(self):
        board = self.read_board()

        if all(all(cell == 0 for cell in row) for row in board):
            messagebox.showwarning(
                "Empty Puzzle",
                "Please enter at least one number."
            )
            return


        if not is_board_valid(board):
            messagebox.showerror(
                "Invalid Puzzle",
                "Duplicate number detected!"
            )
            return


        start = time.perf_counter()

        solvable = solve(board)

        end = time.perf_counter()


        if solvable:
            self.write_solution(board)
            self.solve_btn.config(state=tk.DISABLED)

            messagebox.showinfo(
                "Solved",
                f"Puzzle solved in {end-start:.4f} seconds"
            )

        else:
            messagebox.showwarning(
                "Unsolvable",
                "No solution exists."
            )


    def clear_clicked(self):
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                entry = self.gui_board[r][c]
                entry.config(state="normal", fg="black")
                entry.delete(0, tk.END)

        self.solve_btn.config(state=tk.NORMAL)