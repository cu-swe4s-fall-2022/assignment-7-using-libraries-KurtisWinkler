"""Processes iris data from a specified file.
   Creates a box plot of iris parameters
   Creates a scatter plot of petal length vs petal width
   with each species labeled
   Creates a multi-panel plot with box plot and scatter plot

    Parameters
    ----------
    --file_name : string
                   name of file containing data

    Returns
    -------
    None

"""

import argparse
import pandas as pd
import matplotlib.pyplot as plt


def get_args():
    """processes input arguments

    Parameters
    ----------
    None

    Returns
    -------
    parser.parse_args() - arguments to be used in script

    """

    parser = argparse.ArgumentParser()

    # add argument for file name
    parser.add_argument('--file_name',
                        type=str,
                        help='name of file to analyze',
                        required=True)

    return parser.parse_args()


def main():

    args = get_args()

    try:
        iris = pd.read_csv(args.file_name, sep=',', header=None)

    except FileNotFoundError:
        print('Could not find ' + args.file_name)
        sys.exit(1)

    except PermissionError:
        print('Do not have permission to open ' + arg.file_name)
        sys.exit(1)

    except Exception as e:
        print('Could not open ' + args.file_name)
        sys.exit(1)

    iris.columns = ['sepal_width',
                    'sepal_length',
                    'petal_width',
                    'petal_length',
                    'species']

    # make box plot
    fig1, ax1 = plt.subplots()
    params = ['sepal_width', 'sepal_length', 'petal_width', 'petal_length']
    ax1.boxplot(iris[params], labels=params)
    ax1.set_ylabel('cm')
    fig1.savefig('iris_boxplot.png')

    # make scatter plot
    fig2, ax2 = plt.subplots()
    for species_name in set(iris['species']):
        iris_subset = iris[iris['species'] == species_name]
        plt.scatter(iris_subset['petal_length'],
                    iris_subset['petal_width'],
                    label=species_name,
                    s=5)
    ax2.legend()
    ax2.set_xlabel('petal_length (cm)')
    ax2.set_ylabel('petal_width (cm)')
    fig2.savefig('petal_length_v_width_scartter.png')

    # make combined plot
    fig, axes = plt.subplots(1, 2)
    fig.set_size_inches(10, 5)

    axes[0].boxplot(iris[params], labels=params)
    axes[0].set_ylabel('cm')

    for species_name in set(iris['species']):
        iris_subset = iris[iris['species'] == species_name]
        axes[1].scatter(iris_subset['petal_length'],
                        iris_subset['petal_width'],
                        label=species_name,
                        s=5)
    axes[1].legend()
    axes[1].set_xlabel('petal_length (cm)')
    axes[1].set_ylabel('petal_width (cm)')

    for i in range(2):
        axes[i].spines['top'].set_visible(False)
        axes[i].spines['right'].set_visible(False)
        axes[i].spines['bottom'].set_visible(True)
        axes[i].spines['left'].set_visible(True)

    fig.savefig('multi_panel_figure.png')


if __name__ == '__main__':
    main()
