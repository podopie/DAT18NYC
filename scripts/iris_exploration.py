#%pylab inline
import pandas as pd
from sklearn import datasets
import pandas.tools.rplot as rplot

iris = datasets.load_iris()
iris_description = iris.DESCR
irisdf = pd.DataFrame(iris.data, columns=iris.feature_names)
irisdf['target'] = iris.target
print irisdf.columns
irisdf.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width',  'target']

iris_grps = irisdf.groupby('target')

print iris_grps.describe()

plt.figure()
pd.scatter_matrix(irisdf)

# example of how sepal is less indicative of target
patterns = [
    ('sepal_length', 'sepal_width'),
    ('petal_length', 'petal_width'),
]

for pattern in patterns:
    plt.figure(figsize=(18, 6))
    plot = rplot.RPlot(irisdf, x=pattern[1], y=pattern[0])
    plot.add(rplot.TrellisGrid(['.','target']))
    plot.add(rplot.GeomScatter())
    print plot.render(plt.gcf())

irisdf["petal_area"] = irisdf["petal_length"] * irisdf["petal_width"]

def petal_guess(x):
    if(x < 1):
        return 0
    elif(x < 7.5):
        return 1
    else:
        return 2

irisdf['guess'] = irisdf['petal_area'].apply(petal_guess)

irisdf['correct?'] = irisdf.apply(lambda row: 1 if row['target'] == row['guess'] else 0, axis=1)
acc = float(irisdf['correct?'].sum()) / float(len(irisdf))
print acc

