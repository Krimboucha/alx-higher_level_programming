#!/usr/bin/python3
"""
    matrix_divided divides all elements of a matrix by a number
    Parameters: matrix a matrix of ints/floats
                div the number to divide the matrix with
"""
def matrix_divided(matrix, div):
    """
    Return: the same matrix with divided elements
    """
    if not all(isinstance(row, list) and 
            all(isinstance(val, (int, float)) for val in row)
            for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_lengths = [len(row) for row in matrix]
    if not all(length == row_lengths[0] for length in row_lengths):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result_matrix = [[round(val / div, 2) for val in row] for row in matrix]
    return result_matrix
