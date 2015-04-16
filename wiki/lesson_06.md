# Practice Goals
* Practice using both the LinearRegression and RidgeRegression models in scikit-learn
* Explore differences between a model using OLS (L1) and LLS (L2) regularization
* Tear apart and understand how predictions get built in scikit learn
* Work through the Logistic Regression model.

## More in depth understanding behind how scikit learn works

Load up this script (using the same mammals set we glanced at before) and let's break down (any also break) what's going on with each line of code.

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn import linear_model
    mammals = pd.read_csv('mammals.csv')
    lm = linear_model.LinearRegression()
    log_lm = linear_model.LinearRegression()
    body = [ [x] for x in mammals['body'].values]
    log_body = log_body = [ [x] for x in np.log(mammals['body'].values)]
    brain = mammals['brain'].values
    log_brain = np.log(mammals['brain'].values)
    lm.fit(body, brain)
    log_lm.fit(log_body, log_brain)

We can observe various features about our linear models that we've discussed in lecture.

find the intercept (note we can set to train for an intercept with set_params()):

    lm.intercept_
    log_lm.intercept_

find the coefficients:

    lm.coef_
    log_lm.coef_

Print out the predictions for a given matrix (needs to fit the same dimensional space as the data we fit):

    lm.predict(body)
    mammals['predict'] = lm.predict(body)
    log_lm.predict(log_body)
    mammals['log_predict'] = np.exp(log_lm.predict(log_body))

## Practice: Plotting Predictions

Since pyplot plots _discretely_ (and not continuously), if we want an accurate representation of any transformed plot (particularly for polynomial data), we need to sort our data frame by the response value. We can either do this before fitting a model (with the actual response) or post-fit (with the predicted response).

    # Sort by response:
    mammals = mammals.sort('brain')
    # Sort by prediction:
    mammals_log_sort = mammals.sort('log_predict')

Otherwise, use plt.scatter and plt.plot as we know how to use them.

## Multivariable regressions

Remember that we're primarily using dot matrix multiplication to come up with our values. What does this say about the format our data should be in for multiple values?

    smoking = pd.read_csv('http://www.ats.ucla.edu/stat/examples/chp/p081.txt', delimiter="\t")
    input = [ [x, y, z] for x,y,z in zip(smoking['Price'].values, smoking['Income'].values, smoking['Age'].values)]

    # More efficiently:
    input = smoking[ ['Price', 'Income', 'Age'] ].values

Otherwise, we can use observe our results exactly the same way as we had with a single variable. The coefficients will print out in the order we implemented the input matrix.


## Polynomial Regressions

Likewise, polynomial regressions can work as new inputs constructed from our data:

    mammals['body_squared'] = mammals['body']**2
    body_squared = [ [x, y] for x,y in zip(mammals['body'].values, mammals['body_squared'].values)]
    # OR
    body_squared = [ [x, y] for x,y in zip(mammals['body'].values, (mammals['body'].values)**2]    

The LinearRegression model in scikit learn uses L1-Normalization. Let's check out a Ridge Regression, which uses L2.

    ridge = linear_model.Ridge()
    ridge.fit(body_squared, brain)

Check the coefficients and the intercept. and we can verify the results of ridge.predict() against handwriting the full regression:

    ((ridge.coef_[1] * mammals['body'])**2) + ((ridge.coef_[0] * mammals['body'])) + ridge.intercept_

## Classwork
Work through the following datasets, determining best fits for each data set (predictor value/y value in parens).
To better evaluate or improve this process, try including:

    from sklearn import feature_selection
    feature_selection.univariate_selection.f_regression(input, response)

and using this against your feature matrix to determine p-values for each feature (we care about the second array it returns for now).

Datasets:

    https://gist.github.com/podopie/a2c45d2dbae9759c68de # Predicting stopping distance
    https://gist.github.com/podopie/57569c625d9dcb57e40c # Predicting City and Highway MPG.

## Logistic Regression

Let's see if we can use logistic regression to predict what kinds of beer people like.

    import re
    beer = pd.read_csv('http://www-958.ibm.com/software/analytics/manyeyes/datasets/af-er-beer-dataset/versions/1.txt', delimiter="\t")
    beer = beer.dropna()
    def good(x):
      if x > 4.3:
        return 1
      else:
        return 0

    beer['Good'] = beer['WR'].apply(good)

Let's see how fit goes using just Reviews and ABV.

    input = beer[ ['Reviews', 'ABV'] ].values
    good = beer['Good'].values
    logm.fit(input, good)
    logm.predict(input)
    logm.score(input, good)

We end up with a value around .62, which is only slightly higher than random (random = .5, like a coin flip).

Question: What data can we use in this data frame to determine what kind of beer it is? This may be a better indicator!
Note, we can use regex's to create a new column. Write a function that groups our beers together using regex (example here):

    import re
    re.search('Apple', 'Apple Computer') != None # If this is true, then there was a match!

We'll be grouping our beers into Ale, Stout, IPA, and Lager. 
Of course, due to how we handle our data (numpy arrays), these have to be vectorized into four separate columns. 

Finally, we can create a logistic regression model using these four to predict if "Good" = 0 or 1.

    input = beer[ ['Ale', 'Stout', 'IPA', 'Lager'] ].values
    y = beer['Good'].values

    logm.fit(input, y)

And consider looking again at the coef_, intercept_, etc. We can consider precision based on |predicted - actual| as well as looking at .score().

Consider using set_params(penalty = 'l1') to see how your results change, and if this has become more precise or not. How does this align with what we discussed with l1 and l2 norm in lecture?

## Homework

Spend some time this weekend to predict the 2012 salary per player using the 2011 data in the data set below:

    http://cl.ly/RUED (note curl won't work here)

You'll need to "munge" through the data by plotting various data against Salary to understand the relationship for each value in order to interpret the best model. I'd focus around these to start with:

    [ ["HR", "RBI", 'R', "G", "SB", "salary", 'height', 'weight', 'yearID'] ]

but jump around and look at the variety of data available (and use feature selection!) to determine how significant the data available is in predicting salary.

Keep in mind that you cannot have a NEGATIVE salary, so if you have a negative prediction, whoops. :)