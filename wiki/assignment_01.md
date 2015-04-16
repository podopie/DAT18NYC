# Regression Homework: Predicting a baseball player's Salary


## What is this
Using the baseball dataset provided, submit your best model in predicting 2012 Salaries for each individual player.

Since we do already have the actual answer, you should be testing your model against the real 2012 salary data to minimize error.


## What am I submitting

* Your python code: This should read in an unedited baseball.csv file, do all of your data manipulation, and produce the predicted values into a new csv file. That means you're also submitting...
* A csv of player name, year_id (2012), the predicted salary (your new response/y/output), and the actual salary (2012). This csv can be generated using the test csv file, generating the predicted values, and making a new pandas data frame.

## How is performance being measured?

We will be measuring error on a random sample set (roughly half of the submission) using MSE (Mean Squared Error). 

**Benchmark MSE**: 2.094098e+13<br />
Or a more readable benchmark on R-Squared: 0.1322

Find ways to improve the model and perform better than the benchmark provided.

## How can I keep track of my own results and how I am doing?

1. You can easily grab a clean data set of just 2011 (training) and 2012 (test with no missing values) from this repo (in the homework folder). This should make your data munging much easier.
1. This assignment is ongoing. You can always submit a new model as you play with this data more often.
2. Use the mean_squared_error metric available in scikit learn to measure your own performance and compare it to the benchmark.


###A Good submission will:
* beat the benchmark
* prove you understand how a regression works

###A Great submission will:
* beat the benchmark
* Show there was some exploration of the data set available in determining the most ideal model to submit
* Likely attempted to go through all continuous data points in order to best predict salary

###An Excellent submission will:
* beat the benchmark
* Show there was some exploration of the data set available in determining the most ideal model to submit
* Experiment with text data (bats, throws, team, league) and calculate new fields based on available data (age at playing year, etc)