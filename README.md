# libraries

## Description
This code works with the standard python library\
This project creates 3 figures:\
&emsp; A box plot showing distribution of plant characteristics\
&emsp; A scatter plot of petal length vs petal width\
&emsp; A multipanel plot containing the box and scatter plots

## How to Use
Run with `bash run.sh`

Update run.sh with input file

Example:\
`python plot_gtex.py --file_name 'iris.data'`
                

**Arguments:**

--file_name : name of file to be analyzed


## Functions
**get_random_matrix** - creates a random matrix with a specified number of rows and columns

**get_file_dimensions** - returns the dimensions of a file

**write_matrix_to file** - creates a matrix using get_random_matrix and writes it to a file