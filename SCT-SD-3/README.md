# 🧩 Sudoku Solver GUI (Python)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-lightgrey.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-Backtracking-success.svg)

An **interactive desktop Sudoku Solver** built using **Python**, **Tkinter**, and a **Backtracking Algorithm**.

The application allows users to manually enter Sudoku puzzles and automatically solves them while enforcing Sudoku constraints through real-time validation.

This project demonstrates:

* Recursive algorithm design
* Constraint satisfaction logic
* GUI application development
* Input validation handling
* Modular Python architecture
* Execution-time benchmarking

---

## ✨ Key Features

✔ Interactive 9×9 Sudoku GUI

✔ Automatic solving using Backtracking Algorithm

✔ Real-time numeric input validation (1–9 only)

✔ Duplicate conflict detection before solving

✔ Solver-generated values highlighted in blue

✔ Prevents editing solved cells

✔ Execution-time measurement display

✔ Detects unsolvable puzzle configurations

✔ Reset / Clear board functionality

✔ Clean modular multi-file architecture

---

## 🧠 Algorithm Used — Backtracking

The solver uses a **Depth-First Search Backtracking Algorithm**, commonly applied in:

* Sudoku solving
* N-Queens problem
* Maze traversal
* Constraint satisfaction problems
* Artificial Intelligence search systems

### Algorithm Workflow

1. Locate empty cell
2. Try digits 1–9
3. Validate against:

   * Row constraints
   * Column constraints
   * 3×3 subgrid constraints
4. If valid → recurse forward
5. If invalid → backtrack
6. Continue until puzzle solved

---

## 🖥️ Application Preview

![sudoku solver screenshot](screenshot/image.png)

---

## 📂 Project Structure

```
sudoku-solver-gui/
│
├── main.py        # Application entry point
├── gui.py         # Tkinter GUI logic
├── solver.py      # Backtracking solver engine
├── validator.py   # Board validation logic
├── constants.py   # Configuration settings
│
├── README.md
├── requirements.txt
├── .gitignore
└── screenshot/
```

This layered architecture separates:

* Presentation layer
* Solver engine
* Validation logic
* Configuration constants

and prevents circular dependencies.

---

## ⚙️ How to Run the Project

### Clone repository

```
git clone https://github.com/BhaveshV23/SkillCraft-Internship-Tasks.git
```

### Navigate to project directory

```
cd SkillCraft-Internship-Tasks/SCT-SD-3
```

### Run the application

```
python main.py
```

The GUI launches automatically.

---

## 📊 Example Workflow

1️⃣ Enter Sudoku values manually

2️⃣ Click **Solve Puzzle**

3️⃣ Solver fills missing cells automatically

4️⃣ Execution time displayed after solving

5️⃣ Click **Clear Board** to reset puzzle

---

## 🛡️ Edge Cases Handled

The solver safely detects:

* Invalid numeric input
* Duplicate row conflicts
* Duplicate column conflicts
* Duplicate subgrid conflicts
* Empty puzzle submission
* Unsolvable puzzles
* Multiple Solve button presses
* Editing solver-generated values

---

## 📈 Performance

Typical solving time:

```
0.001 – 0.02 seconds
```

(depending on puzzle complexity)

Measured using:

```
time.perf_counter()
```

for high-precision benchmarking.

---

## 🧱 Technologies Used

* Python 3
* Tkinter (GUI framework)
* Backtracking Algorithm
* Object-Oriented Programming
* Modular Software Architecture

---

## 🎯 Learning Outcomes

This project demonstrates implementation of:

* Recursive backtracking algorithms
* Constraint validation systems
* GUI event-driven programming
* Input sanitization techniques
* Execution-time measurement
* Modular Python project structuring
* Edge-case handling strategies

---

## 🔮 Future Improvements

Planned enhancements:

* Step-by-step solving animation mode
* Puzzle difficulty selector
* Random puzzle generator
* Web-based version (Flask / React)
* Export solved puzzle as image
* Windows executable release (.exe)

---

## 👨‍💻 Author

**Bhavesh Vadnere**

Information Technology Engineering Student
Interested in Python Development, AI, and Software Engineering

GitHub: https://github.com/BhaveshV23

LinkedIn: https://www.linkedin.com/in/bhavesh-vadnere

---

## ⭐ Support

If you found this project useful or interesting:

Please consider ⭐ starring the repository.
