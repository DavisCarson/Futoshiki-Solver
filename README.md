# Futoshiki Puzzle Solver

This repository contains a Python implementation of a solver for the **Futoshiki puzzle** (also known as "More or Less" puzzle). Futoshiki is a logic-based puzzle where you fill a grid with numbers under certain constraints, including inequalities between neighboring cells.

### How It Works
The solver uses **backtracking** to explore possible number assignments for each cell in the grid. It checks that each assignment satisfies:
1. **Row and Column Uniqueness:** No number appears more than once in any row or column.
2. **Inequality Constraints:** The solver ensures that the inequalities between cells are respected.
3. **2x2 Sub-squares Validation:** In this implementation, an additional constraint ensures that values in each 2x2 sub-grid are unique.

### Key Features
- Implements the **backtracking** algorithm to solve the puzzle by filling the grid progressively and exploring possible solutions.
- Includes functions to check:
  - Whether a value can be placed in a specific cell without violating row, column, or inequality constraints.
  - If the puzzle is fully solved (i.e., all cells are filled and constraints are met).
- Designed to work on a **4x4 grid** but can be modified for larger grid sizes with additional constraints.

### File Overview
- **main.py**:  
  Contains the main logic of the Futoshiki solver, including the backtracking algorithm, validation checks, and puzzle grid initialization.

### How to Use
1. Clone the repository.
2. Run the script using Python:
   ```bash
   python main.py
   ```
   The solver will print the solved Futoshiki grid or state that no solution was found.
