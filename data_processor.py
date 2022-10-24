import numpy as np
import pandas as pd
import sys


def get_random_matrix(num_rows, num_columns):

    if type(num_rows) != int or type(num_columns) != int:
        raise TypeError("num_rows and num_columns must be integers")

    if min(num_rows, num_columns) < 1:
        raise IndexError('num_rows and num_columns must be >= 1')

    return np.random.rand(num_rows, num_columns)


def get_file_dimensions(file_name):

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

    if type(file_name) != str:
        raise TypeError('file_name must be a string')

    # exceptions handled in get_randmom_matrix
    data = get_random_matrix(num_rows, num_columns)

    data_df = pd.DataFrame(data)
    data_df.to_csv(file_name + '.csv', sep=',')

    return True
