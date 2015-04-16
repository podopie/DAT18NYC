## Plotting decision surfaces of ensembles of trees on the iris dataset


Plot the decision surfaces of forests of randomized trees trained on pairs of features of the iris dataset.

This plot compares the decision surfaces learned by a decision tree classifier (first column), by a random forest classifier (second column), by an extra-trees classifier (third column) and by an AdaBoost classifier (fourth column).

In the first row, the classifiers are built using the sepal width and the sepal length features only, on the second row using the petal length and sepal length only, and on the third row using the petal width and the petal length only.

#### Code

    import numpy as np
    import pylab as pl

    from sklearn import clone
    from sklearn.datasets import load_iris

    # note: these imports are incorrect in the example online!
    from sklearn.ensemble.weight_boosting import AdaBoostClassifier
    from sklearn.ensemble.forest import (RandomForestClassifier,
                                            ExtraTreesClassifier)

    from sklearn.externals.six.moves import xrange
    from sklearn.tree import DecisionTreeClassifier

    # Parameters
    n_classes = 3
    n_estimators = 30
    plot_colors = "bry"
    plot_step = 0.02

    # Load data
    iris = load_iris()

    plot_idx = 1

    for pair in ([0, 1], [0, 2], [2, 3]):
        for model in (DecisionTreeClassifier(),
                      RandomForestClassifier(n_estimators=n_estimators),
                      ExtraTreesClassifier(n_estimators=n_estimators),
                      AdaBoostClassifier(DecisionTreeClassifier(),
                                         n_estimators=n_estimators)):
            # We only take the two corresponding features
            X = iris.data[:, pair]
            y = iris.target

            # Shuffle
            idx = np.arange(X.shape[0])
            np.random.seed(13)
            np.random.shuffle(idx)
            X = X[idx]
            y = y[idx]

            # Standardize
            mean = X.mean(axis=0)
            std = X.std(axis=0)
            X = (X - mean) / std

            # Train
            clf = model.fit(X, y)
            
            # Get accuracy scores
            scores = clf.score(X, y)
            # Create a title for each column and the console by using str() and slicing away useless parts of the string
            model_title = str(type(model)).split(".")[-1][:-2][:-len("Classifier")]
            model_details = model_title
            if hasattr(model, "estimators_"):
                model_details += " with {} estimators".format(len(model.estimators_))
            print model_details + " with features", pair, "has a score of", scores

            # Plot the decision boundary
            pl.subplot(3, 4, plot_idx)

            x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
            y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
            xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                                 np.arange(y_min, y_max, plot_step))

            if isinstance(model, DecisionTreeClassifier):
                Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
                Z = Z.reshape(xx.shape)
                cs = pl.contourf(xx, yy, Z, cmap=pl.cm.Paired)
            else:
                for tree in model.estimators_:
                    Z = tree.predict(np.c_[xx.ravel(), yy.ravel()])
                    Z = Z.reshape(xx.shape)
                    cs = pl.contourf(xx, yy, Z, alpha=0.1, cmap=pl.cm.Paired)

            pl.axis("tight")

            # Plot the training points
            for i, c in zip(xrange(n_classes), plot_colors):
                idx = np.where(y == i)
                pl.scatter(X[idx, 0], X[idx, 1], c=c, label=iris.target_names[i],
                           cmap=pl.cm.Paired)

            pl.axis("tight")

            plot_idx += 1

    pl.suptitle("Decision surfaces of DecisionTreeClassifier, "
                "RandomForestClassifier,\nExtraTreesClassifier"
                " and AdaBoostClassifier")
    pl.show()
    
## Application to other data sets

Here we have a dataset of chapters from books and plays by specific authors, and their usages of stop words. Let's see how accurately a random forest can predict the author based on stop word usage.

    import random
    from pandas import read_csv
    from sklearn.cross_validation import train_test_split
    from sklearn.ensemble.forest import ExtraTreesClassifier
    from sklearn import metrics
    from sklearn import preprocessing
    authorship = read_csv('http://people.stern.nyu.edu/jsimonof/AnalCatData/Data/Comma_separated/authorship.csv')
    authors = list(set(authorship.Author.values))
    le = preprocessing.LabelEncoder()
    le.fit(authors)
    authorship['Author_num'] = le.transform(authorship['Author'])

    #What are some of the stop words we're looking at?
    features = list(authorship.columns)
    features
    features.remove('Author')
    features.remove('Author_num')

    # Create a random variable (random forests work best with a random variable)
    # and create a test and training set
    authorship['random'] = [random.random() for i in range(841)]
    x_train, x_test, y_train, y_test = train_test_split(authorship[features], authorship.Author_num.values, test_size=0.4, random_state=123)


    # Fit Model
    etclf = ExtraTreesClassifier(n_estimators=20)
    etclf.fit(x_train, y_train)

    # Print Confusion Matrix
    metrics.confusion_matrix(etclf.predict(x_test), y_test)


## Classwork Questions/Exercises

1. With the authorship data, determine how changing the parameters in the random forest model changes the performance of the model. 

2. Also with the authorship data, feel free to go back to the base random forest classifer included in sklearn, or see how using adaboost does on guess work.

3. Try timing adaboost in comparison to randomforests to see how performance changes.

4. Consider building your own bagging algorithm (or get crazy and see if you can write up a simple boosting one) on your own. While this is relatively efficient in python, R users tend to complain a lot about how slow ensemble methods are (from the base packages). Building a strong understanding of these approaches can really move you along in the world of machine learning!

5. How can ensemble methods be distributed across a cluster of servers? Can they be?

## Resources
- [Random Forests in Python](http://blog.yhathq.com/posts/random-forests-in-python.html)
- [Random Forests for Kaggle](http://www.kaggle.com/c/titanic-gettingStarted/details/getting-started-with-random-forests)
- [Random Forests and Performance Metrics](http://citizennet.com/blog/2012/11/10/random-forests-ensembles-and-performance-metrics/)