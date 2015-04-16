## Mean Absolute Error(MAE), Mean Squared Error(MSE)
Implementation of each without scikit learn:

    from numpy import mean
    def mae(predict, actual):
    return mean(abs(predict - actual))

    def mse(predict, actual):
    return mean((predict - actual)**2)

Actual calls from sklearn.metrics:

    from sklearn.metrics import mean_squared_error, mean_absolute_error
    mean_squared_error(predicted, actual)
    mean_absolute_error(predicted, actual)

## Application to the mammals data set

    from matplotlib import pyplot as plt
    from sklearn import linear_model, metrics
    from scipy import stats
    import numpy as np
    from pandas import read_csv
    lm = linear_model.LinearRegression()
    mammals = read_csv('https://gist.github.com/podopie/5ea0c35ecc556d6cbae3/raw/c56f694bf4e7bbeeec92e24d33a8f49f7da37be8/mammals.csv')
    body, brain = mammals[ ['body'] ].values, mammals['brain'].values
    lm.fit(np.log(body), np.log(brain))
    # View a qqplot of the predicted values
    stats.probplot(abs(lm.predict(np.log(body)) - np.log(brain)), dist="norm", plot=plt)
    plt.show()

    metrics.mean_squared_error(lm.predict(np.log(body)), np.log(brain))
    metrics.mean_absolute_error(lm.predict(np.log(body)), np.log(brain))