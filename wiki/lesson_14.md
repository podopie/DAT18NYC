    import csv
    import numpy as np
    import pandas as pd
    from dateutil import parser
    import pylab as pl
    import statsmodels.api as sm
    import matplotlib.pyplot as plt
    import random
    from sklearn.preprocessing import scale
    from numpy import inf
    import scipy.stats as stats
    import pylab

## Import Data

    data = pd.read_csv("/Users/PMcNamara/Downloads/baseball.csv")

## Drop Unwanted Variables

    slimdata = data.drop(['playerID', 'lahmanID', 'managerID', 'birthYear', 'birthMonth', 'birthDay', 
    'birthCountry', 'birthState', 'birthCity', 'deathYear', 'deathMonth', 'deathDay', 'deathCountry', 
    'deathState', 'deathCity', 'nameFirst','nameLast', 'nameNote', 'nameGiven', 'nameNick','bats', 
    'throws', 'debut', 'finalGame', 'college','lahman40ID', 'lahman45ID', 'retroID', 'holtzID', 
    'bbrefID', 'deathDate', 'birthDate','teamID', 'lgID', 'stint','G_batting','X2B', 'X3B',
    'CS', 'SO', 'IBB', 'HBP', 'SH', 'SF', 'GIDP', 'G_old', 'hofID', 'yearID'], axis =1)

    slimdata = slimdata.dropna()

### Shrinking the data to make things easier

    slimdata['random'] = np.random.randn(len(slimdata))
    slimdata = slimdata[slimdata.random > 1]
    slimdata.AB = np.log(slimdata.AB)
    slimdata = slimdata.replace([inf, -inf], np.nan)
    slimdata = slimdata.dropna()


## Plotting scatterplot matrix for collinearity

### Histogram
    pd.tools.plotting.scatter_matrix(slimdata, alpha=0.2, diagonal='hist')
    plt.show()

### Kernel Density
    pd.tools.plotting.scatter_matrix(SLIMDATA, alpha=0.2, diagonal='kde')
    plt.show()

## Defining IVs & DVs

    X = np.array(slimdata.drop(['salary'], axis = 1))
    y = np.array(slimdata['salary'])

## Running regression model

    model = sm.OLS(y, X)
    results = model.fit()
    print results.summary()

## Box plot for outliers

    slimdata.boxplot()
    plt.show()
    slimdata.drop(['salary'], axis = 1).boxplot()
    plt.show()

## Normalization

### Scaling 
### Mean-center then divide by std dev

    data_norm = pd.DataFrame(scale(slimdata), index=slimdata.index, columns=slimdata.columns)
    data_norm.boxplot()
    plt.show()

## Running regression model again

    X = np.array(data_norm.drop(['salary'], axis = 1))
    y = np.array(data_norm['salary'])

    model2 = sm.OLS(y, X)
    results2 = model2.fit()
    print results2.summary()

## Influence plot
    influence = results2.get_influence()
    (d, p) = influence.cooks_distance
    plt.stem(np.arange(len(d)), d, markerfmt=",")
    plt.show()

## Residuals vs. Fitted plot

    plt.scatter(results.norm_resid(), results.fittedvalues)
    plt.xlabel('Fitted Values')
    plt.ylabel('Normalized residuals')

## QQ Plot

    stats.probplot(slimdata.AB, dist="norm", plot=pylab)
    pylab.show()

## The effect of reshaping/dropping variables
    res_dropped = ols_results.params / ols_results2.params * 100 - 100