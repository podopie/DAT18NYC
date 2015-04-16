# Practice Goals
* Work through various data and scatterplots
* Create linear models with simple relationships (one feature)
* Create linear models with multiple features
* Evaluate model performance

## Build an incredibly basic linear model function.

    from numpy import array, dot
    from scipy import linalg
    X = array([ [1, 1], [1, 2], [1, 3], [1, 4] ])
    y = array([ [1], [2], [3], [4] ])
    n = linalg.inv(dot(X.T, X))
    k = dot(X.T, y)
    coef_ = dot(n, k)

This can all be turned into one relatively simple algorithm, though it is rather limiting in features.

    def regression(input, response):
        return dot(linalg.inv(dot(input.T, input)), dot(input.T, response))

## Practice: Plotting Data

We're gonna start by playing with data about mammals brain and body size. Use the gist link and find the "< >" button to get the actual raw data file.

    https://gist.github.com/podopie/5ea0c35ecc556d6cbae3

Lets load the data into pandas and generate a scatterplot:

    import pandas as pd
    import matplotlib.pyplot as plt
    mammals = pd.read_csv('/location/to/file/mammals.csv')
    plt.scatter(mammals['body'], mammals['brain'])
    plt.show()
    plt.hist(mammals['body'], bins=range(0, 10000, 100))
    plt.show()
    plt.hist(mammals['brain'], bins=range(0, 10000, 100))
    plt.show()

For the most part, we know that this data is a _long tail_ distribution, so we could take the log of each feature to create something that is not just more readable, but new features that could be a better representation of the data!

    from numpy import log
    mammals['log_body'] = log(mammals['body'])
    mammals['log_brain'] = log(mammals['brain'])
    plt.scatter(mammals['log_body'], mammals['log_brain'])

## Practice: Using Linear Regressions

    from sklearn import linear_model
    # Make the model object
    regr = linear_model.LinearRegression()
    # Fit the data
    body = [[x] for x in mammals['body'].values]
    brain = mammals['brain'].values
    regr.fit(body, brain)

Above we go through some steps to get our data 'presentable' for scikit learn. There is a regression model available in PANDAS, but let's stick with the models available in scikit learn.

We can overview the important segments of our model:

    # Display the coefficients:
    regr.coef_
    # Display our SSE:
    mean((regr.predict(body) - brain) ** 2)
    # Scoring our model (closer to 1 is better!)
    regr.score(body, brain)

Our performance here is okay (~87% accuracy), and can verify this with a plot:

    plt.scatter(body, brain)
    plt.plot(body, regr.predict(body), color='blue', linewidth=3)
    plt.show()
    
## Classwork
    http://bit.ly/16bZqir # cleaned up aggregation nytimes data

1. Go through the same steps, but this time generate a new model use the log of brain and body, which we know generated a much better distribution and cleaner set of data. Compare the results to the original model. Remember that exp() can be 
used to "normalize" our "logged" values. ***Note: Make sure you start a new linear regression object!***

2. Using your aggregate data compiled from nytimes1-30.csv, write a python script that determines the best model predicting CTR based off of age and gender. Since gender is not actually numeric (it is binary), investigate ways to vectorize this feature. ***Clue: you may want two features now instead of one.***

3. Compare this practice to making two separate models based on Gender, with Age as your one feature predicting CTR. How are your results different? Which results would you be more confident in presenting to your manager? Why's that?

4. Evaluate what data you could still use to improve your nytimes model. Consider plotting your model to service your explanations and write a short blurb about insights gained and next steps in your "data collection."