# Machine Learning Notetaker

Use this notetaker for each algorithm so you can keep track of the important information for each algorithm

## linear regression

> What data problem does it solve?

regression analysis (continuous, supervised learner)

> How do we evaluate performance?

R^2: explanation of variance in the data
p-values: explanation of relationship of features to the target variable
error: clearer relationship of error to the data, but scales with the data (to inf)

> What is the output?

predicted values for a y target.

> What is interpretable of the algorithm?

coefficients: contribution, or weights, for each feature to predict the target.
y_intercept: given all weights missing, the baseline target prediction

> How is it prone to overfitting?

Since any 2 points make a line, and any 3 points make a plane, etc., the more features you have, the more likely the model could become overfit. Polynomials and multicollinearity make that more so.

> How is it customizable?

Regularization: the w parameter represents either the sum (L1) or the squared sum (L2) of the coefficients, while the hyperparameter (`alpha` in sklearn) adjusts the size of that weight

