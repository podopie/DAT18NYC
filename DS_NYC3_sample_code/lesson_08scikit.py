
# scikit examples
"""
Iris data set, using Support Vector Clustering
"""
from sklearn import svm, datasets
from sklearn.metrics import confusion_matrix
iris = datasets.load_iris()

mysvm = svm.SVC().fit(iris.data, iris.target)
mysvm_pred = mysvm.predict(iris.data)
print confusion_matrix(mysvm_pred, iris.target)

"""
Naive Bayesian Classifier
"""
from sklearn import datasets
iris = datasets.load_iris()
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
print "Number of mislabeled points : %d" % (iris.target != y_pred).sum()

# compare results!
print iris.target
print y_pred

"""
Linear Regression using pylab (matplotlib), numpy, and a diabetes data set
"""
print __doc__

# Code source: Jaques Grobler
# License: BSD
import pylab as pl
import numpy as np
from sklearn import datasets, linear_model

# Load the diabetes dataset
diabetes = datasets.load_diabetes()


# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis]
diabetes_X_temp = diabetes_X[:, :, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X_temp[:-20]
diabetes_X_test = diabetes_X_temp[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# The coefficients
print 'Coefficients: \n', regr.coef_
# The mean square error
print ("Residual sum of squares: %.2f" %
       np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print ('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))

# Plot outputs
pl.scatter(diabetes_X_test, diabetes_y_test,  color='black')
pl.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',
        linewidth=3)

pl.xticks(())
pl.yticks(())

pl.show()