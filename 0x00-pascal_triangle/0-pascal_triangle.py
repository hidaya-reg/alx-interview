#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal's Triangle of size n.
    Returns an empty list if n <= 0.
    """
    triangle = []
    
    if n <= 0:
        return triangle
    
    triangle = [[1]]
    
    for i in range(1, n):
        previous_row = triangle[i - 1]
        current_row = [1]
        
        for j in range(len(previous_row) - 1):
            current_row.append(previous_row[j] + previous_row[j + 1])
        
        current_row.append(1)
        triangle.append(current_row)
    
    return triangle
