## Unit Project 2: Supervised Learning
*Due March 9, 2015.  Brief presentations in class.*

### After the project, you will be able to

Create a functional supervised learning model to predict (well or for naught!) a target variable.

### Contents of your submission include

You'll turn in [to the assignments form](https://) a link to a formatted ipython notebook - preferably on your github account as a gist or in a repo.  Be sure to run all cells in the notebook before turning it in.  Your notebook should include markdown headings and be well commented.

Your notebook should contain the following sections:

####Target

* Describe your target variable.
* Why is it interesting?
* How is the outcome represented?
* What might the benefits of creating a predictor be?
* Who would benefit most from predicting this variable?

* Include a labelled histogram and one additional graph that provides context for your target.

####Features

* Summarize the feature variables you will use to predict your target
* Produce histograms of each feature variable
* Include a scattermatrix
* Why did you choose these features?
* Explain, in words, how these features might be able to 'predict' the target.

####Data Preparation

* Show and notate the transformations, cleaning and other work you did to prepare your data for supervised learning into a features vector ("X") and a target vector ("Y")

####Test/Train Split

* Create a test/train split of your data.
* Explain the algorithm you used to perform the split

####Model Building

* Select an algorithm for your model and explain, briefly, how the model works and how you expect it to work with your features and target.  Chose from the following methods:
    * Linear Regression
    * Logistic Regression
    * Naive Bayes
    * Decision Trees

####Model Scoring

Using your test set, score the results of your model.

* Accuracy: Provide and explain the accuracy score
* AUC: Provide and explain the AUC score
* How does your classifier compare on the train vs test set?

####Predict

Using a set of features that you made up, or otherwise obtained which do not have a known target, predict the target using your classifier.

How do the results seem to you?

Stepping back from the scoring metrics, would you intuitively say that your classifier has  value?  If not, what are the minimum steps necessary so it can be of use?

####Results Summary

* Provide a few graphs that provide the results of your classifier on your test set
* Provide a few examples of specific features and their predicted outcome
