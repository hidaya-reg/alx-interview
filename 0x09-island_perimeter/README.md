# 0x09. Island Perimeter

## Concepts Needed:
### 1. 2D Arrays (Matrices):
- Accessing and iterating over elements in a 2D array.
- Understanding how to navigate through adjacent cells (horizontally and vertically).

### 2. Conditional Logic:
- Applying conditions to determine whether a cell contributes to the perimeter of the island.

### 3. Counting Techniques:
- Developing a method to count the edges that contribute to the island’s perimeter.

### 4. Problem-Solving Strategies:
- Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

### 5. Python Programming:
- Nested loops for iterating over grid cells.
- Conditional statements to check the status of adjacent cells.

## Resources:
- **Python Official Documentation:**
[Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions): Understanding how to work with lists within lists in Python.
- **GeeksforGeeks Articles:**
[Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/): A guide to working with 2D arrays in Python effectively.
- **TutorialsPoint:**
[Python Lists](https://www.tutorialspoint.com/python/python_lists.htm): Explains how to create, access, and manipulate lists in Python, which is essential for working with a grid.
- **YouTube Tutorials:**
[Python 2D arrays and lists](https://www.youtube.com/watch?v=aNzepGawwCI&ab_channel=RealLifeEd)

## Additional Resources
[Mock Technical Interviews](https://www.youtube.com/watch?v=fFgEM6CMQc4&ab_channel=EvgenyKim)

## Tasks
### 0. Island Perimeter
Create a function ``def island_perimeter(grid)``: that returns the perimeter of the island described in ``grid``:
- ``grid`` is a list of list of integers:
    + 0 represents water
    + 1 represents land
    + Each cell is square, with a side length of 1
    + Cells are connected horizontally/vertically (not diagonally).
    + ``grid`` is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

```bash
$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

$ 
$ ./0-main.py
12
``` 