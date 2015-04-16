# Naive Bayes Classifier 

## Goals
* Apply a Naive Bayes algorithm to a classification problem
* Scoring classification algorithms using AUC
* Work through the data mining workflow to build an insult classifier.

## Naive Bayes Application
Like we did with KNN, let's use the Iris data set first to verify that the algorithm works as it should:

    from sklearn import datasets, metrics
    from matplotlib import pyplot as plt
    iris = datasets.load_iris()
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
    print("Number of mislabeled points : %d" % (iris.target != y_pred).sum())
    
## ROC and AUC

As we keep learning algorithms, we'll also approach various ways to score our algorithms. Above we used a simple mislabel count to determine a score: 6 mislabels/150 total or 144 right/150 total = .96 (obviously here, we want as close to 1 as possible).

One way we can score a binary classification is by plotting the reciever operating characteristic and determining the value of the area under curve (AUC). Again, our goal is to see an AUC as close to 1 as possible.

    # Finding the false positive and true positive rates where the positive label is 2.
    fpr, tpr, thresholds = metrics.roc_curve(iris.target, y_pred, pos_label=2)
    metrics.auc(fpr, tpr)
    plt.plot(fpr, tpr)
    plt.show()
    
## Insult Classifier

As a class, let's go through all the steps to build an insult classifier based on the data available in the repo (train and test in the naiveBayes folder). Approach this problem like we'd approach any problem in class, and in the data science workflow:

1. What does the data that we have look like?
2. What is the goal--the question we're trying to answer?
3. What does the data throughput have to look like?
4. What are the steps to get us there?


Class example: [https://gist.github.com/podopie/9e0a2e64d928ff94f2a0](https://gist.github.com/podopie/9e0a2e64d928ff94f2a0)