'''Contains functions to make, analyze, and write matrices

    get_random_matrix - creates a matrix with a specified number
                        of rows and columns

    get_file_dimensions - returns the dimensions of a file

    write_matrix_to file - creates a matrix using get_random_matrix
                           and writes it to a file
'''


import numpy as np
import pandas as pd
import sys


def get_random_matrix(num_rows, num_columns):
    """Generates a matrix with values between 0 and 1

    Parameters
    ----------
    num_rows - number of rows for matrix

    num_columns - number of columns for the matrix

    Returns
    -------
    Matrix with specified rows and columns, all values between 0 and 1

    """
    if type(num_rows) != int or type(num_columns) != int:
        raise TypeError("num_rows and num_columns must be integers")

    if min(num_rows, num_columns) < 1:
        raise IndexError('num_rows and num_columns must be >= 1')

    return np.random.rand(num_rows, num_columns)


def get_file_dimensions(file_name):
    """Returns dimensions of file

    Parameters
    ----------
    file_name - name of file to get dimensions of

    Returns
    -------
    file shape returned as (rows, columns)

    """
    try:
        file = pd.read_csv(file_name, sep=',', header=None)

    except FileNotFoundError:
        raise FileNotFoundError('Could not find ' + file_name)

    except PermissionError:
        raise PermissionError('Do not have permission to open ' + file_name)

    except Exception as e:
        print('Could not open ' + file_name)
        sys.exit(1)

    return file.shape


def write_matrix_to_file(num_rows, num_columns, file_name):
    """Creates a matrix with values between 0 and 1 and
       writes it to a file

    Parameters
    ----------
    num_rows - number of rows for matrix

    num_columns - number of columns for the matrix

    file_name - file name of output file

    Returns
    -------
    True if data is written to file

    """
    if type(file_name) != str:
        raise TypeError('file_name must be a string')

    # exceptions handled in get_randmom_matrix
    data = get_random_matrix(num_rows, num_columns)

    data_df = pd.DataFrame(data)
    data_df.to_csv(file_name + '.csv', sep=',')

    return True
