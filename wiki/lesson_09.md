## Objectives

* Implement the decision tree classification to the test iris set
* Review the implementation and output of a confusion matrix
* Error terms: Precision and Recall

## Decision Tree Implementation

Iris implementation (as per usual):


    from sklearn import datasets, metrics, tree, cross_validation
    from matplotlib import pyplot as plt
    iris = datasets.load_iris()
    y_pred = tree.DecisionTreeClassifier().fit(iris.data, iris.target).predict(iris.data)
    print("Number of mislabeled points : %d" % (iris.target != y_pred).sum())
    print("Absolutely ridiculously overfit score: %d" % (tree.DecisionTreeClassifier().fit(iris.data, iris.target).score(iris.data, iris.target)))

BEFORE we discuss the over-the-top overfitting with this model, get acquainted with two more important views of error to understand the performance of the model.

## Confusion Matrices

Confusion matrices allow you to view actual v predicted for all class labels. Since this model seems to be "perfect," we can use this an an example of how to read a confusion matrix:

    metrics.confusion_matrix(iris.target, clf.predict(iris.data))
    
Similar to the identity matrix from earlier in class, a "perfect" prediction will result in complete matches at the diagonal and zeroes in all other places. However, this is not typical, so expect to see mismatches by reading it predicted (horizontal) vs actual (vertical).


## Precision and Recall

Precision and recall are best explained as follows:

* **Precision**: Of predicted value X, how many were actually X? (translation: of all predicted cats in a photo of cats and dogs, how many were actually cats?)
* **Recall**: Of all the possible Xs, how many did you find? (translation, of all the possible cats in the photo, how many did you find?)

Conveniently, we can use precision and recall with sklearn. (In a binary example, we can even create a different AUC using precision and recall).

    print metrics.classification_report(iris.target, clf.predict(iris.data))

## Generalizing our tree

As mentioned before, having a perfect model is more often _scary_. We know this is overfitting by using a test/train set from iris.

    x_train, x_test, y_train, y_test = cross_validation.train_test_split(iris.data, iris.target, test_size=.3)
    clf.fit(x_train, y_train)
    metrics.confusion_matrix(y_train, clf.predict(x_train))
    print metrics.classification_report(y_train, clf.predict(x_train))
    metrics.confusion_matrix(y_test, clf.predict(x_test))
    print metrics.classification_report(y_test, clf.predict(x_test))
    
Though the concept of "pruning" is not as clear in sklearn (specifically since decision trees are only included as a "well-known" model), we can generalize the model by changing the defaults of min_samples_leaf and max_depth.

    clf.set_params(min_samples_leaf=5)
    clf.set_params(max_depth=5)
    clf.fit(x_train, y_train)
    metrics.confusion_matrix(y_train, clf.predict(x_train))
    metrics.confusion_matrix(y_test, clf.predict(x_test))

## Homework

You can find the ongoing classification assignment [here](https://github.com/podopie/data_science_class_examples/wiki/OngoingAssignment_02:-Classification-Model-Predicting-Good-Bad-Used-Car-Purchase).