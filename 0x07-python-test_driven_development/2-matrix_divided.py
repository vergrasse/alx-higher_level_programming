def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
    - matrix: a list of lists of integers or floats
    - div: a number (integer or float) that is not equal to 0

    Returns:
    - A new matrix where all elements are divided by the given divisor and rounded to 2 decimal places

    Raises:
    - TypeError: if the input matrix is not a list of lists of integers/floats, or if the divisor is not a number
    - ZeroDivisionError: if the divisor is equal to 0
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
