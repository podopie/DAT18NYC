import pandas as pd

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
header = [
    'mpg', 'cylinders', 'displacement',
    'horsepower', 'weight', 'acceleration',
    'model year', 'origin', 'car name'
]

autompg = pd.read_csv(url, delimiter='\s+', header=0, na_values='?')
autompg.columns = header

years = [70, 82]
for year in years:
    print autompg[autompg['model year'] == year].describe()

for i in autompg['model year'].unique():
    autompg[autompg['model year'] == i] = autompg[autompg['model year'] == i].fillna(autompg[(autompg['horsepower'].notnull()) & (autompg['model year'] == i)].mean())

autompg['manufacturer'] = autompg['car name'].apply(lambda x: x.split()[0])

print autompg[autompg['horsepower'].isnull()]
