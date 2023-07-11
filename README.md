# Intelligent-A-star-Puzzle-Solver-Finding-the-Optimal-Solution
The project utilizes the A* search algorithm and heuristics to solve the 7-tile puzzle using the shortest possible path. The solver evaluates all possible moves to provide efficient and reliable optimal solutions.

## 7-tile Puzzle :
The 7-tile puzzle is played on a 3 by 3 grid with 7 tiles labeled with corresponding images and two empty grids.
The goal is to rearrange the tiles so that they are in order and the empty places are at the bottom right.
<img width="1530" alt="moves" src="https://github.com/YangCheng27/Intelligent-A-star-Puzzle-Solver-Finding-the-Optimal-Solution/assets/56757171/fec20a5c-33df-4505-a22f-6705208b486e">
![animation](https://github.com/YangCheng27/Intelligent-A-star-Puzzle-Solver-Finding-the-Optimal-Solution/assets/56757171/7d5e6cfe-b3f1-47d5-9770-4c239a25a611)

## How to find the optimal solution?
Using A* searching algorithm!

1. Before implementing the A* search algorithm, we need to transform the 7-tile puzzle into a number puzzle with numbers 1 to 7 and an empty cell. 
<img width="1103" alt="moves_n1" src="https://github.com/YangCheng27/Intelligent-A-star-Puzzle-Solver-Finding-the-Optimal-Solution/assets/56757171/e8cf8271-bd19-4dfd-b602-06953631649e">

We solve the puzzle by moving the tiles around. For each step, we can only move one of the neighbor tiles (left, right, top, and bottom but not diagonally) into an empty grid. And all tiles must stay in the 3x3 grid (so no wrap-around allowed). An example is shown in the picture below. Suppose
we start from the following initial state:
<img width="980" alt="moves_n2" src="https://github.com/YangCheng27/Intelligent-A-star-Puzzle-Solver-Finding-the-Optimal-Solution/assets/56757171/a38b609f-596d-44c1-a8fe-8ced8744dc98">





## A* Searching Algorithm
