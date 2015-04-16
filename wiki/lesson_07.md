# KNN Classification, Training and Testing Data, Cross Validation

## Goals:
* Apply the KNN Algorithm
* Using an RNG to cross validate performance
* Compare results to Logistic Regression

## Applying the KNN Algorithm

The best data set to validate any classification algorithm's performance is the [Fisher Iris data set](http://en.wikipedia.org/wiki/Iris_flower_data_set), which is commonly included in any stats or machine learning package.

    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap
    from sklearn import neighbors, datasets, feature_selection

    # Various variables we'll need to set intially.
    n_neighbors = range(1, 101)
    np.random.seed(1234)

    # Load in the data and seperate the class labels and input data
    iris = datasets.load_iris()
    X = iris.data[:, :4]
    y = iris.target

    # Create the training (and test) set using the rng in numpy
    n = len(y) * .7
    ind = np.hstack((np.ones(n, dtype=np.bool), np.zeros(len(y) - n, dtype=np.bool)))
    np.random.shuffle(ind)
    X_train, X_test = X[ind], X[ind == False]
    y_train, y_test = y[ind], y[ind == False]

    # Loop through each neighbors value from 1 to 100 and append
    # the scores
    scores = []
    for n in n_neighbors:
        clf = neighbors.KNeighborsClassifier(n, weights='uniform')
        clf.fit(X_train, y_train)
        scores.append(clf.score(X_train, y_train))

    plt.plot(n_neighbors, scores)
    plt.show()

## Application of Cross Validation

The work above shows that at 21 neighbors, we can get an ideal result that doesn't overfit the data. To verify this, we'll use cross validation.

    scores = []
    for k in range(5):
        np.random.shuffle(ind)
        X_train, X_test = X[ind], X[ind == False]
        y_train, y_test = y[ind], y[ind == False]
        clf = neighbors.KNeighborsClassifier(21, weights='uniform')
        clf.fit(X_train, y_train)
        scores.append(clf.score(X_test, y_test))

    print scores
    print np.mean(scores)

To showcase our whole model's performance, we can plot our algorithm against the two most significant features available in this data set.

    # Below returns highest signifiance for features 2 and 3
    # (remember, Python uses index 0). 
    feature_selection.f_classif(X, y)

    h = .02  # step size in the mesh

    # Create color maps
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

    clf = neighbors.KNeighborsClassifier(21, weights='uniform')
    clf.fit(X[:, 2:4], y)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    x_min, x_max = X[:, 2].min() - 1, X[:, 2].max() + 1
    y_min, y_max = X[:, 3].min() - 1, X[:, 3].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)

    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    plt.scatter(X[:, 2], X[:, 3], c=y, cmap=cmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')"
             % (21, 'uniform'))

    plt.show()

## Homework: Compare Results

Using the beer data set from the [previous class](https://github.com/podopie/data_science_class_examples/wiki/Lesson_06:-Polynomial-and-Logistic-Regression), compare the results between prediction a good beer using the Logistic regression implementation on that page, and your own implementation of KNN. Use training and testing data with both algorithms and cross validate your model!