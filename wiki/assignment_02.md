# Classifying if a used car purchase was a good deal or not

The data from this assignment was originally used for a kaggle competition. The intent is to determine if a used car purchase was a good deal or not worth the amount of work that would have to go into it (a 'lemon'). 

##Data

Data is included in the [repo](https://github.com/podopie/data_science_class_examples) under data/lemonsClassificationData. Included is the training set (which has 'IsBadBuy' included), the test set ('IsBadBuy' not included), and a description text file explaining each column.

##Objective

Clean up the data as needed and create a model for predicting if the car 'IsBadBuy'. You may use any of the classification algorithms learned (or still to learn) to predict this column, though given the data, some algorithms will be better than others.


##Submission file

Like the regression problem, submit both a gist of your python script and send us the output csv file which includes two columns:

    RefId, IsBadBuy
    3,0
    4,0
    8,1

This submission is based on the test csv file, which has the IsBadBuy column _missing_. This means that unlike the regression problem, you have to validate with your training data to feel more comfortable about your submission!

##Scoring

We will be scoring the submission based on the auc curve from precision and recall based on the two outputs.