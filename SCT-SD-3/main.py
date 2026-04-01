from tkinter import Tk
from gui import SudokuGUI

def main():
    root = Tk()
    SudokuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()