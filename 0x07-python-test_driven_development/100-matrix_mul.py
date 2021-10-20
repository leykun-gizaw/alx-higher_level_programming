#!/usr/bin/python3
"""Module defines 'matrix_mul' function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices together.

    Returns the matrix product of @m_a and @m_b

    Args:
        m_a (list): List of lists
        m_b (list): List of lists

    Returns:
        Matrix product of @m_a & @m_b

    Raises:
        TypeError: If @m_a or @m_b are not lists
                 : If @m_a or @m_b are not list of lists
                 : If @m_a's or @m_b's elements are not either integers or
                 floats
                 : If all rows of @m_a or @m_b are not the same size

        ValueError: If either @m_a or @m_b is empty
                  : If @m_a and @m_b can't be multiplied
    """
    prod_matrix, prod_row = [], []
    prod_sum = 0

    # Code to verify Test_Case 1.
    # Details of Test_Cases located in file ``./tests/5-text_indentation.txt``
    is_list(m_a, "m_a")
    is_list(m_b, "m_b")
    # Code to verify Test_Case 2.
    is_list_of_list(m_a, "m_a")
    is_list_of_list(m_b, "m_b")
    # Code to verify Test_Case 3.
    is_not_empty_matrix(m_a, "m_a")
    is_not_empty_matrix(m_b, "m_b")
    # Code to verify Test_Case 4.
    numness_check(m_a, "m_a")
    numness_check(m_b, "m_b")
    # Code to verify Test_Case 5.
    rows_same_size(m_a, "m_a")
    rows_same_size(m_b, "m_b")
    # Code to verify Test_Case 6.
    multipliable(m_a, m_b)

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                prod_sum += m_a[len(prod_matrix)][k] * m_b[k][len(prod_row)]
            prod_row.append(prod_sum)
            prod_sum = 0
        prod_matrix.append(prod_row)
        prod_row = []
    return prod_matrix


def is_list(matrix, name):
    """Check if passed argument is a list.

    Args:
        matrix (list): List of lists
        name (str): Name of the @matrix

    Returns:
        None

    Raises:
        TypeError: If @matrix is not a list
    """
    if not isinstance(matrix, list):
        raise TypeError(f"{name} must be a list")
    return None


def is_list_of_list(matrix, name):
    """Check if passed argument is a list of lists.

    Args:
        matrix (list): List of lists
        name (str): Name of the @matrix

    Returns:
        None

    Raises:
        TypeError: If @matrix is not a list of lists
    """
    if any(not isinstance(el, list) for el in matrix):
        raise TypeError(f"{name} must be a list of lists")


def is_not_empty_matrix(matrix, name):
    """Check if passed argument is an empty list.

    Args:
        matrix (list): List of lists
        name (str): Name of the @matrix

    Returns:
        None

    Raises:
        ValueError: If @matrix is empty
    """
    if matrix == [] or any(el == [] for el in matrix):
        raise ValueError(f"{name} can't be empty")


def numness_check(matrix, name):
    """Checks if matrix elements are numbers (either int or float).

    Args:
        matrix (list): List of lists
        name (str): Name of the matrix

    Returns:
        None

    Raises:
        TypeError: If any elements are not numbers (i.e. not int or float)
    """
    for el in matrix:
        if any(not isinstance(e, int) for e in el):
            raise TypeError(f"{name} should contain only integers or floats")

    return None


def rows_same_size(matrix, name):
    """Check if passed argument has same size lists in it.

    Args:
        matrix (list): List of lists
        name (str): Name of the @matrix

    Returns:
        None

    Raises:
        TypeError: If @matrix has different size lists in it
    """
    size = len(matrix[0])
    for el in matrix:
        if size != len(el):
            raise TypeError(f"each row of {name} must be of the same size")
    return None


def multipliable(m_a, m_b):
    """Check matrices can be multiplied.

    Args:
        matrix (list): List of lists
        name (str): Name of the @matrix

    Returns:
        None

    Raises:
        ValueError: If can not multiply @m_a and @m_b
    """
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
