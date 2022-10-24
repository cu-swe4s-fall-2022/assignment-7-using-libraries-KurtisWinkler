import numpy as np
import pandas as pd


def get_random_matrix(num_rows, num_columns):
    
    if type(num_rows) != int or type(num_columns) != int:
        raise TypeError("num_rows and num_columns must be integers")
        
    if min(num_rows, num_columns) < 1:
        raise IndexError('num_rows and num_columns must be >= 1')

    return np.random.rand(num_rows, num_columns)

def get_file_dimensions(file_name):
	return (0,0)

def write_matrix_to_file(num_rows, num_columns, file_name):
	return None
