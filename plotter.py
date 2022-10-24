import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('iris.data', sep=',', header=None)
iris.columns = ['sepal_width', 'sepal_length', 'petal_width', 'petal_length', 'species']

# make box plot
fig1, ax1 = plt.subplots()
params = ['sepal_width', 'sepal_length', 'petal_width', 'petal_length']
ax1.boxplot(iris[params], labels = params)
ax1.set_ylabel('cm')
fig1.savefig('iris_boxplot.png')
