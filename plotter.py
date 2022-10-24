import pandas as pd
import matplotlib.pyplot as plt


iris = pd.read_csv('iris.data', sep=',', header=None)
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
