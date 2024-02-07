#!/usr/bin/python3
""" pascal_triangle module
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]  # First element in every row is 1

        # Calculate the next elements in the row based on the previous row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        if i > 0:
            row.append(1)  # Last element in every row is 1

        triangle.append(row)

    return triangle
