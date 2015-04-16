## Objectives

* See a very basic example of K-means applied to a clear data set
* Work through an implementation of predicting the classes in the iris data set
* Application to data we're using

## Kmeans with good data

First things first, let's look at a readable and good application of kmeans with made up data:

    # load modules
    from sklearn import cluster
    from numpy import random
    from pandas import DataFrame, concat
    from matplotlib import pyplot as plt
    random.seed(1)

    classone = DataFrame({
        'x' :random.random(20) + 1,
        'y' : random.random(20) + 1,
        'label' : ['r' for i in range(20)]
    })
    classtwo = DataFrame({
        'x' :random.random(20) + 1,
        'y' : random.random(20) + 3,
        'label' : ['g' for i in range(20)]  
    })
    classthree = DataFrame({
        'x' :random.random(20) + 3,
        'y' : random.random(20) + 1,
        'label' : ['b' for i in range(20)]
    })
    classfour = DataFrame({
        'x' :random.random(20) + 3,
        'y' : random.random(20) + 3,
        'label' : ['purple' for i in range(20)]  
    })
    data = concat([classone, classtwo, classthree, classfour])

A quick scatter shows that yes, these are easy identifiable clusters.

    plt.scatter(data.x.values, data.y.values, color=list(data.label.values))
    plt.title('Really Easy Clusters')
    plt.show()

    cls = cluster.k_means(data[ ['x', 'y'] ].values, 4)
 
 Printing cls returns two arrays and a float.
 The first array is 'x' and 'y' for the centrioids of each cluster.
 The second array is the cluster values.
 The float represents the inertia.

    data['clusters'] = cls[1]

    plt.scatter(data.x.values, data.y.values, c=list(data.clusters.values))
    plt.title('Clusters Identifed by color')
    plt.show()

What happens when we introduce a new length of cluster?

    classfive = DataFrame({
        'x' : random.random(50) * 50 + 100,
        'y' : random.random(50) * 50 + 100,
        'label' : ['orange' for i in range(50)]
    })
    data = concat([data, classfive])
    cls = cluster.k_means(data[ ['x', 'y'] ].values, 5)
    data['clusters'] = cls[1]

Plot this. What happened here?

    plt.scatter(data.x.values, data.y.values, c=list(data.clusters.values))
    plt.title('Clusters Identifed by color')
    plt.show()


## Iris Data Application
    from sklearn import datasets
    iris = datasets.load_iris()
    cls = cluster.k_means(iris.data, 3)

Compare the results here. How did K-means do without any data changes?

    plt.subplot(211)
    plt.scatter(iris.data[:,:1], iris.data[:, 1:2], cmap=plt.cm.jet, c=iris.target)
    plt.subplot(212)
    plt.scatter(iris.data[:,:1], iris.data[:, 1:2], cmap=plt.cm.jet, c=list(cls[1]))
    plt.show()

## Application to data we're using

Kmeans is a really effective way of regrouping or reclassifying data that may make more sense to be viewed based on other variables. 

1. Consider a strategy here for the baseball problem: Could Kmeans be used to determine groups of players, which could then better predict salary?
2. Consider it's application to bad vs good used car purchases. What data could be used to to generate new car groups? What should those car groups represent?

## Resources
- [Blogpost on Insult Detection](http://blog.kaggle.com/2012/09/26/impermium-andreas-blog/)
- [Github Code of Insult Detection Solution](https://github.com/amueller/kaggle_insults/)
- [Choosing a ML Classifier](http://blog.echen.me/2011/04/27/choosing-a-machine-learning-classifier/)
- [KMeans IPython Notebook] (http://nbviewer.ipython.org/urls/raw.github.com/temporaer/tutorial_ml_gkbionics/master/2%2520-%2520KMeans.ipynb)
- [Cloudera ML KMeans](http://blog.cloudera.com/blog/2013/03/cloudera_ml_data_science_tools/)